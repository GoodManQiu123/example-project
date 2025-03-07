"""
Overview:
This testing script is designed to validate the parsing functionality of an article analysis system, ensuring that
various components such as metadata, content, references, and author details are accurately extracted from academic
papers. It leverages test cases stored in JSON format to compare expected results against parsed outputs obtained
from PDF files of the articles. The script employs difflib's SequenceMatcher to assess the similarity between parsed
texts and expected outcomes, providing a flexible approach to validate the content that may have minor discrepancies
due to parsing inaccuracies.

The script is organized into functions that test different aspects of article parsing:
- normalize_text: Utility function to prepare text for comparison by normalizing its format.
- _parse_test_case_article_reference: Parses test case data for article references from JSON files.
- _parse_test_case_article_metadata: Extracts expected article metadata from JSON test cases.
- _parse_test_case_article_content: Retrieves expected article content, such as abstract and keywords, from JSON files.
- _parse_test_case_article_authors: Extracts expected author details from JSON test cases.
- _are_similar: Compares two text snippets for similarity beyond a certain threshold.
- _are_reference_similar: Specifically compares lists of references for similarity based on titles.

Test cases:
- test_parse_article_reference: Validates the parsing of article references against expected outcomes.
- test_parse_article_metadata: Ensures the article metadata is extracted accurately.
- test_parse_article_content: Checks the parsing of article content, such as abstracts and keywords.
- test_parse_article_authors: Confirms that author details are correctly parsed from articles.

Each test function iterates over JSON files containing expected test case results, compares these against parsed data
obtained from corresponding PDF files, and asserts the accuracy of the parsing process. The tests provide valuable
feedback on the efficacy of the parsing algorithms and help in identifying areas for improvement in the article
analysis system.
"""

import json
from typing import List
from backend.app.services import analysis
from backend.app.services.Parser.types import Metadata, Content, Reference, Author
from pathlib import Path
from difflib import SequenceMatcher


# Test cases for the article metadata
def normalize_text(text):
    """
    Normalize the text by converting it to lowercase and removing extra whitespaces.

    @param text: The text to normalize.
    @return: The normalized text.
    """
    return ' '.join(text.lower().split())


# Parse test case data
def _parse_test_case_article_reference(path: str) -> List[Reference]:
    """
    Parse the test case data for the article reference.

    @param path: The path to the test case data.
    @return: The list of references.
    """
    with open(path, "r") as file:
        data = json.load(file)
        if not data['Reference']:
            return []
        return [
            Reference(
                authors=ref.get('authors', ''),
                title=ref.get('title', ''),
                type=ref.get('type', ''),
                container_title=ref.get('container-title', ''),
                doi=ref.get('doi', ''),
                published_date=ref.get('date', [])[0] if ref.get('data') else ''
            )
            for ref in data['Reference']
        ]


def _parse_test_case_article_metadata(path: str) -> Metadata:
    """
    Parse the test case data for the article metadata.

    @param path: The path to the test case data.
    @return: The article metadata.
    """
    with open(path, "r") as file:
        data = json.load(file)
        return Metadata(
            title=data["title"],
            doi=data["doi"],
            journal=data["journal"],
            published_date=data["publish date"],
            publisher=data["publisher"]
        )


def _parse_test_case_article_content(path: str) -> Content:
    """
    Parse the test case data for the article content.

    @param path: The path to the test case data.
    @return: The article content.
    """
    with open(path, "r") as file:
        data = json.load(file)
        return Content(
            abstract=data["abstract"],
            keywords=data["keywords"]
        )


def _parse_test_case_article_authors(path: str) -> List[Author]:
    """
    Parse the test case data for the article authors.

    @param path: The path to the test case data.
    @return: The list of authors.
    """
    with open(path, "r") as file:
        data = json.load(file)
        return [
            Author(
                name=author.get('name', ''),
                affiliation=author.get('affiliation', ''),
                email=author.get('email', '')
            )
            for author in data['authors']
        ]


