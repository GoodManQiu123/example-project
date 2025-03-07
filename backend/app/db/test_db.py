"""
Overview:
This pytest file is designed for comprehensive testing of database models related to academic articles, authors, topics,
institutions, and their relationships within an article processing and academic metadata management system. It
leverages pytest_asyncio for asynchronous test execution, mirroring the asynchronous nature of database operations in
modern web applications.

The file includes fixtures for creating temporary instances of models such as Article, Topic, Author, Institution, and
Department, among others. These fixtures are used to set up a pre-defined state before each test and are cleaned up
afterward, ensuring test isolation and preventing side effects.

Test cases are organized to cover CRUD (Create, Read, Update, Delete) operations for each model, ensuring the
integrity and functionality of the system's database interactions. This includes testing the creation of articles,
association of articles with topics and authors, and the establishment of hierarchical relationships between topics
(parent-child relationships), as well as associations between authors and institutions or departments.

Usage:
The tests can be executed using the pytest framework to validate the behavior of the system's data layer, ensuring
consistency and reliability in handling academic metadata. This testing suite is crucial for maintaining data
integrity, especially when introducing new features or making changes to the database schema.

This file plays a vital role in the quality assurance process, allowing developers to detect and address issues early
in the development lifecycle. It also aids in ensuring that modifications do not inadvertently break existing
functionalities, contributing to the overall stability and reliability of the system.
"""


import pytest
import pytest_asyncio
from backend.app.db.mongoengine_models import Article, Topic, Author, Institution, Department, AuthorInstitution, \
    AuthorDepartment, ArticleCitation, TopicRelationship, ArticleTopic, ArticleAuthor


@pytest_asyncio.fixture
async def article() -> Article:
    """
    Setup: Create a new Article object

    @return: Article - The created article
    """
    test_article = Article(
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
        type="Journal Article",  # Added new field
        container_title="Test Journal"  # Added new field
    )
    test_article.save()

    yield test_article

    test_article.delete()


@pytest_asyncio.fixture
async def citing_article() -> Article:
    """
    Setup: Create a new Article object to represent the citing article

    @return: Article - The created article
    """
    article = Article(
        title="Citing Article",
        abstract="This is a citing article",
        publisher="Citing Publisher",
        date="2024-02-01",
        issn="2345-6789",
        eissn="9876-5432",
        volume="2",
        issue="1",
        page="11-20",
        doi="10.1000/citing",
        meeting="Citing Conference",
        file_path="/path/to/citing_article.pdf",
        type="Conference Paper",  # Added new field
        container_title="Annual Tech Conference"  # Added new field
    )
    article.save()

    yield article

    article.delete()


@pytest_asyncio.fixture
async def cited_article() -> Article:
    """
    Setup: Create a new Article object to represent the cited article

    @return: Article - The created article
    """
    article = Article(
        title="Cited Article",
        abstract="This is a cited article",
        publisher="Cited Publisher",
        date="2024-01-15",
        issn="1234-5678",
        eissn="8765-4321",
        volume="1",
        issue="2",
        page="21-30",
        doi="10.1000/cited",
        meeting="Cited Conference",
        file_path="/path/to/cited_article.pdf",
        type="Journal Article",  # Added new field
        container_title="Scientific Journal"  # Added new field
    )
    article.save()

    yield article

    article.delete()


@pytest_asyncio.fixture
async def author() -> Author:
    """
    Setup: Create a new Author object

    @return: Author - The created author
    """
    test_author = Author(name="Doe", email="john.doe@example.com")
    test_author.save()

    # Yield the setup object to be used by the test
    yield test_author

    # Teardown: Clean up any created data after the test finishes
    test_author.delete()


@pytest_asyncio.fixture
async def topic() -> Topic:
    """"
    Setup: Create a new Topic object

    @return: Topic - The created topic
    """
    test_topic = Topic(name="Test Topic")
    test_topic.save()

    yield test_topic

    test_topic.delete()


@pytest_asyncio.fixture
async def institution() -> Institution:
    """
    Setup: Create a new Institution object

    @return: Institution - The created institution
    """
    test_institution = Institution(name="Test Institution")
    test_institution.save()

    # Yield the setup object to be used by the test
    yield test_institution

    # Teardown: Clean up any created data after the test finishes
    test_institution.delete()


