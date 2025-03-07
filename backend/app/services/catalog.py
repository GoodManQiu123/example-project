"""
Overview:
This script facilitates the extraction and storage of academic article data from structured files into a database.
It processes JSON files containing article metadata, authors, references, and topics, and saves this information
using CRUD operations. The script supports batch processing of files within directories, and also provides functions
to generate structured responses for various queries, such as searching for papers by filter criteria, exploring
topics, authors, co-authorships, and citation trees.

Key Components:
- save_parse_article: Processes an article from various input formats and saves it to the database.
- save_parse_article_with_filepath: Processes and saves an article given a path to its JSON file.
- save_parse_articles_within_dir: Recursively processes and saves articles from JSON files in a specified directory.
- search_papers_by_filter_as_response: Returns a structured response with papers that meet specified filter criteria.
- search_topics_by_filter_as_response: Generates a response listing topics based on given filter criteria.
- search_authors_by_filter_as_response: Retrieves authors matching specified filters and structures the response.
- search_same_topic_by_filter_as_response: Identifies articles sharing topics and organizes the information.
- search_co_author_by_filter_as_response: Explores co-authorship relations based on article filters.
- search_cited_tree_by_filter_as_response: Constructs a citation tree showing how articles reference each other.

Usage:
The script can be utilized in a backend system for academic article management, where it would parse, store, and
retrieve article data for various applications, such as content management systems, research databases, or academic
network analysis tools. It provides a comprehensive approach to handling academic article data with flexibility and
scalability.
"""

import json
import os
from pathlib import Path

from ..integration.catalog_access import ArticleCRUD, AuthorCRUD, ArticleAuthorCRUD, \
    ArticleCitationCRUD, TopicCRUD, ArticleTopicCRUD
from ..services.Parser.types import ArticleObject
from ..services.models import ParseArticleVO, ArticleVO, AuthorVO, ArticleAuthorVO, ArticleCitationVO, \
    AuthorFilter, ArticleFilter, ArticleAuthorFilter, TopicFilter, TopicVO, ArticleTopicVO, ArticleCitationFilter, \
    ArticleTopicFilter, ParseReferenceAuthorVO
from ..services.schema import PaperResponse, PaperItemSchema, AuthorSchema, TopicResponse, TopicItemSchema, \
    AuthorResponse, AuthorItemSchema, SameTopicConnectionItemSchema, SameTopicDataSchema, SameTopicResponseSchema, \
    CoAuthorResponseSchema, CoAuthorDataSchema, CoAuthorConnectionItemSchema, TopicSchema, CitedTreeResponseSchema, \
    CitedTreeDataSchema, CitedConnectionItemSchema


