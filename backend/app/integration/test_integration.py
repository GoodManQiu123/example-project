"""
Overview:
This pytest file is designed to comprehensively test CRUD (Create, Read, Update, Delete) operations for various models
in a document processing and management system. The tests cover a range of models including Article, Topic, Institution,
Author, Department, AuthorInstitution, AuthorDepartment, ArticleAuthor, ArticleCitation, TopicRelationship, and
ArticleTopic. Each model is associated with a specific aspect of document management, such as article metadata,
author details, institutional affiliations, and relationships between articles and topics.

Features:
- Fixtures for initializing CRUD objects for each model, facilitating the creation, modification, and deletion of
  database entries in an isolated test environment.
- Test functions for each model's CRUD operations, ensuring the integrity and functionality of database interactions.
- Use of `pytest_asyncio` for testing asynchronous database operations, reflecting real-world application scenarios.
- Implementation of test cases for both positive scenarios (successful CRUD operations) and negative scenarios
  (handling of invalid data and operation failures).

Usage:
The tests in this file can be run using the pytest framework to validate the correctness and robustness of CRUD
operations within the system's backend. These tests are essential for ensuring data integrity, consistency, and
reliability of the system's database interactions, making them crucial during development, continuous integration,
and deployment phases.

This file contributes to the overall quality assurance strategy of the system, allowing developers and testers to
identify issues early in the development lifecycle, and ensuring that new features or changes do not break existing
functionality.
"""

import pytest
import pytest_asyncio
from .catalog_access import ArticleCRUD, TopicCRUD, InstitutionCRUD, AuthorCRUD, \
    DepartmentCRUD, AuthorInstitutionCRUD, AuthorDepartmentCRUD, ArticleAuthorCRUD, ArticleCitationCRUD, \
    TopicRelationshipCRUD, ArticleTopicCRUD
from ..services.models import ArticleVO, ArticleFilter, TopicVO, TopicFilter, AuthorFilter, AuthorVO, \
    InstitutionVO, InstitutionFilter, DepartmentVO, DepartmentFilter, AuthorInstitutionVO, AuthorInstitutionFilter, \
    AuthorDepartmentVO, AuthorDepartmentFilter, ArticleAuthorFilter, ArticleAuthorVO, ArticleCitationVO, \
    ArticleCitationFilter, TopicRelationshipVO, TopicRelationshipFilter, ArticleTopicVO, ArticleTopicFilter


@pytest_asyncio.fixture
def article_crud() -> ArticleCRUD:
    """
    Create a CRUD object for the Article model.

    @return: ArticleCRUD: The CRUD object for the Article model.
    """
    return ArticleCRUD()


# Combined test function for all CRUD operations of Article
@pytest.mark.asyncio
async def test_article_crud_operations(article_crud) -> None:
    """
    Test the CRUD operations for the Article model.

    @param article_crud: ArticleCRUD: The CRUD object for the Article model.
    @return: None
    """
    # Create an article
    article_vo_create = ArticleVO(
        title="Test Article",
        abstract="This is a test article",
        publisher="Test Publisher",
        date="2024-01-01",
        issn="1234-5678",
        eissn="8765-4321",
        volume="1",
        issue="1",
        page="1-10",
        doi="10.1000/xyz123",
        meeting="Test Conference",
        file_path="/path/to/article.pdf",
        type="Journal Article",
        container_title="Test Journal"
    )
    created_article = article_crud.create(article_vo_create)
    assert created_article.title == "Test Article"
    assert created_article.abstract == "This is a test article"

    # Search by filter (using the title)
    filter_obj = ArticleFilter(article_id=created_article.article_id)
    search_results = article_crud.search_by_filter(filter_obj)
    assert len(search_results) == 1

    # Get by filter to verify creation
    filter_obj = ArticleFilter(**created_article.dict())
    verify_create_results = article_crud.get_by_filter(filter_obj)
    assert verify_create_results is not None

    # Update article by filter (change abstract)
    update_filter_obj = ArticleFilter(article_id=created_article.article_id)
    article_vo_update = ArticleVO(
        title="Updated Test Article",  # Ensure this is a string
        abstract="This is an updated test article",
        publisher="Updated Test Publisher",
        date="2025-01-01",
        issn="1234-5678",
        eissn="8765-4321",
        volume="2",
        issue="1",
        page="11-20",
        doi="10.1000/xyz123",
        meeting="Updated Test Conference",
        file_path="/path/to/updated_article.pdf",  # Ensure this field is included
        type="Journal Article",
        container_title="Test Journal"
    )
    update_results = article_crud.update_by_filter(update_filter_obj, article_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].abstract == "This is an updated test article"

    # Delete article by filter
    delete_filter_obj = ArticleFilter(article_id=created_article.article_id)
    delete_success = article_crud.delete_by_filter(delete_filter_obj)
    assert delete_success

    # Verify deletion
    verify_delete_results = article_crud.get_by_filter(delete_filter_obj)
    assert verify_delete_results is None or len(verify_delete_results) == 0