@pytest_asyncio.fixture
async def department(institution):
    """
    Setup: Create a new Department object

    @param institution: Institution - The institution to associate with the department
    @return: Department - The created department
    """
    test_department = Department(name="Test Department", institution_id=institution.institution_id)
    test_department.save()

    yield test_department

    test_department.delete()


@pytest_asyncio.fixture
async def parent_topic() -> Topic:
    """
    Setup: Create a new Topic object for the parent topic

    @return: Topic - The created topic
    """
    # Setup: Create a new Topic object for the parent topic
    parent = Topic(name="Parent Topic")
    parent.save()

    # Yield the setup object to be used by the test
    yield parent

    # Teardown: Clean up any created data after the test finishes
    parent.delete()


@pytest_asyncio.fixture
async def child_topic() -> Topic:
    """
    Setup: Create a new Topic object for the child topic

    @return: Topic - The created topic
    """
    # Setup: Create a new Topic object for the child topic
    child = Topic(name="Child Topic")
    child.save()

    # Yield the setup object to be used by the test
    yield child

    # Teardown: Clean up any created data after the test finishes
    child.delete()


@pytest_asyncio.fixture
async def new_institution() -> Institution:
    """
    Setup: Create a new Institution object for testing updates

    @return: Institution - The created institution
    """
    new_inst = Institution(name="New Test Institution")
    new_inst.save()

    yield new_inst

    new_inst.delete()


@pytest_asyncio.fixture
async def new_department(new_institution) -> Department:
    """
    Setup: Create a new Department object for testing updates, associated with a new institution

    @param new_institution: Institution - The new institution to associate with the department
    @return: Department - The created department
    """
    new_dept = Department(name="New Test Department", institution_id=new_institution.institution_id)
    new_dept.save()

    yield new_dept

    new_dept.delete()


@pytest_asyncio.fixture
async def new_cited_article() -> Article:
    """
    Setup: Create a new Article object to represent an alternative cited article for testing updates

    @return: Article - The created article
    """
    new_article = Article(
        title="New Cited Article",
        abstract="This is a new cited article",
        publisher="New Cited Publisher",
        date="2024-03-01",
        issn="3456-7890",
        eissn="0987-6543",
        volume="3",
        issue="2",
        page="31-40",
        doi="10.1000/newcited",
        meeting="New Cited Conference",
        file_path="/path/to/new_cited_article.pdf",
        type="Review Article",  # Added new field
        container_title="New Scientific Journal"  # Added new field
    )
    new_article.save()

    yield new_article

    new_article.delete()


@pytest_asyncio.fixture
async def new_child_topic() -> Topic:
    """
    Setup: Create a new Topic object for an alternative child topic for testing updates

    @return: Topic - The created topic
    """
    new_child = Topic(name="New Child Topic")
    new_child.save()

    yield new_child

    new_child.delete()