def save_parse_article(parse_article: ParseArticleVO | dict | ArticleObject) -> ArticleVO | None:
    """
    This function processes and saves the article metadata, authors, references, and topics to the database.

    @param parse_article: The ParseArticleVO, dict, or ArticleObject containing the article information.
    @return: None
    """

    # Type checking and conversion
    if isinstance(parse_article, ParseArticleVO):
        # If the input is already a ParseArticleVO instance, use it directly
        parse_article_vo = parse_article
    elif isinstance(parse_article, dict):
        parse_article_vo = ParseArticleVO.from_dict(parse_article)
    elif isinstance(parse_article, ArticleObject):
        parse_article_vo = ParseArticleVO.from_dict(parse_article.to_dict())
    else:
        raise ValueError("Unsupported type for parse_article_vo")

    # Initialize CRUD operation classes
    article_crud = ArticleCRUD()
    author_crud = AuthorCRUD()
    article_author_crud = ArticleAuthorCRUD()
    article_citation_crud = ArticleCitationCRUD()
    topic_crud = TopicCRUD()
    article_topic_crud = ArticleTopicCRUD()

    article_data_lst = article_crud.search_by_filter(ArticleFilter(title=parse_article_vo.metadata.title,
                                                                   doi=parse_article_vo.metadata.doi))

    if not article_data_lst:
        # Process and save the article metadata
        article_data = ArticleVO(
            title=parse_article_vo.metadata.title,
            abstract=parse_article_vo.content.abstract,
            publisher=parse_article_vo.metadata.publisher,
            date=parse_article_vo.metadata.published_date,
            doi=parse_article_vo.metadata.doi,
            container_title=parse_article_vo.metadata.journal
        )

        try:
            # Save the article to the database
            saved_article = article_crud.create(article_data)
        except Exception as e:
            print(f"Error saving article: {e}")
            return  # or handle error accordingly

        # Process and save authors with their affiliations
        for parse_author_vo in parse_article_vo.authors:
            # Check if the author already exists in the database
            author_vo_list = author_crud.search_by_filter(
                AuthorFilter(name=parse_author_vo.name, email=parse_author_vo.email))
            if author_vo_list:
                # If the author exists, use the existing author
                saved_author = author_vo_list[0]
            else:
                # If the author does not exist, save the author
                try:
                    saved_author = author_crud.create(AuthorVO(name=parse_author_vo.name,
                                                               email=parse_author_vo.email,
                                                               affiliation=parse_author_vo.affiliation))
                except Exception as e:
                    print(f"Error saving author: {e}")
                    continue  # or handle error accordingly

            # Associate the author with the saved article
            if not article_author_crud.get_by_filter(ArticleAuthorFilter(article_id=saved_article.article_id,
                                                                         author_id=saved_author.author_id)):
                try:
                    article_author_crud.create(
                        ArticleAuthorVO(article_id=saved_article.article_id, author_id=saved_author.author_id))
                except Exception as e:
                    print(f"Error creating article-author relationship: {e}")
                    # Decide whether to continue or handle differently

            # Process and save the author's affiliation (Future work)

        # Process and save references (as articles) and create citation relationships
        for parse_reference_vo in parse_article_vo.references:
            # Check if the reference already exists in the database
            reference_article_lst = article_crud.search_by_filter(
                ArticleFilter(title=parse_reference_vo.title,
                              doi=parse_reference_vo.doi))

            # If the reference exists, use the existing reference
            if reference_article_lst:
                # If the reference exists, use the existing reference
                reference_article = reference_article_lst[0]
            else:
                # If the reference does not exist, save the reference
                article_vo = ArticleVO(
                    title=parse_reference_vo.title,
                    doi=parse_reference_vo.doi,
                    date=parse_reference_vo.published_date,
                    container_title=parse_reference_vo.container_title[0]
                    if parse_reference_vo.container_title
                    else None
                )
                try:
                    # Save the reference article to the database
                    reference_article = article_crud.create(article_vo)
                except Exception as e:
                    print(f"Error saving reference article: {e}")
                    continue  # or handle error accordingly

            # Check if the authors of reference article already exist in the database
            for reference_author_vo in parse_reference_vo.authors:
                if isinstance(reference_author_vo, dict):
                    reference_author_vo = ParseReferenceAuthorVO.from_dict(reference_author_vo)
                if not isinstance(reference_author_vo, ParseReferenceAuthorVO):
                    continue
                reference_author_name = f"{reference_author_vo.given} {reference_author_vo.family}".strip()
                reference_author_vo_list = author_crud.search_by_filter(
                    AuthorFilter(name=reference_author_name))
                if reference_author_vo_list:
                    # If the author exists, use the existing author
                    reference_author = reference_author_vo_list[0]
                else:
                    # If the author does not exist, save the author
                    try:
                        reference_author = author_crud.create(AuthorVO(name=reference_author_name))
                    except Exception as e:
                        print(f"Error saving reference author: {e}")
                        continue

                # Associate the author with the saved article
                if not article_author_crud.get_by_filter(ArticleAuthorFilter(article_id=reference_article.article_id,
                                                                             author_id=reference_author.author_id)):
                    try:
                        article_author_crud.create(
                            ArticleAuthorVO(article_id=reference_article.article_id,
                                            author_id=reference_author.author_id))
                    except Exception as e:
                        print(f"Error creating article-author relationship: {e}")
                        # Decide whether to continue or handle differently

            try:
                if not article_citation_crud \
                        .get_by_filter(ArticleCitationFilter(citing_article_id=saved_article.article_id,
                                                             cited_article_id=reference_article.article_id)):
                    article_citation_crud.create(ArticleCitationVO(citing_article_id=saved_article.article_id,
                                                                   cited_article_id=reference_article.article_id))
            except Exception as e:
                print(f"Error creating article citation: {e}")
                # Decide whether to continue or handle differently

        # Process and save topics and create relationships between articles and topics
        for keyword in parse_article_vo.content.keywords:
            topic_vo = topic_crud.get_by_filter(TopicFilter(name=keyword))
            if topic_vo:
                topic_vo = topic_vo[0]
            else:
                try:
                    topic_vo = topic_crud.create(TopicVO(name=keyword))
                except Exception as e:
                    print(f"Error saving topic: {e}")
                    continue  # or handle error accordingly

            try:
                article_topic_crud.create(
                    ArticleTopicVO(article_id=saved_article.article_id, topic_id=topic_vo.topic_id))
            except Exception as e:
                print(f"Error creating article-topic relationship: {e}")
                # Decide whether to continue or handle differently
        return saved_article
    else:
        return article_data_lst[0]


