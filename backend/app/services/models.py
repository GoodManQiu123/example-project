"""
Overview:
This script defines a comprehensive suite of Pydantic models and dataclasses to represent various entities in an
academic paper management or analysis system. The entities covered include articles, authors, topics, institutions,
departments, and various relationships such as article-author and article-topic associations.

Key Components:
- Value Object (VO) Models: Pydantic models for articles, authors, topics, etc., ensuring data validation and
  serialization for API responses and internal processing.
- Filters: Specialized VO models intended for filtering database queries, with optional fields allowing for flexible
  query construction.
- Relationships: Models defining associations between different entities, such as authors and institutions or articles
  and topics, to represent complex relationships within the domain.
- Dataclasses: Used for parsing and processing metadata, content, and references from articles, providing a simple yet
  effective way to handle structured data without the need for extensive validation.

Features:
- Validators: Custom validators in Pydantic models to handle complex fields such as dates and DOIs, ensuring they meet
  specific formats and standards.
- Configurations: Configuration options in models to enable ORM compatibility, allowing direct interaction with ORM
  objects and facilitating integration with databases.
- Alias Generators: Utilized in models to transform snake_case field names into camelCase for JSON serialization,
  adhering to common JSON naming conventions.

Usage:
These models and dataclasses are integral to various system operations, including API data exchange, database
interactions, data parsing from documents, and more. They provide a structured and validated approach to handling
data, ensuring consistency and reliability throughout the system's components.
"""


import re
import warnings
from dataclasses import dataclass
from datetime import datetime, date
from pydantic import BaseModel, Field, validator
from typing import Optional, List, AnyStr


# Pydantic model for the Sequence
class SequenceVO(BaseModel):
    """
    The schema for sequence information.
    """
    name: str
    value: int