@pytest.mark.asyncio
async def test_article_crud(article) -> None:
    """
    Test the CRUD operations for the Article model

    @param article: Article - The article to test
    @return: None
    """
    # Read (The article is already created by the fixture)
    fetched_article = Article.objects(article_id=article.article_id).first()
    assert fetched_article.title == "Test Article", "Failed to fetch the created Article"

    # Update
    fetched_article.update(set__title="Updated Test Article")
    updated_article = Article.objects(article_id=article.article_id).first()
    assert updated_article.title == "Updated Test Article", "Failed to update the Article"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_topic_crud(topic) -> None:
    """
    Test the CRUD operations for the Topic model

    @param topic: Topic - The topic to test
    @return: None
    """
    # Read (The topic is already created by the fixture)
    fetched_topic = Topic.objects(topic_id=topic.id).first()
    assert fetched_topic.name == "Test Topic", "Failed to fetch the created Topic"

    # Update
    fetched_topic.update(set__name="Updated Test Topic")
    updated_topic = Topic.objects(topic_id=topic.id).first()
    assert updated_topic.name == "Updated Test Topic", "Failed to update the Topic"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_author_crud(author) -> None:
    """
    Test the CRUD operations for the Author model

    @param author: Author - The author to test
    @return: None
    """
    # Read (The author is already created by the fixture)
    fetched_author = Author.objects(author_id=author.id).first()
    assert fetched_author.name == "Doe", "Failed to fetch the created Author"

    # Update
    fetched_author.update(set__name="Smith")
    updated_author = Author.objects(author_id=author.id).first()
    assert updated_author.name == "Smith", "Failed to update the Author"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_institution_crud(institution) -> None:
    """
    Test the CRUD operations for the Institution model

    @param institution: Institution - The institution to test
    @return: None
    """
    # Read (The institution is already created by the fixture)
    fetched_institution = Institution.objects(institution_id=institution.id).first()
    assert fetched_institution.name == "Test Institution", "Failed to fetch the created Institution"

    # Update
    fetched_institution.update(set__name="Updated Test Institution")
    updated_institution = Institution.objects(institution_id=institution.id).first()
    assert updated_institution.name == "Updated Test Institution", "Failed to update the Institution"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_department_crud(institution) -> None:
    """
    Test the CRUD operations for the Department model

    @param institution: Institution - The institution to associate with the department
    @return: None
    """
    # Now you can use the 'institution' fixture in your test
    # Create
    department = Department(name="Computer Science", institution_id=institution.institution_id)
    department.save()
    assert department.department_id is not None, "Failed to create a new Department"

    # Read
    fetched_department = Department.objects(department_id=department.id).first()
    assert fetched_department.name == "Computer Science", "Failed to fetch the created Department"

    # Update
    fetched_department.update(set__name="Updated Computer Science")
    updated_department = Department.objects(department_id=department.id).first()
    assert updated_department.name == "Updated Computer Science", "Failed to update the Department"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_author_institution_crud(author, institution, new_institution) -> None:
    """
    Test the CRUD operations for the AuthorInstitution model

    @param author: Author - The author to associate with the institution
    @param institution: Institution - The institution to associate with the author
    @param new_institution: Institution - The new institution to associate with the author
    @return: None
    """
    # Create
    author_institution = AuthorInstitution(author_id=author.author_id, institution_id=institution.institution_id)
    author_institution.save()
    assert author_institution.id is not None, "Failed to create a new AuthorInstitution relationship"

    # Read
    fetched_author_institution = AuthorInstitution.objects(id=author_institution.id).first()
    assert fetched_author_institution.author_id == author.author_id, "Failed to fetch the created AuthorInstitution " \
                                                                     "relationship "

    # Update
    fetched_author_institution.update(set__institution_id=new_institution.institution_id)
    fetched_author_institution.reload()
    assert fetched_author_institution.institution_id == new_institution.institution_id, "Failed to update the " \
                                                                                        "AuthorInstitution " \
                                                                                        "relationship "

    # Delete
    fetched_author_institution.delete()
    assert AuthorInstitution.objects(
        id=fetched_author_institution.id).first() is None, "Failed to delete the AuthorInstitution relationship"


@pytest.mark.asyncio
async def test_author_department_crud(author, department, new_department) -> None:
    """
    Test the CRUD operations for the AuthorDepartment model

    @param author: Author - The author to associate with the department
    @param department: Department - The department to associate with the author
    @param new_department: Department - The new department to associate with the author
    @return: None
    """
    # Create
    author_department = AuthorDepartment(author_id=author.author_id, department_id=department.department_id)
    author_department.save()
    assert author_department.id is not None, "Failed to create a new AuthorDepartment relationship"

    # Read
    fetched_author_department = AuthorDepartment.objects(id=author_department.id).first()
    assert fetched_author_department.author_id == author.author_id, "Failed to fetch the created AuthorDepartment " \
                                                                    "relationship "

    # Update
    fetched_author_department.update(set__department_id=new_department.department_id)
    fetched_author_department.reload()
    assert fetched_author_department.department_id == new_department.department_id, "Failed to update the " \
                                                                                    "AuthorDepartment relationship "

    # Delete
    fetched_author_department.delete()
    assert AuthorDepartment.objects(
        id=fetched_author_department.id).first() is None, "Failed to delete the AuthorDepartment relationship"


