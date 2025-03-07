"""
Overview:
This module defines a comprehensive set of CRUD (Create, Read, Update, Delete) operations for various models in a
FastAPI application that interfaces with a MongoDB database through MongoEngine ODM. Utilizing the power of generic
programming, it introduces a base class 'CRUDOperations' that abstracts common CRUD functionalities, which can be
extended or customized for specific models such as Articles, Topics, Authors, Institutions, and Departments. The
module is structured to separate concerns effectively, using type variables to enforce type safety and consistency
across model, value object (VO), and filter classes.

Each specific CRUD class inherits from 'CRUDOperations' and may implement additional methods tailored to the model's
needs, such as 'search_by_filter' which performs query operations based on various filter criteria. This design
pattern promotes code reuse and maintainability, allowing for easy extension as new models or requirements emerge.

Key Components:
- MongoEngine ODM: Provides the database models and query capabilities.
- Pydantic Models (VO): Serve as data transfer objects, ensuring strict type checking and validation.
- Generic Programming: Leverages Python's typing system to create flexible and reusable components.

Functionality: - Base CRUD Operations: Includes methods for creating, reading, updating, and deleting documents in
MongoDB. - Model-Specific Extensions: Allows for the implementation of additional methods specific to the domain
logic of each model. - Search by Filter: A common method in many specific CRUD classes to perform advanced querying
based on a set of filter criteria.

Usage: The CRUD classes can be instantiated with the respective MongoEngine model, Pydantic VO model, and filter
model to begin performing database operations. This modular approach facilitates the development of a clean,
maintainable codebase for web applications that require robust data management capabilities. """

from mongoengine import Q, DoesNotExist
from typing import List, TypeVar, Generic

# Assuming these imports are correctly resolving your actual project structure
from ..db.mongoengine_models import (
    Article, Topic, Author, Institution, Department, AuthorInstitution, AuthorDepartment,
    ArticleAuthor, ArticleCitation, TopicRelationship, ArticleTopic
)
from ..services.models import (
    ArticleVO, TopicVO, AuthorVO, InstitutionVO, DepartmentVO, AuthorInstitutionVO, AuthorDepartmentVO,
    ArticleAuthorVO, ArticleCitationVO, TopicRelationshipVO, ArticleTopicVO, ArticleFilter, TopicFilter,
    AuthorFilter, InstitutionFilter, DepartmentFilter, AuthorInstitutionFilter, AuthorDepartmentFilter,
    ArticleAuthorFilter, ArticleCitationFilter, TopicRelationshipFilter, ArticleTopicFilter
)

# Define type variables for use with generic classes/functions
TModel = TypeVar('TModel')  # MongoEngine model
TVO = TypeVar('TVO')  # VO model
TFilter = TypeVar('TFilter')  # Filter model


class CRUDOperations(Generic[TModel, TVO, TFilter]):
    def __init__(self, mongo_model: TModel, vo_model: TVO):
        self.mongo_model = mongo_model
        self.vo_model = vo_model

    def create(self, obj: TVO) -> TVO:
        # Create a MongoEngine document from the Pydantic model
        mongo_obj = self.mongo_model(**obj.dict()).save()
        # Return a Pydantic model created from the MongoEngine document
        return self.vo_model.from_orm(mongo_obj)

    def create_many(self, objs: List[TVO]) -> List[TVO]:
        inserted_objs = []
        for obj in objs:
            try:
                mongo_obj = self.mongo_model(**obj.dict())
                mongo_obj.save()  # Save each document individually
                inserted_objs.append(self.vo_model.from_orm(mongo_obj))
            except Exception as e:  # Consider catching more specific exceptions
                print(f"Error inserting document: {e}")
        return inserted_objs

    def get_by_filter(self, filter_obj: TFilter) -> List[TVO] | None:
        try:
            mongo_objs = self.mongo_model.objects(**filter_obj.dict(exclude_none=True))
            return [self.vo_model.from_orm(obj) for obj in mongo_objs]
        except DoesNotExist:
            return None

    def update_by_filter(self, filter_obj: TFilter, update_obj: TVO) -> List[TVO] | None:
        try:
            matched_objects = self.mongo_model.objects(**filter_obj.dict(exclude_none=True))

            updated_objects = []
            for obj in matched_objects:
                obj.clean()
                for key, value in update_obj.dict(exclude_none=True).items():
                    setattr(obj, key, value)
                obj.save()
                updated_objects.append(self.vo_model.from_orm(obj))

            return updated_objects
        except DoesNotExist:
            return None

    def delete_by_filter(self, filter_obj: TFilter) -> bool:
        result = self.mongo_model.objects(**filter_obj.dict(exclude_none=True)).delete()
        return result > 0