@pytest_asyncio.fixture
def topic_crud() -> TopicCRUD:
    """
    Create a CRUD object for the Topic model.

    @return: TopicCRUD: The CRUD object for the Topic model.
    """

    return TopicCRUD()


@pytest.mark.asyncio
async def test_topic_crud_operations(topic_crud) -> None:
    """
    Test the CRUD operations for the Topic model.

    @param topic_crud: TopicCRUD: The CRUD object for the Topic model.
    @return: None
    """
    # Create a topic
    topic_vo_create = TopicVO(name="Test Topic", description="This is a test topic")
    created_topic = topic_crud.create(topic_vo_create)
    assert created_topic.name == "Test Topic"

    # Search by filter (using the name)
    filter_obj = TopicFilter(topic_id=created_topic.topic_id)
    search_results = topic_crud.search_by_filter(filter_obj)
    assert len(search_results) == 1
    assert search_results[0].name == "Test Topic"

    # Get by filter to verify creation
    filter_obj = TopicFilter(**created_topic.dict())
    verify_create_results = topic_crud.get_by_filter(filter_obj)
    assert verify_create_results is not None

    # Update topic by filter (change description)
    update_filter_obj = TopicFilter(topic_id=created_topic.topic_id)
    topic_vo_update = TopicVO(name="Updated Test Topic")
    update_results = topic_crud.update_by_filter(update_filter_obj, topic_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].name == "Updated Test Topic"

    # Delete topic by filter
    delete_filter_obj = TopicFilter(topic_id=created_topic.topic_id)
    delete_success = topic_crud.delete_by_filter(delete_filter_obj)
    assert delete_success

    # Verify deletion
    verify_delete_results = topic_crud.get_by_filter(delete_filter_obj)
    assert verify_delete_results is None or len(verify_delete_results) == 0


@pytest_asyncio.fixture
def author_crud() -> AuthorCRUD:
    """
    Create a CRUD object for the Author model.

    @return: AuthorCRUD: The CRUD object for the Author model.
    """
    return AuthorCRUD()


@pytest.mark.asyncio
async def test_author_crud_operations(author_crud) -> None:
    """
    Test the CRUD operations for the Author model.

    @param author_crud: AuthorCRUD: The CRUD object for the Author model.
    @return: None
    """
    # Create an author
    author_vo_create = AuthorVO(
        name="Doe",
        email="jane.doe@example.com"
    )
    created_author = author_crud.create(author_vo_create)
    assert created_author.name == "Doe"

    # Search by filter (using the name)
    filter_obj = AuthorFilter(author_id=created_author.author_id)
    search_results = author_crud.search_by_filter(filter_obj)
    assert len(search_results) == 1
    assert search_results[0].name == "Doe"

    # Get by filter to verify creation
    filter_obj = AuthorFilter(**created_author.dict())
    verify_create_results = author_crud.get_by_filter(filter_obj)
    assert verify_create_results is not None

    # Update author by filter (change name)
    update_filter_obj = AuthorFilter(author_id=created_author.author_id)
    author_vo_update = AuthorVO(
        name="Janet",
        email="janet.doe@example.com"
    )
    update_results = author_crud.update_by_filter(update_filter_obj, author_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].name == "Janet"

    # Delete author by filter
    delete_filter_obj = AuthorFilter(author_id=created_author.author_id)
    delete_success = author_crud.delete_by_filter(delete_filter_obj)
    assert delete_success

    # Verify deletion
    verify_delete_results = author_crud.get_by_filter(delete_filter_obj)
    assert verify_delete_results is None or len(verify_delete_results) == 0


@pytest_asyncio.fixture
def institution_crud() -> InstitutionCRUD:
    """
    Create a CRUD object for the Institution model.

    @return: InstitutionCRUD: The CRUD object for the Institution model.
    """
    return InstitutionCRUD()