# Pydantic model for the Article
class ArticleVO(BaseModel):
    """
    Article Value Object (VO) class for the Article model.
    """
    article_id: Optional[int] = Field(None,
                                      tile="Article ID",
                                      description="The unique identifier of the article.")
    title: str = Field(...,
                       title="Title",
                       description="The title of the article.")
    abstract: Optional[str] = Field(None,
                                    title="Abstract",
                                    description="The abstract of the article.")
    publisher: Optional[str] = Field(None,
                                     title="Publisher",
                                     description="The publisher of the article.")
    date: Optional[str] = Field(None,
                                title="Publication Date",
                                description="The publication date of the article.")
    issn: Optional[str] = Field(None,
                                title="ISSN",
                                description="The International Standard Serial Number of the article.")
    eissn: Optional[str] = Field(None,
                                 title="EISSN",
                                 description="The Electronic International Standard Serial Number of the article.")
    volume: Optional[str] = Field(None,
                                  title="Volume",
                                  description="The volume of the article.")
    issue: Optional[str] = Field(None,
                                 title="Issue",
                                 description="The issue of the article.")
    page: Optional[str] = Field(None,
                                title="Page",
                                description="The page number of the article.")
    doi: Optional[str] = Field(None,
                               title="DOI",
                               description="The Digital Object Identifier of the article.")
    meeting: Optional[str] = Field(None,
                                   title="Meeting",
                                   description="The meeting where the article was presented.")
    file_path: Optional[str] = Field(None,
                                     title="File Path",
                                     description="The file path of the article.")
    type: Optional[str] = Field(None,
                                title="Type",
                                description="The type of the article.")
    container_title: Optional[str] = Field(None,
                                           title="Container Title",
                                           description="The title of the container holding the article.")

    @validator('date', pre=True, allow_reuse=True)
    def validate_date(cls, v):
        """
        Validate the date field to ensure it is in a standard format.

        @param v: str: The date string to validate.
        @return: str: The validated date string in 'YYYY-MM-DD' format.
        """
        # If the date is None, or the input is None, simply return None
        if v is None or v == '':
            return None

        if isinstance(v, (datetime, date)):
            # If the input is a datetime or date object, convert it to a string in 'YYYY-MM-DD' format.
            return v.strftime('%Y-%m-%d')

        # Define a comprehensive list of date formats to try
        date_formats = [
            '%Y-%m-%d',  # ISO 8601 format
            '%d-%m-%Y',  # Common UK/EU format
            '%m-%d-%Y',  # Common US format
            '%Y/%m/%d',  # ISO 8601 alternative format
            '%d/%m/%Y',  # Common UK/EU alternative format
            '%m/%d/%Y',  # Common US alternative format
            '%Y-%m',  # Four-digit year and month
            '%m-%Y',  # Month and four-digit year
            '%Y/%m',  # Four-digit year and month (alternative)
            '%m/%Y',  # Month and four-digit year (alternative)
            '%Y',  # Four-digit year
            '%y',  # Two-digit year
            '%b %d %Y',  # Abbreviated month name, e.g., Jan 02 2021
            '%B %d %Y',  # Full month name, e.g., January 02 2021
            '%d %b %Y',  # Day first, abbreviated month name
            '%d %B %Y',  # Day first, full month name
            '%b %d, %Y',  # Abbreviated month name with comma, e.g., Jan 02, 2021
            '%B %d, %Y',  # Full month name with comma, e.g., January 02, 2021
            '%d-%b-%Y',  # Day first, abbreviated month name with dashes
            '%d-%B-%Y',  # Day first, full month name with dashes
            '%d %b, %Y',  # Day first, abbreviated month name with comma
            '%d %B, %Y',  # Day first, full month name with comma
            '%Y %b %d',  # Year first, abbreviated month name
            '%Y %B %d',  # Year first, full month name
            '%b %Y',  # Abbreviated month name and year
            '%B %Y',  # Full month name and year
            '%d-%b',  # Day and abbreviated month
            '%d-%B',  # Day and full month
            '%b-%d',  # Abbreviated month and day
            '%B-%d',  # Full month and day
            '%Y-%b-%d',  # Year, abbreviated month, and day
            '%Y-%B-%d',  # Year, full month, and day
            '%d-%b-%Y',  # Day, abbreviated month, and year
            '%d-%B-%Y',  # Day, full month, and year
        ]

        # Try to parse the date string using each format
        for date_format in date_formats:
            try:
                # Attempt to parse the date string
                parsed_date = datetime.strptime(v, date_format)

                # If successful, return the date string in 'YYYY-MM-DD' format
                return parsed_date.strftime('%Y-%m-%d')
            except ValueError:
                # If parsing fails, continue to try the next format
                continue

        # If none of the formats match, set date to None and issue a warning
        warnings.warn(f"Date '{v}' does not match any of the recognized formats. Setting 'date' to None.")
        return None

    @validator('doi', pre=True, allow_reuse=True)
    def validate_doi(cls, v):
        """
        Validate the DOI field to ensure it meets the standard DOI format.

        @param v: str: The DOI string to validate.
        @return: str: The validated DOI string or None if it doesn't match the standard format.
        """
        if v is None or v == '':
            return None

        # Regular expression for validating a DOI
        doi_regex = re.compile(r'^10.\d{4,9}/[-._;()/:A-Za-z0-9]+$')

        if not doi_regex.match(v):
            # If the DOI doesn't match the regex, issue a warning and return None
            warnings.warn(f"DOI '{v}' does not match the standard DOI format. Setting 'doi' to None.")
            return None

        return v

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleFilter(ArticleVO):
    """
    Article Filter class for the Article model.
    """
    article_id: Optional[int] = Field(None,
                                      title="Article ID",
                                      description="The unique identifier of the article.")
    title: Optional[str] = Field(None,
                                 title="Title",
                                 description="The title of the article.")
    file_path: Optional[str] = Field(None,
                                     title="File Path",
                                     description="The file path of the article.")


# Pydantic model for the Topic
class TopicVO(BaseModel):
    """
    Topic Value Object (VO) class for the Topic model.
    """
    topic_id: Optional[int] = Field(None,
                                    title="Topic ID",
                                    description="The unique identifier of the topic.")
    name: str = Field(...,
                      title="Name",
                      description="The name of the topic.")

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class TopicFilter(TopicVO):
    """
    Topic Filter class for the Topic model.
    """
    topic_id: Optional[int] = Field(None,
                                    title="Topic ID",
                                    description="The unique identifier of the topic.")
    name: Optional[str] = Field(None,
                                title="Name",
                                description="The name of the topic.")


# Pydantic model for the Author
class AuthorVO(BaseModel):
    """
    Author Value Object (VO) class for the Author model.
    """
    author_id: Optional[int] = Field(None,
                                     title="Author ID",
                                     description="The unique identifier of the author.")
    name: str = Field(...,
                      title="Name",
                      description="The name of the author.")
    email: Optional[str] = Field(None,
                                 title="Email",
                                 description="The email address of the author.")
    affiliation: Optional[str] = Field(None,
                                       title="Affiliation",
                                       description="The affiliation of the author.")

    @validator('email', pre=True, allow_reuse=True)
    def validate_email(cls, v):
        """
        Validate the email field to ensure it is in a standard email format.

        @param v: str: The email string to validate.
        @return: str: The validated email string or None if it doesn't match the standard format.
        """
        if v is None or v == '':
            return None

        # Regular expression for validating an Email
        email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        # If the email is not empty or None, try matching against the regex
        if not email_regex.match(v):
            # If the email doesn't match the regex, issue a warning and return None
            warnings.warn(f"Provided email '{v}' is not a valid email format. Setting 'email' to None.")
            return None

        # If the email matches the regex, return it as is
        return v

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class AuthorFilter(AuthorVO):
    """
    Author Filter class for the Author model.
    """
    author_id: Optional[int] = Field(None,
                                     title="Author ID",
                                     description="The unique identifier of the author.")
    name: Optional[str] = Field(None,
                                title="Name",
                                description="The name of the author.")


