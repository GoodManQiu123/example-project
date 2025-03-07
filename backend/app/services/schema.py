"""
Overview:
This script defines a collection of Pydantic models representing the data structures for an academic paper analysis
or management system. These models serve as schemas for various entities such as authors, topics, papers, and the
connections between them, facilitating data validation, serialization, and documentation within the system.

The models are categorized as follows:
- Response Schemas: Base structures for standardizing API response formats, including status codes, messages,
and data payloads.
- Entity Schemas: Definitions for individual entities like authors, topics, and papers, detailing their attributes
and relationships.
- Connection Schemas: Representations of relationships between entities, such as co-authorships, topic associations,
and citation networks.

Each schema employs Pydantic's features for data validation and transformation, including custom field definitions,
optional fields, and aliasing for serialization. The aliasing, in particular, utilizes a function to convert field
names to camelCase, aligning with common JSON naming conventions.

Usage:
The defined schemas can be used across the system for various purposes, including:
- Forming the structure of HTTP responses in API endpoints.
- Validating incoming data payloads to ensure they meet the expected formats.
- Structuring data retrieved from the database before it is sent to clients.

This approach ensures consistency in data handling, improves code maintainability, and aids in generating clear
API documentation. By leveraging Pydantic models, developers can easily define and manage complex data structures.
"""

from typing import Any, Optional
from pydantic import BaseModel, Field


def to_camel(string: str) -> str:
    """
    Convert a string to camel case.

    @param string: str: The input string.
    @return: str: The string in camel case.
    """
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


class ResponseSchema(BaseModel):
    """
    The base response schema for all API responses.
    """
    code: int = Field(200, title="HTTP status code", description="The HTTP status code of the response.")
    # By default, the response is successful (But in practice, it should be "error" if failed)
    msg: str = Field("success", title="Message", description="The message of the response.")
    data: list | dict | Any = Field(None, title="Data", description="The data of the response.")


class AuthorSchema(BaseModel):
    """
    The schema for author information.
    """
    author_id: int = Field(None, title="Author ID", description="The unique identifier of the author.")
    name: str = Field(None, title="Author Name", description="The name of the author.")
    email: str = Field(None, title="Author Email", description="The email of the author.")
    affiliation: Optional[str] = Field(None, title="Author Affiliation", description="The affiliation of the author.")

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class TopicSchema(BaseModel):
    """
    The schema for topic information.
    """
    topic_id: int = Field(None, title="Topic ID", description="The unique identifier of the topic.")
    name: str = Field(None, title="Topic Name", description="The name of the topic.")

    # original: Optional[bool] = False

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class PaperItemSchema(BaseModel):
    """
    The schema for paper information.
    """
    article_id: int = Field(None, title="Paper ID", description="The unique identifier of the paper.")
    title: str = Field(None, title="Paper Title", description="The title of the paper.")
    authors: list[AuthorSchema] = Field([], title="Paper Authors", description="The authors of the paper.")

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class PaperResponse(ResponseSchema):
    """
    The response schema for paper information.
    """
    data: list[PaperItemSchema] = Field([], title="Paper List", description="The list of papers.")


class TopicItemSchema(BaseModel):
    """
    The schema for topic information.
    """
    topic_id: int = Field(None, title="Topic ID", description="The unique identifier of the topic.")
    topic: str = Field(None, title="Topic Name", description="The name of the topic.")
    count: int = Field(None, title="Paper Count", description="The number of papers in the topic.")

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class TopicResponse(ResponseSchema):
    """
    The response schema for topic information.
    """
    data: list[TopicItemSchema] = Field([], title="Topic List", description="The list of topics.")


class AuthorItemSchema(BaseModel):
    """
    The schema for author information.
    """
    author_id: int = Field(None, title="Author ID", description="The unique identifier of the author.")
    name: str = Field(None, title="Author Name", description="The name of the author.")
    count: int = Field(None, title="Paper Count", description="The number of papers by the author.")

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class AuthorResponse(ResponseSchema):
    """
    The response schema for author information.
    """
    data: list[AuthorItemSchema] = Field([], title="Author List", description="The list of authors.")


class SameTopicConnectionItemSchema(BaseModel):
    """
    The schema for same-topic connection information.
    """
    topic: int = Field(None, title="Topic ID", description="The unique identifier of the topic.")
    papers: list[int] = Field([], title="Paper List", description="The list of papers in the topic.")


class SameTopicDataSchema(BaseModel):
    """
    The schema for same-topic data information.
    """
    connections: list[SameTopicConnectionItemSchema] = Field([],
                                                             title="Connection List",
                                                             description="The list of connections.")
    topics: list[TopicSchema] = Field([], title="Topic List", description="The list of topics.")
    papers: list[PaperItemSchema] = Field([], title="Paper List", description="The list of papers.")


class SameTopicResponseSchema(ResponseSchema):
    """
    The response schema for same-topic information.
    """
    data: SameTopicDataSchema = Field({}, title="Data", description="The data of the response.")


class CoAuthorConnectionItemSchema(BaseModel):
    """
    The schema for co-author connection information.
    """
    author: int = Field(None, title="Author ID", description="The unique identifier of the author.")
    papers: list[int] = Field([], title="Paper List", description="The list of papers by the author.")


class CoAuthorDataSchema(BaseModel):
    """
    The schema for co-author data information.
    """
    connections: list[CoAuthorConnectionItemSchema] = Field([],
                                                            title="Connection List",
                                                            description="The list of connections.")
    authors: list[AuthorSchema] = Field([], title="Author List", description="The list of authors.")
    papers: list[PaperItemSchema] = Field([], title="Paper List", description="The list of papers.")


class CoAuthorResponseSchema(ResponseSchema):
    """
    The response schema for co-author information.
    """
    data: CoAuthorDataSchema = Field({}, title="Data", description="The data of the response.")


class CitedConnectionItemSchema(BaseModel):
    """
    The schema for cited connection information.
    """
    from_paper: int = Field(..., title="From Paper ID", description="The unique identifier of the paper.")
    to_paper: list[int] = Field([], title="To Paper List", description="The list of papers cited by the from paper.")

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class CitedTreeDataSchema(BaseModel):
    """
    The schema for cited tree data information.
    """
    connections: list[CitedConnectionItemSchema] = Field([],
                                                         title="Connection List",
                                                         description="The list of connections.")
    papers: list[PaperItemSchema] = Field([], title="Paper List", description="The list of papers.")


class CitedTreeResponseSchema(ResponseSchema):
    """
    The response schema for cited tree information.
    """
    data: CitedTreeDataSchema = Field({}, title="Data", description="The data of the response.")