@pytest.mark.asyncio
async def test_institution_crud_operations(institution_crud) -> None:
    """
    Test the CRUD operations for the Institution model.

    @param institution_crud: InstitutionCRUD: The CRUD object for the Institution model.
    @return: None
    """
    # Create an institution
    institution_vo_create = InstitutionVO(
        name="Test Institution"
    )
    created_institution = institution_crud.create(institution_vo_create)
    assert created_institution.name == "Test Institution"

    # Search by filter (using the name)
    filter_obj = InstitutionFilter(institution_id=created_institution.institution_id)
    search_results = institution_crud.search_by_filter(filter_obj)
    assert len(search_results) == 1
    assert search_results[0].name == "Test Institution"

    # Update institution by filter (change name)
    update_filter_obj = InstitutionFilter(institution_id=created_institution.institution_id)
    institution_vo_update = InstitutionVO(name="Updated Test Institution")
    update_results = institution_crud.update_by_filter(update_filter_obj, institution_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].name == "Updated Test Institution"

    # Delete institution by filter
    delete_filter_obj = InstitutionFilter(institution_id=created_institution.institution_id)
    delete_success = institution_crud.delete_by_filter(delete_filter_obj)
    assert delete_success

    # Verify deletion
    verify_delete_results = institution_crud.get_by_filter(delete_filter_obj)
    assert verify_delete_results is None or len(verify_delete_results) == 0


@pytest_asyncio.fixture
def department_crud() -> DepartmentCRUD:
    """
    Create a CRUD object for the Department model.

    @return: DepartmentCRUD: The CRUD object for the Department model.
    """
    return DepartmentCRUD()


@pytest.mark.asyncio
async def test_department_crud_operations(department_crud) -> None:
    """
    Test the CRUD operations for the Department model.

    @param department_crud: DepartmentCRUD: The CRUD object for the Department model.
    @return: None
    """
    # Create a department
    department_vo_create = DepartmentVO(
        name="Test Department",
        institution_id=1  # Assuming an institution with ID 1 exists
    )
    created_department = department_crud.create(department_vo_create)
    assert created_department.name == "Test Department"
    assert created_department.institution_id == 1

    # Search by filter (using the name)
    filter_obj = DepartmentFilter(department_id=created_department.department_id)
    search_results = department_crud.search_by_filter(filter_obj)
    assert len(search_results) == 1
    assert search_results[0].name == "Test Department"

    # Update department by filter (change name)
    update_filter_obj = DepartmentFilter(department_id=created_department.department_id)
    department_vo_update = DepartmentVO(name="Updated Test Department")
    update_results = department_crud.update_by_filter(update_filter_obj, department_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].name == "Updated Test Department"

    # Delete department by filter
    delete_filter_obj = DepartmentFilter(department_id=created_department.department_id)
    delete_success = department_crud.delete_by_filter(delete_filter_obj)
    assert delete_success

    # Verify deletion
    verify_delete_results = department_crud.get_by_filter(delete_filter_obj)
    assert verify_delete_results is None or len(verify_delete_results) == 0


@pytest.fixture
def author_institution_crud() -> AuthorInstitutionCRUD:
    """
    Create a CRUD object for the AuthorInstitution model.

    @return: AuthorInstitutionCRUD: The CRUD object for the AuthorInstitution model.
    """
    return AuthorInstitutionCRUD()


@pytest.mark.asyncio
async def test_author_institution_crud_operations(author_institution_crud) -> None:
    """
    Test the CRUD operations for the AuthorInstitution model.

    @param author_institution_crud: AuthorInstitutionCRUD: The CRUD object for the AuthorInstitution model.
    @return: None
    """
    # Create an author-institution link
    author_institution_vo_create = AuthorInstitutionVO(
        author_id=1,  # Assuming an author with ID 1 exists
        institution_id=1  # Assuming an institution with ID 1 exists
    )
    created_author_institution = author_institution_crud.create(author_institution_vo_create)
    assert created_author_institution.author_id == 1
    assert created_author_institution.institution_id == 1

    # Get by filter to verify creation
    filter_obj = AuthorInstitutionFilter(**author_institution_vo_create.dict())
    verify_create_results = author_institution_crud.get_by_filter(filter_obj)
    assert verify_create_results is not None

    # Update author-institution link by filter
    update_filter_obj = AuthorInstitutionFilter(**author_institution_vo_create.dict())
    author_institution_vo_update = AuthorInstitutionVO(
        author_id=1,  # Assuming an author with ID 1 exists
        institution_id=2  # Assuming an institution with ID 2 exists
    )
    update_results = author_institution_crud.update_by_filter(update_filter_obj, author_institution_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].institution_id == 2

    # Delete author-institution link by filter
    delete_filter_obj = AuthorInstitutionFilter(author_id=1, institution_id=2)
    delete_success = author_institution_crud.delete_by_filter(delete_filter_obj)
    assert delete_success