def save_parse_article_with_filepath(file_path: str) -> ArticleVO:
    """
    Processes a JSON file containing article metadata and saves the article to the database.

    @param file_path: The path to the JSON file containing article metadata.
    @return: The saved ArticleVO object.
    """
    # Open the JSON file and load its content
    with open(file_path, 'r', encoding='utf-8') as f:
        # Load the JSON content into a ParseParseArticleVO object
        parse_article_vo = ParseArticleVO.from_dict(json.load(f))
        # Call the function to process the parsed article object
        return save_parse_article(parse_article_vo)


def save_parse_articles_within_dir(folder_path) -> list[ArticleVO]:
    """
    Recursively processes each JSON file in a given folder and its subfolders.

    @param folder_path: The path to the folder containing JSON files to process.
    @return: None
    """
    # Initialize an empty list to store the parsed article objects
    parse_article_vo_lst: list[ArticleVO] = []
    # Traverse all files and subdirectories within the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a JSON file based on its extension
            if Path(file).suffix == '.json':
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                try:
                    # Open the JSON file and load its content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parse_article_vo = ParseArticleVO.from_dict(json.load(f))
                        parse_article_vo_lst.append(parse_article_vo)
                    # Call the function to process the parsed article object
                    save_parse_article(parse_article_vo)
                except Exception as e:
                    # Print an error message if something goes wrong
                    print(f"Error processing file {file_path}: {e}")
    return parse_article_vo_lst


def search_papers_by_filter_as_response(filter_obj: ArticleFilter) -> PaperResponse:
    """
    Get a list of papers based on the given filter and return a PaperResponse object.

    @param filter_obj: An ArticleFilter object containing the filter criteria.
    @return: A PaperResponse object containing the list of papers.
    """
    article_crud = ArticleCRUD()
    author_crud = AuthorCRUD()
    article_author_crud = ArticleAuthorCRUD()

    # Get the list of ArticleVOs based on the filter
    article_vo_lst = article_crud.search_by_filter(filter_obj)

    # Convert the list of ArticleVOs to a list of PaperItemVOs
    paper_items = []
    for article_vo in article_vo_lst:
        PaperItemSchema(article_id=article_vo.article_id, title=article_vo.title, authors=[])

        # Get the authors for the article
        article_author_vo_lst = article_author_crud.get_by_filter(ArticleAuthorFilter(article_id=article_vo.article_id))
        author_lst = []
        for article_author_vo in article_author_vo_lst:
            # Get the author details
            author_vo = author_crud.get_by_filter(AuthorFilter(author_id=article_author_vo.author_id))[0]
            if not author_vo:
                continue
            # Add the author to the list
            author_lst.append(AuthorSchema(author_id=author_vo.author_id,
                                           name=author_vo.name,
                                           email=author_vo.email,
                                           affiliation=author_vo.affiliation))

        # Create a PaperItemVO for the article
        paper_item = PaperItemSchema(article_id=article_vo.article_id, title=article_vo.title, authors=author_lst)
        paper_items.append(paper_item)

    # Create and return the PaperResponse object
    paper_response = PaperResponse(code=200, msg="Success", data=paper_items)
    return paper_response


def search_topics_by_filter_as_response(filter_obj: TopicFilter) -> TopicResponse:
    """
    Get a list of topics based on the given filter and return a TopicResponse object.

    @param filter_obj: A TopicFilter object containing the filter criteria.
    @return: A TopicResponse object containing the list of topics.
    """
    topic_crud = TopicCRUD()
    article_topic_crud = ArticleTopicCRUD()

    # Get the list of TopicVOs based on the filter
    topic_vo_lst = topic_crud.search_by_filter(filter_obj)

    # Convert the list of TopicVOs to a list of TopicItemVOs
    topic_items = []
    for topic_vo in topic_vo_lst:
        count = len(article_topic_crud.get_by_filter(ArticleTopicFilter(topic_id=topic_vo.topic_id)))
        # Create a TopicItemVO for the topic
        topic_item = TopicItemSchema(topic_id=topic_vo.topic_id,
                                     topic=topic_vo.name,
                                     count=count)  # Set count to 0 for now
        topic_items.append(topic_item)

    # Create and return the TopicResponse object
    topic_response = TopicResponse(code=200, msg="Success", data=topic_items)
    return topic_response