class InstitutionVO(BaseModel):
    """
    Institution Value Object (VO) class for the Institution model.
    """
    institution_id: Optional[int] = Field(None,
                                          title="Institution ID",
                                          description="The unique identifier of the institution.")
    name: str = Field(...,
                      title="Name",
                      description="The name of the institution.")

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class InstitutionFilter(InstitutionVO):
    """
    Institution Filter class for the Institution model.
    """
    institution_id: Optional[int] = Field(None,
                                          title="Institution ID",
                                          description="The unique identifier of the institution.")
    name: Optional[str] = Field(None,
                                title="Name",
                                description="The name of the institution.")


class DepartmentVO(BaseModel):
    """
    Department Value Object (VO) class for the Department model.
    """
    department_id: Optional[int] = Field(None,
                                         title="Department ID",
                                         description="The unique identifier of the department.")
    name: str = Field(...,
                      title="Name",
                      description="The name of the department.")
    institution_id: Optional[int] = Field(None,
                                          title="Institution ID",
                                          description="The unique identifier of the institution.")

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class DepartmentFilter(DepartmentVO):
    """
    Department Filter class for the Department model.
    """
    department_id: Optional[int] = Field(None,
                                         title="Department ID",
                                         description="The unique identifier of the department.")
    name: Optional[str] = Field(None,
                                title="Name",
                                description="The name of the department.")


# Pydantic model for Author-Institution relationship
class AuthorInstitutionVO(BaseModel):
    """
    Author-Institution Value Object (VO) class for the Author-Institution relationship model.
    """
    author_id: int = Field(...,
                           title="Author ID",
                           description="The unique identifier of the author.")
    institution_id: int = Field(...,
                                title="Institution ID",
                                description="The unique identifier of the institution.")

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class AuthorInstitutionFilter(AuthorInstitutionVO):
    """
    Author-Institution Filter class for the Author-Institution relationship model.
    """
    author_id: Optional[int] = Field(None,
                                     title="Author ID",
                                     description="The unique identifier of the author.")
    institution_id: Optional[int] = Field(None,
                                          title="Institution ID",
                                          description="The unique identifier of the institution.")


class AuthorDepartmentVO(BaseModel):
    """
    Author-Department Value Object (VO) class for the Author-Department relationship model.
    """
    author_id: int = Field(...,
                           title="Author ID",
                           description="The unique identifier of the author.")
    department_id: int = Field(...,
                               title="Department ID",
                               description="The unique identifier of the department.")

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class AuthorDepartmentFilter(AuthorDepartmentVO):
    """
    Author-Department Filter class for the Author-Department relationship model.
    """
    author_id: Optional[int] = Field(None,
                                     title="Author ID",
                                     description="The unique identifier of the author.")
    department_id: Optional[int] = Field(None,
                                         title="Department ID",
                                         description="The unique identifier of the department.")


# Pydantic model for Article-Author relationship
class ArticleAuthorVO(BaseModel):
    """
    Article-Author Value Object (VO) class for the Article-Author relationship model.
    """
    article_id: int = Field(...,
                            title="Article ID",
                            description="The unique identifier of the article.")
    author_id: int = Field(...,
                           title="Author ID",
                           description="The unique identifier of the author.")

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleAuthorFilter(ArticleAuthorVO):
    """
    Article-Author Filter class for the Article-Author relationship model.
    """
    article_id: Optional[int] = Field(None,
                                      title="Article ID",
                                      description="The unique identifier of the article.")
    author_id: Optional[int] = Field(None,
                                     title="Author ID",
                                     description="The unique identifier of the author.")