@pytest.fixture(scope="module")
def author_department_crud() -> AuthorDepartmentCRUD:
    """
    Create a CRUD object for the AuthorDepartment model.

    @return: AuthorDepartmentCRUD: The CRUD object for the AuthorDepartment model.
    """
    return AuthorDepartmentCRUD()


@pytest.mark.asyncio
async def test_author_department_crud_operations(author_department_crud) -> None:
    """
    Test the CRUD operations for the AuthorDepartment model.

    @param author_department_crud: AuthorDepartmentCRUD: The CRUD object for the AuthorDepartment model.
    @return: None
    """
    # Create an author-department link
    author_department_vo_create = AuthorDepartmentVO(
        author_id=1,  # Assuming an author with ID 1 exists
        department_id=1  # Assuming a department with ID 1 exists
    )
    created_author_department = author_department_crud.create(author_department_vo_create)
    assert created_author_department.author_id == 1
    assert created_author_department.department_id == 1

    # Get by filter to verify creation
    filter_obj = AuthorDepartmentFilter(**author_department_vo_create.dict())
    verify_create_results = author_department_crud.get_by_filter(filter_obj)
    assert verify_create_results is not None

    # Update author-department link by filter
    update_filter_obj = AuthorDepartmentFilter(**author_department_vo_create.dict())
    author_department_vo_update = AuthorDepartmentVO(
        author_id=1,  # Assuming an author with ID 1 exists
        department_id=2  # Assuming a department with ID 2 exists
    )
    update_results = author_department_crud.update_by_filter(update_filter_obj, author_department_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].department_id == 2

    # Delete author-department link by filter
    delete_filter_obj = AuthorDepartmentFilter(author_id=1, department_id=2)
    delete_success = author_department_crud.delete_by_filter(delete_filter_obj)
    assert delete_success


@pytest.fixture(scope="module")
def article_author_crud() -> ArticleAuthorCRUD:
    """
    Create a CRUD object for the ArticleAuthor model.

    @return: ArticleAuthorCRUD: The CRUD object for the ArticleAuthor model.
    """
    return ArticleAuthorCRUD()


@pytest.mark.asyncio
async def test_article_author_crud_operations(article_author_crud) -> None:
    """
    Test the CRUD operations for the ArticleAuthor model.

    @param article_author_crud: ArticleAuthorCRUD: The CRUD object for the ArticleAuthor model.
    @return: None
    """
    # Create an article-author link
    article_author_vo_create = ArticleAuthorVO(
        article_id=9999,
        author_id=9999
    )
    created_article_author = article_author_crud.create(article_author_vo_create)
    assert created_article_author.article_id == 9999
    assert created_article_author.author_id == 9999

    # Get by filter to verify creation
    filter_obj = ArticleAuthorFilter(**article_author_vo_create.dict())
    verify_create_results = article_author_crud.get_by_filter(filter_obj)
    assert verify_create_results is not None

    # Update article-author link by filter
    update_filter_obj = ArticleAuthorFilter(article_id=9999, author_id=9999)
    article_author_vo_update = ArticleAuthorVO(
        article_id=9998,
        author_id=9998
    )
    update_results = article_author_crud.update_by_filter(update_filter_obj, article_author_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].author_id == 9998

    # Delete article-author link by filter
    delete_filter_obj = ArticleAuthorFilter(article_id=9998, author_id=9998)
    delete_success = article_author_crud.delete_by_filter(delete_filter_obj)
    assert delete_success


@pytest.fixture(scope="module")
def article_citation_crud() -> ArticleCitationCRUD:
    """
    Create a CRUD object for the ArticleCitation model.

    @return: ArticleCitationCRUD: The CRUD object for the ArticleCitation model.
    """
    return ArticleCitationCRUD()