def search_authors_by_filter_as_response(filter_obj: AuthorFilter) -> AuthorResponse:
    """
    Get a list of authors based on the given filter and return an AuthorResponse object.

    @param filter_obj: An AuthorFilter object containing the filter criteria.
    @return: An AuthorResponse object containing the list of authors.
    """
    author_crud = AuthorCRUD()
    article_author_crud = ArticleAuthorCRUD()

    # Get the list of AuthorVOs based on the filter
    author_vo_lst = author_crud.search_by_filter(filter_obj)

    # Convert the list of AuthorVOs to a list of AuthorItemVOs
    author_items = []
    for author_vo in author_vo_lst:
        count = len(article_author_crud.get_by_filter(ArticleAuthorFilter(author_id=author_vo.author_id)))
        # Create an AuthorItemVO for the author
        author_item = AuthorItemSchema(author_id=author_vo.author_id, name=author_vo.name, count=count)
        author_items.append(author_item)

    # Create and return the AuthorResponse object
    author_response = AuthorResponse(code=200, msg="Success", data=author_items)
    return author_response


def search_same_topic_by_filter_as_response(filter_obj: ArticleFilter) -> SameTopicResponseSchema:
    """
    Based on the provided ArticleFilter, this function identifies articles that share the same topic(s)
    and aggregates information related to these articles, such as related topics and authors. It returns
    a structured response that includes connections between topics and articles, a list of topics with their
    details, and a list of papers with their authors.

    @param filter_obj: An ArticleFilter object containing the filter criteria.
    @return: A SameTopicResponseSchema object containing structured information about topics, articles, and authors.
    """
    try:
        # Initialize CRUD operations for articles, topics, and authors
        article_crud = ArticleCRUD()
        topic_crud = TopicCRUD()
        author_crud = AuthorCRUD()
        article_author_crud = ArticleAuthorCRUD()

        # Fetch the first article that matches the filter criteria
        article_vo = article_crud.get_by_filter(filter_obj)[0]

        # Initialize CRUD operation for article-topic relationships
        article_topic_crud = ArticleTopicCRUD()

        # Fetch topics related to the article
        article_topic_vo_lst = article_topic_crud.get_by_filter(ArticleTopicFilter(article_id=article_vo.article_id))

        same_topic_connection_item_schema_lst: list[SameTopicConnectionItemSchema] = []
        article_id_set: set[int] = set()
        article_id_set.add(article_vo.article_id)

        # Iterate over each topic related to the article
        for article_topic_vo in article_topic_vo_lst:
            # Fetch articles related to the current topic
            paper_id_lst: list[int] = [item.article_id for item in article_topic_crud.get_by_filter(
                ArticleTopicFilter(topic_id=article_topic_vo.topic_id))]

            # Update the set of unique article IDs
            for paper_id in paper_id_lst:
                article_id_set.add(paper_id)

            # Append information about the topic and related articles
            same_topic_connection_item_schema_lst.append(SameTopicConnectionItemSchema(topic=article_topic_vo.topic_id,
                                                                                       papers=paper_id_lst))

        topic_item_schema_lst: list[TopicSchema] = []

        # Iterate over each topic again to fetch detailed topic information
        for article_topic_vo in article_topic_vo_lst:
            topic_vo = topic_crud.get_by_filter(TopicFilter(topic_id=article_topic_vo.topic_id))[0]
            topic_item_schema_lst.append(TopicSchema(topic_id=topic_vo.topic_id,
                                                     name=topic_vo.name))

        paper_item_schema_lst: list[PaperItemSchema] = []

        # Iterate over each unique article ID to fetch detailed article and author information
        for article_id in article_id_set:
            article_vo = article_crud.get_by_filter(ArticleFilter(article_id=article_id))[0]
            article_author_vo_lst = article_author_crud.get_by_filter(ArticleAuthorFilter(article_id=article_id))

            author_schema_lst: list[AuthorSchema] = []

            # Fetch detailed author information for each article
            for article_author_vo in article_author_vo_lst:
                author_vo = author_crud.get_by_filter(AuthorFilter(author_id=article_author_vo.author_id))[0]
                author_schema_lst.append(AuthorSchema(author_id=author_vo.author_id,
                                                      name=author_vo.name,
                                                      email=author_vo.email,
                                                      affiliation=author_vo.affiliation))

            # Append information about the article and its authors
            paper_item_schema_lst.append(PaperItemSchema(article_id=article_vo.article_id,
                                                         title=article_vo.title,
                                                         authors=author_schema_lst))

        # Return the structured response containing topics, articles, and authors
        return SameTopicResponseSchema(code=200,
                                       msg="Success",
                                       data=SameTopicDataSchema(connections=same_topic_connection_item_schema_lst,
                                                                topics=topic_item_schema_lst,
                                                                papers=paper_item_schema_lst))
    except Exception as e:
        # Handle exceptions and return an appropriate error response
        # This is a generic handler; you might want to catch and handle different exceptions differently
        return SameTopicResponseSchema(code=500,
                                       msg=f"An error occurred: {str(e)}",
                                       data=[])