# Pydantic model for Article-Author relationship
class ArticleTopicVO(BaseModel):
    """
    Article-Topic Value Object (VO) class for the Article-Topic relationship model.
    """
    article_id: int = Field(...,
                            title="Article ID",
                            description="The unique identifier of the article.")
    topic_id: int = Field(...,
                          title="Topic ID",
                          description="The unique identifier of the topic.")

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleTopicFilter(ArticleTopicVO):
    """
    Article-Topic Filter class for the Article-Topic relationship model.
    """
    article_id: Optional[int] = Field(None,
                                      title="Article ID",
                                      description="The unique identifier of the article.")
    topic_id: Optional[int] = Field(None,
                                    title="Topic ID",
                                    description="The unique identifier of the topic.")


class ArticleCitationVO(BaseModel):
    """
    Article-Citation Value Object (VO) class for the Article-Citation relationship model.
    """
    citing_article_id: int = Field(...,
                                   title="Citing Article ID",
                                   description="The unique identifier of the citing article.")
    cited_article_id: int = Field(...,
                                  title="Cited Article ID",
                                  description="The unique identifier of the cited article.")

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleCitationFilter(ArticleCitationVO):
    """
    Article-Citation Filter class for the Article-Citation relationship model.
    """
    citing_article_id: Optional[int] = Field(None,
                                             title="Citing Article ID",
                                             description="The unique identifier of the citing article.")
    cited_article_id: Optional[int] = Field(None,
                                            title="Cited Article ID",
                                            description="The unique identifier of the cited article.")


class TopicRelationshipVO(BaseModel):
    """
    TopicRelationship Value Object (VO) class for the TopicRelationship model.
    """
    parent_topic_id: int = Field(...,
                                 title="Parent Topic ID",
                                 description="The unique identifier of the parent topic.")
    child_topic_id: int  # Assuming you want to reference the child Topic by its ID

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class TopicRelationshipFilter(TopicRelationshipVO):
    """
    TopicRelationship Filter class for the TopicRelationship model.
    """
    parent_topic_id: Optional[int] = Field(None,
                                           title="Parent Topic ID",
                                           description="The unique identifier of the parent topic.")
    child_topic_id: Optional[int] = Field(None,
                                          title="Child Topic ID",
                                          description="The unique identifier of the child topic.")


@dataclass
class ParseMetadataVO:
    """
    Value Object (VO) class for the metadata of an article.
    """
    title: str  # The title of the article
    doi: str  # Digital Object Identifier for the article
    publisher: str  # The publisher of the article
    journal: str  # The journal where the article is published
    published_date: str  # The publication date of the article


@dataclass
class ParseContentVO:
    """
    Value Object (VO) class for the content of an article.
    """
    abstract: str  # The abstract of the article
    keywords: List[AnyStr]  # A list of keywords associated with the article


@dataclass
class ParseAuthorVO:
    """
    Value Object (VO) class for an author of an article.
    """
    name: str  # The name of the author
    affiliation: str  # The affiliation of the author
    email: Optional[str]  # The email address of the author, which is optional


class ParseReferenceAuthorVO(BaseModel):
    """
    Value Object (VO) class for an author of a reference.
    """
    family: str = ''
    given: str = ''

    @staticmethod
    def from_dict(data: dict):
        """
        Create a ParseReferenceAuthorVO instance from a dictionary.

        @param data: dict: The dictionary containing author data.
        @return: ParseReferenceAuthorVO: The parsed author value object.
        """
        return ParseReferenceAuthorVO(
            family=data.get('family', ''),
            given=data.get('given', '')
        )


@dataclass
class ParseReferenceVO:
    """
    Value Object (VO) class for a reference cited in an article.
    """
    authors: List[ParseReferenceAuthorVO]  # A list of authors of the reference
    title: str  # The title of the reference
    type: str  # The type of the reference (e.g., journal article, book)
    container_title: str  # The title of the container holding the reference (e.g., journal name)
    doi: str  # Digital Object Identifier for the reference
    published_date: str  # The publication date of the reference


@dataclass
class ParseArticleVO:
    """
    Value Object (VO) class for an article parsed from a document.
    """
    metadata: ParseMetadataVO  # The metadata of the article
    content: ParseContentVO  # The content of the article
    authors: List[ParseAuthorVO]  # A list of authors of the article
    references: List[ParseReferenceVO]  # A list of references cited in the article

    @staticmethod
    def from_dict(data: dict):
        """
        Create a ParseArticleVO instance from a dictionary.

        @param data: dict: The dictionary containing article data.
        @return: ParseArticleVO: The parsed article value object.
        """
        return ParseArticleVO(
            metadata=ParseMetadataVO(**data['metadata']),
            content=ParseContentVO(**data['content']),
            authors=[ParseAuthorVO(**author) for author in data['authors']],
            references=[ParseReferenceVO(**reference) for reference in data['references']]
        )