def _are_similar(text1, text2, threshold=0.8):
    """
    Check if two texts are similar based on the Levenshtein distance.

    @param text1: The first text to compare.
    @param text2: The second text to compare.
    @param threshold: The similarity threshold.
    @return: True if the texts are similar, False otherwise.
    """
    text1 = normalize_text(text1)
    text2 = normalize_text(text2)
    similarity = SequenceMatcher(None, text1, text2).ratio()
    return similarity >= threshold


def _are_reference_similar(reference1: List[Reference], reference2: List[Reference], match_threshold=0.8,
                           match_ratio_threshold=0.7):
    """
    Check if two lists of references are similar based on their titles.
    A reference is considered similar to another if their titles have more than 80% similarity.
    References in one list are matched to the most similar
    references in the other list without assuming identical order.

    @param reference1: The first list of references.
    @param reference2: The second list of references.
    @param match_threshold: The similarity threshold for matching references.
    @param match_ratio_threshold: The ratio of matched references to the total number of references.
    @return: True if the references are similar, False otherwise.
    """
    if len(reference1) == 0 and len(reference2) == 0:
        return True
    match_count = 0

    for ref1 in reference1:
        for ref2 in reference2:
            # Compute similarity based on titles, but other fields like authors and DOI can also be considered
            title_similarity = SequenceMatcher(None, normalize_text(ref1.title), normalize_text(ref2.title)).ratio()
            if title_similarity > match_threshold:
                match_count += 1
                break  # Stop searching once a match is found for this reference

    # Check if the ratio of matched references in reference1 is above the threshold

    match_ratio = match_count / len(reference1)
    print("match ratio:", match_ratio)
    return match_ratio >= match_ratio_threshold


# Test cases for the article reference
def test_parse_article_reference():
    """
    Test the parsing of the article reference.

    @return: None
    """
    json_dir = Path(Path.cwd() / "app/services/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        print("testing reference:", json_file.name)
        test_case = _parse_test_case_article_reference(str(json_file))
        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path(Path.cwd() / "app/services/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_article_object(xml_path)
        # print("reference test case")
        # print(test_case)
        # print(article.references)
        assert _are_reference_similar(test_case, article.references), f"Reference mismatch for {json_file.name}"


# Test cases for the article metadata
def test_parse_article_metadata():
    """
    Test the parsing of the article metadata.

    @return: None
    """
    json_dir = Path(Path.cwd() / "app/services/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        test_case = _parse_test_case_article_metadata(str(json_file))

        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path(Path.cwd() / "app/services/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_article_object(xml_path)
        # print(test_case.journal)
        # print(article.metadata.journal)
        assert test_case == article.metadata, f"Metadata mismatch for {json_file.name}"


# Test cases for the article content
def test_parse_article_content():
    """
    Test the parsing of the article content.

    @return: None
    """
    json_dir = Path(Path.cwd() / "app/services/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        test_case = _parse_test_case_article_content(str(json_file))

        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path(Path.cwd() / "app/services/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_article_object(xml_path)
        # print("Test Case:\n")
        # print(test_case)
        # print("Article:\n")
        # print(article.content)
        assert _are_similar(normalize_text(test_case.abstract),
                            normalize_text(article.content.abstract)), f"Abstract mismatch for {json_file.name}"


# Test cases for the article authors
def test_parse_article_authors():
    """
    Test the parsing of the article authors.

    @return: None
    """
    json_dir = Path(Path.cwd() / "app/services/test_data/JSON")
    for json_file in json_dir.glob("*.json"):
        test_case = _parse_test_case_article_authors(str(json_file))

        # Construct corresponding PDF file path from the JSON file name
        pdf_file_name = json_file.stem + ".pdf"
        pdf_path = Path(Path.cwd() / "app/services/test_data/Papers") / pdf_file_name

        # Parse the article metadata
        xml_path = analysis.get_extracted_xml(str(pdf_path))
        article = analysis.get_article_object(xml_path)
        # print(test_case)
        # print(article.authors)
        for i, author in enumerate(article.authors):
            assert test_case[i].name == author.name, f"Author mismatch for {json_file.name}"