def search_co_author_by_filter_as_response(filter_obj: ArticleFilter) -> CoAuthorResponseSchema:
    """
    Based on the provided ArticleFilter, this function identifies articles and aggregates information about their
    authors, specifically focusing on co-authorship relations. It returns a structured response that includes
    co-authorship connections, detailed author information, and a list of related papers.

    @param filter_obj: An ArticleFilter object containing the filter criteria.
    @return: A CoAuthorResponseSchema object containing structured information about co-authorships, authors,
    and papers.
    """
    try:
        # Initialize CRUD operations for articles and authors
        article_crud = ArticleCRUD()
        author_crud = AuthorCRUD()
        article_author_crud = ArticleAuthorCRUD()

        # Fetch the first article that matches the filter criteria
        article_vo = article_crud.get_by_filter(filter_obj)[0]

        # Fetch authorship information for the article
        article_author_vo_lst = article_author_crud.get_by_filter(ArticleAuthorFilter(article_id=article_vo.article_id))

        co_author_connection_item_schema_lst: list[CoAuthorConnectionItemSchema] = []
        article_id_set: set[int] = set()
        article_id_set.add(article_vo.article_id)

        # Iterate over each author of the article
        for article_author_vo in article_author_vo_lst:
            # Fetch articles co-authored by the current author
            paper_id_lst: list[int] = [item.article_id for item in article_author_crud.get_by_filter(
                ArticleAuthorFilter(author_id=article_author_vo.author_id))]

            # Update the set of unique article IDs
            for paper_id in paper_id_lst:
                article_id_set.add(paper_id)

            # Append information about the author and their co-authored papers
            co_author_connection_item_schema_lst.append(CoAuthorConnectionItemSchema(author=article_author_vo.author_id,
                                                                                     papers=paper_id_lst))

        author_schema_lst: list[AuthorSchema] = []

        # Iterate over each author again to fetch detailed author information
        for article_author_vo in article_author_vo_lst:
            author_vo = author_crud.get_by_filter(AuthorFilter(author_id=article_author_vo.author_id))[0]
            author_schema_lst.append(AuthorSchema(author_id=author_vo.author_id,
                                                  name=author_vo.name,
                                                  email=author_vo.email,
                                                  affiliation=author_vo.affiliation))

        paper_item_schema_lst: list[PaperItemSchema] = []

        # Iterate over each unique article ID to fetch detailed article information
        for article_id in article_id_set:
            article_vo = article_crud.get_by_filter(ArticleFilter(article_id=article_id))[0]

            # Append information about the article and its authors
            paper_item_schema_lst.append(PaperItemSchema(article_id=article_vo.article_id,
                                                         title=article_vo.title,
                                                         authors=author_schema_lst))

        # Return the structured response containing co-authorships, authors, and papers
        return CoAuthorResponseSchema(code=200,
                                      msg="Success",
                                      data=CoAuthorDataSchema(connections=co_author_connection_item_schema_lst,
                                                              authors=author_schema_lst,
                                                              papers=paper_item_schema_lst))
    except Exception as e:
        # Handle exceptions and return an appropriate error response
        # This is a generic handler; specific exceptions can be caught and handled differently if needed
        return CoAuthorResponseSchema(code=500,
                                      msg=f"An error occurred: {str(e)}",
                                      data=[])