# Specific CRUD operation classes for each model
class ArticleCRUD(CRUDOperations[Article, ArticleVO, ArticleFilter]):
    def __init__(self):
        super().__init__(Article, ArticleVO)

    def search_by_filter(self, filter_obj: TFilter) -> List[TVO]:
        query = Q()
        for field, value in filter_obj.dict(exclude_none=True).items():
            query |= Q(**{f"{field}__icontains": value})
        mongo_objs = self.mongo_model.objects.filter(query)
        return [self.vo_model.from_orm(obj) for obj in mongo_objs]


class TopicCRUD(CRUDOperations[Topic, TopicVO, TopicFilter]):
    def __init__(self):
        super().__init__(Topic, TopicVO)

    def search_by_filter(self, filter_obj: TFilter) -> List[TVO]:
        query = Q()
        for field, value in filter_obj.dict(exclude_none=True).items():
            query |= Q(**{f"{field}__icontains": value})
        mongo_objs = self.mongo_model.objects.filter(query)
        return [self.vo_model.from_orm(obj) for obj in mongo_objs]


class AuthorCRUD(CRUDOperations[Author, AuthorVO, AuthorFilter]):
    def __init__(self):
        super().__init__(Author, AuthorVO)

    def search_by_filter(self, filter_obj: TFilter) -> List[TVO]:
        query = Q()
        for field, value in filter_obj.dict(exclude_none=True).items():
            query |= Q(**{f"{field}__icontains": value})
        mongo_objs = self.mongo_model.objects.filter(query)
        return [self.vo_model.from_orm(obj) for obj in mongo_objs]


class InstitutionCRUD(CRUDOperations[Institution, InstitutionVO, InstitutionFilter]):
    def __init__(self):
        super().__init__(Institution, InstitutionVO)

    def search_by_filter(self, filter_obj: TFilter) -> List[TVO]:
        query = Q()
        for field, value in filter_obj.dict(exclude_none=True).items():
            query |= Q(**{f"{field}__icontains": value})
        mongo_objs = self.mongo_model.objects.filter(query)
        return [self.vo_model.from_orm(obj) for obj in mongo_objs]


class DepartmentCRUD(CRUDOperations[Department, DepartmentVO, DepartmentFilter]):
    def __init__(self):
        super().__init__(Department, DepartmentVO)

    def search_by_filter(self, filter_obj: TFilter) -> List[TVO]:
        query = Q()
        for field, value in filter_obj.dict(exclude_none=True).items():
            query |= Q(**{f"{field}__icontains": value})
        mongo_objs = self.mongo_model.objects.filter(query)
        return [self.vo_model.from_orm(obj) for obj in mongo_objs]


class AuthorInstitutionCRUD(CRUDOperations[AuthorInstitution, AuthorInstitutionVO, AuthorInstitutionFilter]):
    def __init__(self):
        super().__init__(AuthorInstitution, AuthorInstitutionVO)


class AuthorDepartmentCRUD(CRUDOperations[AuthorDepartment, AuthorDepartmentVO, AuthorDepartmentFilter]):
    def __init__(self):
        super().__init__(AuthorDepartment, AuthorDepartmentVO)


class ArticleAuthorCRUD(CRUDOperations[ArticleAuthor, ArticleAuthorVO, ArticleAuthorFilter]):
    def __init__(self):
        super().__init__(ArticleAuthor, ArticleAuthorVO)


class ArticleCitationCRUD(CRUDOperations[ArticleCitation, ArticleCitationVO, ArticleCitationFilter]):
    def __init__(self):
        super().__init__(ArticleCitation, ArticleCitationVO)


class TopicRelationshipCRUD(CRUDOperations[TopicRelationship, TopicRelationshipVO, TopicRelationshipFilter]):
    def __init__(self):
        super().__init__(TopicRelationship, TopicRelationshipVO)


class ArticleTopicCRUD(CRUDOperations[ArticleTopic, ArticleTopicVO, ArticleTopicFilter]):
    def __init__(self):
        super().__init__(ArticleTopic, ArticleTopicVO)