@pytest.mark.asyncio
async def test_article_citation_crud(citing_article, cited_article, new_cited_article) -> None:
    """
    Test the CRUD operations for the ArticleCitation model

    @param citing_article: Article - The citing article
    @param cited_article: Article - The cited article
    @param new_cited_article: Article - The new cited article
    @return: None
    """
    # Create
    article_citation = ArticleCitation(citing_article_id=citing_article.article_id,
                                       cited_article_id=cited_article.article_id)
    article_citation.save()
    assert article_citation.id is not None, "Failed to create a new ArticleCitation"

    # Read
    fetched_article_citation = ArticleCitation.objects(id=article_citation.id).first()
    assert fetched_article_citation.citing_article_id == citing_article.article_id, "Failed to fetch the created " \
                                                                                    "ArticleCitation "

    # Update
    fetched_article_citation.update(set__cited_article_id=new_cited_article.article_id)
    fetched_article_citation.reload()
    assert fetched_article_citation.cited_article_id == new_cited_article.article_id, "Failed to update the " \
                                                                                      "ArticleCitation "

    # Delete
    fetched_article_citation.delete()
    assert ArticleCitation.objects(
        id=fetched_article_citation.id).first() is None, "Failed to delete the ArticleCitation"


@pytest.mark.asyncio
async def test_topic_relationship_crud(parent_topic, child_topic, new_child_topic) -> None:
    """
    Test the CRUD operations for the TopicRelationship model

    @param parent_topic: Topic - The parent topic
    @param child_topic: Topic - The child topic
    @param new_child_topic: Topic - The new child topic
    @return: None
    """
    # Create
    topic_relationship = TopicRelationship(parent_topic_id=parent_topic.topic_id, child_topic_id=child_topic.topic_id)
    topic_relationship.save()
    assert topic_relationship.id is not None, "Failed to create a new TopicRelationship"

    # Read
    fetched_topic_relationship = TopicRelationship.objects(id=topic_relationship.id).first()
    assert fetched_topic_relationship.parent_topic_id == parent_topic.topic_id, "Failed to fetch the created " \
                                                                                "TopicRelationship "

    # Update
    fetched_topic_relationship.update(set__child_topic_id=new_child_topic.topic_id)
    fetched_topic_relationship.reload()
    assert fetched_topic_relationship.child_topic_id == new_child_topic.topic_id, "Failed to update the " \
                                                                                  "TopicRelationship "

    # Delete
    fetched_topic_relationship.delete()
    assert TopicRelationship.objects(
        id=fetched_topic_relationship.id).first() is None, "Failed to delete the TopicRelationship"


@pytest.mark.asyncio
async def test_article_topic_crud(article, topic) -> None:
    """
    Test the CRUD operations for the ArticleTopic model.

    @param article: Article - The article involved in the relationship.
    @param topic: Topic - The topic related to the article.
    @return: None
    """
    # Assuming ArticleTopic model exists and has article_id and topic_id fields
    # Create
    article_topic = ArticleTopic(article_id=article.id, topic_id=topic.id)
    article_topic.save()
    assert article_topic.id is not None, "Failed to create a new ArticleTopic relationship"

    # Read
    fetched_article_topic = ArticleTopic.objects(id=article_topic.id).first()
    assert fetched_article_topic.article_id == article.id and fetched_article_topic.topic_id == topic.id, \
        "Failed to fetch the created ArticleTopic relationship"

    # Delete
    fetched_article_topic.delete()
    assert ArticleTopic.objects(id=article_topic.id).first() is None, "Failed to delete the ArticleTopic relationship"


@pytest.mark.asyncio
async def test_article_author_crud(article, author) -> None:
    """
    Test the CRUD operations for the ArticleAuthor model.

    @param article: Article - The article involved in the relationship.
    @param author: Author - The author related to the article.
    @return: None
    """
    # Create
    article_author = ArticleAuthor(article_id=article.id, author_id=author.id)
    article_author.save()
    assert article_author.id is not None, "Failed to create a new ArticleAuthor relationship"

    # Read
    fetched_article_author = ArticleAuthor.objects(id=article_author.id).first()
    assert fetched_article_author.article_id == article.id and fetched_article_author.author_id == author.id, \
        "Failed to fetch the created ArticleAuthor relationship"

    # Delete
    fetched_article_author.delete()
    assert ArticleAuthor.objects(
        id=article_author.id).first() is None, "Failed to delete the ArticleAuthor relationship"