def search_cited_tree_by_filter_as_response(filter_obj: ArticleFilter, level_num: int = 5) -> CitedTreeResponseSchema:
    """
    Retrieves a structured response that outlines the citation relationships between articles
    and their associated metadata, based on the given filter criteria and up to a certain level of citation depth.
    This function maps out how articles cite each other, forming a tree-like structure of citations.

    @param filter_obj: An object containing filter criteria for article retrieval.
    @param level_num: The maximum depth of citation connections to retrieve, defining how far the citation
                      chain should be explored. Level 0 starts with the initial article.
    @return: A structured response with citation connections and article metadata, including titles and authors.
    """

    # Initialize CRUD operations for articles, citations, and authors
    article_crud = ArticleCRUD()
    article_citation_crud = ArticleCitationCRUD()
    article_author_crud = ArticleAuthorCRUD()
    author_crud = AuthorCRUD()

    # Retrieve the initial article based on the filter criteria
    article_vo = article_crud.get_by_filter(filter_obj)[0]

    # Initialize a set with the ID of the initial article
    article_id_set: set[int] = {article_vo.article_id}

    # Initialize the list to store connections between citing and cited articles
    cited_connection_item_schema_lst: list[CitedConnectionItemSchema] = []

    # Iterate through each level of citation from the initial article to the maximum specified level
    current_level_citing_articles = [article_vo.article_id]
    for level in range(level_num):
        if not current_level_citing_articles:
            break  # Exit the loop if there are no more articles citing at the current level

        # Prepare to collect articles cited by those at the current level
        next_level_cited_articles = []

        # Iterate through each article at the current level to find articles they cite
        for citing_article_id in current_level_citing_articles:
            # Retrieve articles cited by the current article
            article_citation_vo_lst = article_citation_crud.get_by_filter(
                ArticleCitationFilter(citing_article_id=citing_article_id)
            )

            # Process each citation to collect cited article IDs and prepare for the next level
            cited_article_id_lst: list[int] = []
            for article_citation_vo in article_citation_vo_lst:
                cited_article_id = article_citation_vo.cited_article_id
                article_id_set.add(cited_article_id)  # Add to the set of all encountered article IDs
                if cited_article_id not in current_level_citing_articles:
                    cited_article_id_lst.append(cited_article_id)
                    next_level_cited_articles.append(cited_article_id)

            # Log or debug output to track the citation chain; this line can be commented out or removed in production
            # print(f"Level {level}: {citing_article_id} -> {cited_article_id_lst}")

            # Store the citation connection if the current article cites others
            if cited_article_id_lst:
                cited_connection_item_schema_lst.append(CitedConnectionItemSchema(from_paper=citing_article_id,
                                                                                  to_paper=cited_article_id_lst))
        # Make sure to remove duplicates from the list of articles cited in the next level
        next_level_cited_articles = list(set(next_level_cited_articles))
        for article_id in current_level_citing_articles:
            if article_id in next_level_cited_articles:
                next_level_cited_articles.remove(article_id)
        # Move to the next level with the list of articles cited in the current level
        current_level_citing_articles = next_level_cited_articles

    # Collect detailed metadata for all articles encountered in the citation tree
    paper_item_schema_lst: list[PaperItemSchema] = []
    for article_id in article_id_set:
        # Retrieve the article and its authors' details
        article_vo = article_crud.get_by_filter(ArticleFilter(article_id=article_id))[0]
        article_author_vo_lst = article_author_crud.get_by_filter(ArticleAuthorFilter(article_id=article_id))

        # Collect author information for the current article
        author_schema_lst: list[AuthorSchema] = []
        for article_author_vo in article_author_vo_lst:
            author_vo = author_crud.get_by_filter(AuthorFilter(author_id=article_author_vo.author_id))[0]
            author_schema_lst.append(AuthorSchema(author_id=author_vo.author_id,
                                                  name=author_vo.name,
                                                  email=author_vo.email,
                                                  affiliation=author_vo.affiliation))

        # Store detailed information about the article, including its authors
        paper_item_schema_lst.append(PaperItemSchema(article_id=article_vo.article_id,
                                                     title=article_vo.title,
                                                     authors=author_schema_lst))

    # Construct and return the response schema with all collected data
    return CitedTreeResponseSchema(code=200,
                                   msg="Success",
                                   data=CitedTreeDataSchema(connections=cited_connection_item_schema_lst,
                                                            papers=paper_item_schema_lst))
