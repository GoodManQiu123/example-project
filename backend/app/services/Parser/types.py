"""
Overview:
This script defines data classes for representing various components of an academic article, including metadata,
content, authors, and references. Each class is equipped with methods for generating string representations, equality
comparisons, and converting instances into JSON serializable formats or dictionaries. These classes provide a
structured approach to handling complex data associated with academic articles, facilitating easy manipulation,
comparison, serialization, and deserialization of article components.

Classes:
- Metadata: Holds information such as title, DOI, publisher, journal, and publication date.
- Content: Contains the abstract and a list of keywords related to the article.
- Author: Represents an author with their name, affiliation, and optional email.
- Reference: Encapsulates reference details, including authors, title, type, container title, DOI, and publication date.
- ArticleObject: Aggregates all above components, representing a complete article with metadata, content, authors, and
  references.

Features:
- __repr__ methods provide a readable string representation for debugging and logging.
- __eq__ methods enable comparison between instances of the same class, checking for content equality.
- to_json methods convert instances into JSON serializable formats, suitable for API responses or storage.
- to_dict method (in ArticleObject) converts the complete article structure into a nested dictionary.

Usage:
These data classes can be used in various applications such as content management systems for academic publications,
metadata extraction tools, information retrieval systems, and research databases, providing a standardized way to
represent and work with academic article data.
"""

from dataclasses import dataclass, asdict
from typing import Optional
from typing import List

"""
The data models for the Parser service.
"""


@dataclass
class Metadata:
    """
    Data class for metadata information.
    """
    title: str
    doi: str
    publisher: str
    journal: str
    published_date: str

    def __repr__(self):
        """
        String representation of the Metadata object.

        @return: str: The string representation of the Metadata object.
        """
        return f"Title: {self.title}\n" \
               f"DOI: {self.doi}\n" \
               f"Publisher: {self.publisher}\n" \
               f"Journal: {self.journal}\n" \
               f"Published Date: {self.published_date}"

    def __eq__(self, other):
        """
        Check if two Metadata objects are equal.

        @param other: Metadata: The other Metadata object to compare.
        @return: bool: True if the Metadata objects are equal, False otherwise.
        """
        if not isinstance(other, Metadata):
            return False
        return self.title.lower() == other.title.lower() and \
            self.doi == other.doi and \
            self.publisher == other.publisher and \
            self.journal == other.journal and \
            self.published_date == other.published_date

    def to_json(self):
        """
        Convert the Metadata object to a JSON serializable format.

        @return: dict: The JSON serializable representation of the Metadata object.
        """
        return {
            "title": self.title,
            "doi": self.doi,
            "publisher": self.publisher,
            "journal": self.journal,
            "published_date": self.published_date
        }


@dataclass
class Content:
    """
    Data class for content information.
    """
    abstract: str
    keywords: list

    def __repr__(self):
        """
        String representation of the Content object.

        @return: str: The string representation of the Content object.
        """
        return f"Abstract: {self.abstract}\n" \
               f"Keywords: {self.keywords}\n"

    def __eq__(self, other):
        """
        Check if two Content objects are equal.

        @param other: Content: The other Content object to compare.
        @return: bool: True if the Content objects are equal, False otherwise.
        """
        if not isinstance(other, Content):
            return False
        return self.abstract == other.abstract and self.keywords == other.keywords

    def to_json(self):
        """
        Convert the Content object to a JSON serializable format.

        @return: dict: The JSON serializable representation of the Content object.
        """
        return {
            "abstract": self.abstract,
            "keywords": self.keywords
        }


@dataclass
class Author:
    """
    Data class for author information.
    """
    name: str
    affiliation: str
    email: Optional[str]

    def __repr__(self):
        """
        String representation of the Author object.

        @return: str: The string representation of the Author object.
        """
        return (f"Name: {self.name}\n"
                f"Affiliation: {self.affiliation}\n"
                f"Email: {self.email}\n")

    def __eq__(self, other):
        """
        Check if two Author objects are equal.

        @param other: Author: The other Author object to compare.
        @return: bool: True if the Author objects are equal, False otherwise.
        """
        if not isinstance(other, Author):
            return False
        return self.name == other.name and self.affiliation == other.affiliation and self.email == other.email

    def to_json(self):
        """
        Convert the Author object to a JSON serializable format.

        @return: dict: The JSON serializable representation of the Author object.
        """
        return {
            "name": self.name,
            "affiliation": self.affiliation,
            "email": self.email
        }


@dataclass
class Reference:
    """
    Data class for reference information.
    """
    authors: list
    title: str
    type: str
    container_title: str
    doi: str
    published_date: str

    def __repr__(self):
        """
        String representation of the Reference object.

        @return: str: The string representation of the Reference object.
        """
        return (f"Authors: {self.authors}\n"
                f"Title: {self.title}\n"
                f"Type: {self.type}\n"
                f"Container Title: {self.container_title}\n"
                f"DOI: {self.doi}\n"
                f"Published Date: {self.published_date}\n")

    def __eq__(self, other):
        """
        Check if two Reference objects are equal.

        @param other: Reference: The other Reference object to compare.
        @return: bool: True if the Reference objects are equal, False otherwise.
        """
        if not isinstance(other, Reference):
            return False
        return self.title == other.title and \
            self.doi == other.doi and \
            self.authors == other.authors and \
            self.type == other.type and \
            self.container_title == other.container_title and \
            self.published_date == other.published_date


@dataclass
class ArticleObject:
    """
    Data class for the article object.
    """
    metadata: Metadata
    content: Content
    authors: List[Author]
    references: List[Reference]

    def __repr__(self):
        """
        String representation of the ArticleObject.

        @return: str: The string representation of the ArticleObject.
        """
        return (f"Metadata: {self.metadata}\n"
                f"Content: {self.content}\n"
                f"Authors: {self.authors}\n"
                f"References: {self.references}")

    def to_dict(self):
        """
        Convert the ArticleObject to a dictionary.

        @return: dict: The dictionary representation of the ArticleObject.
        """
        return asdict(self)

    def to_json(self, article_id: str = None):
        """
        Convert the ArticleObject to a JSON serializable format.

        @param article_id: str: The ID of the article.
        @return: dict: The JSON serializable representation of the ArticleObject.
        """
        return {
            "articleId": article_id,
            "metadata": self.metadata.to_json(),
            "content": self.content.to_json(),
            "authors": [author.to_json() for author in self.authors],
            "references": len(self.references)
        }