@pytest.mark.asyncio
async def test_article_citation_crud_operations(article_citation_crud) -> None:
    """
    Test the CRUD operations for the ArticleCitation model.

    @param article_citation_crud: ArticleCitationCRUD: The CRUD object for the ArticleCitation model.
    @return: None
    """
    # Create an article-citation link
    article_citation_vo_create = ArticleCitationVO(
        citing_article_id=9999,
        cited_article_id=9999
    )
    created_article_citation = article_citation_crud.create(article_citation_vo_create)
    assert created_article_citation.citing_article_id == 9999
    assert created_article_citation.cited_article_id == 9999

    # Get by filter to verify creation
    filter_obj = ArticleCitationFilter(**article_citation_vo_create.dict())
    verify_create_results = article_citation_crud.get_by_filter(filter_obj)
    assert verify_create_results is not None

    # Update article-citation link by filter
    update_filter_obj = ArticleCitationFilter(**article_citation_vo_create.dict())
    article_citation_vo_update = ArticleCitationVO(
        citing_article_id=9998,  # Assuming a citing article with ID 1 exists
        cited_article_id=9998  # Assuming a cited article with ID 3 exists
    )
    update_results = article_citation_crud.update_by_filter(update_filter_obj, article_citation_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].cited_article_id == 9998

    # Delete article-citation link by filter
    delete_filter_obj = ArticleCitationFilter(citing_article_id=9998, cited_article_id=9998)
    delete_success = article_citation_crud.delete_by_filter(delete_filter_obj)
    assert delete_success


@pytest.fixture(scope="module")
def topic_relationship_crud() -> TopicRelationshipCRUD:
    """
    Create a CRUD object for the TopicRelationship model.

    @return: TopicRelationshipCRUD: The CRUD object for the TopicRelationship model.
    """
    return TopicRelationshipCRUD()


@pytest.mark.asyncio
async def test_topic_relationship_crud_operations(topic_relationship_crud) -> None:
    """
    Test the CRUD operations for the TopicRelationship model.

    @param topic_relationship_crud: TopicRelationshipCRUD: The CRUD object for the TopicRelationship model.
    @return: None
    """
    # Create a topic-relationship link
    topic_relationship_vo_create = TopicRelationshipVO(
        parent_topic_id=1,  # Assuming a parent topic with ID 1 exists
        child_topic_id=2  # Assuming a child topic with ID 2 exists
    )
    created_topic_relationship = topic_relationship_crud.create(topic_relationship_vo_create)
    assert created_topic_relationship.parent_topic_id == 1
    assert created_topic_relationship.child_topic_id == 2

    # Get by filter to verify creation
    filter_object = TopicRelationshipFilter(**topic_relationship_vo_create.dict())
    verify_create_results = topic_relationship_crud.get_by_filter(filter_object)
    assert verify_create_results is not None

    # Update topic-relationship link by filter
    update_filter_obj = TopicRelationshipFilter(**topic_relationship_vo_create.dict())
    topic_relationship_vo_update = TopicRelationshipVO(
        parent_topic_id=1,  # Assuming a parent topic with ID 1 exists
        child_topic_id=3  # Assuming a child topic with ID 3 exists
    )
    update_results = topic_relationship_crud.update_by_filter(update_filter_obj, topic_relationship_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].child_topic_id == 3

    # Delete topic-relationship link by filter
    delete_filter_obj = TopicRelationshipFilter(parent_topic_id=1)
    delete_success = topic_relationship_crud.delete_by_filter(delete_filter_obj)
    assert delete_success


@pytest.fixture(scope="module")
def article_topic_crud() -> ArticleTopicCRUD:
    """
    Create a CRUD object for the ArticleTopic model.

    @return: ArticleTopicCRUD: The CRUD object for the ArticleTopic model.
    """
    return ArticleTopicCRUD()


@pytest.mark.asyncio
async def test_article_topic_crud_operations(article_topic_crud) -> None:
    """
    Test the CRUD operations for the ArticleTopic model.

    @param article_topic_crud: ArticleTopicCRUD: The CRUD object for the ArticleTopic model.
    @return: None
    """
    # Create an article-topic link
    article_topic_vo_create = ArticleTopicVO(
        article_id=1,  # Assuming an article with ID 1 exists
        topic_id=1  # Assuming a topic with ID 1 exists
    )
    created_article_topic = article_topic_crud.create(article_topic_vo_create)
    assert created_article_topic.article_id == 1
    assert created_article_topic.topic_id == 1

    # Get by filter to verify creation
    filter_object = ArticleTopicFilter(**article_topic_vo_create.dict())
    verify_create_results = article_topic_crud.get_by_filter(filter_object)
    assert verify_create_results is not None

    # Update article-topic link by filter
    update_filter_obj = ArticleTopicFilter(**article_topic_vo_create.dict())
    article_topic_vo_update = ArticleTopicVO(
        article_id=1,  # Assuming an article with ID 1 exists
        topic_id=2  # Assuming a topic with ID 2 exists
    )
    update_results = article_topic_crud.update_by_filter(update_filter_obj, article_topic_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].topic_id == 2

    # Delete article-topic link by filter
    delete_filter_obj = ArticleTopicFilter(article_id=1)
    delete_success = article_topic_crud.delete_by_filter(delete_filter_obj)
    assert delete_success
