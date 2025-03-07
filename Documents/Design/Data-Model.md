Below is a documentation of the database structure based on the provided DBML, detailing each table, its fields, types, constraints, and descriptions for clarity:

### 1. Article Table

| Field             | Type        | Constraint | Description                                                |
|-------------------|-------------|------------|------------------------------------------------------------|
| id                | int         | PK, Increment | Unique identifier for each article.                        |
| title             | varchar(255) | Not Null   | The title of the article.                                  |
| publisher         | varchar(255) | Null       | The publisher of the article.                              |
| date              | date        | Null       | The original date the article was written or submitted.    |                       |
| issn              | varchar(20)  | Null, Unique | International Standard Serial Number of the article.       |
| eissn             | varchar(20)  | Null, Unique | Electronic International Standard Serial Number.           |
| volume            | varchar(10)  | Null       | The volume in which the article was published.             |
| issue             | varchar(10)  | Null       | The issue of the volume in which the article was published.|
| page              | varchar(10) | Null       | The page number(s) of the article in the publication.      |
| doi               | varchar(255) | Null, Unique | Digital Object Identifier for the article.                 |
| type           | varchar(255) | Null       | Journal Article /  Conference Paper / Book / ... |
| container_title   | varchar(255) | Null       | Journal title / Conference name/ Book name / ...|


### 2. Topic Table

| Field | Type          | Constraint    | Description                       |
|-------|---------------|---------------|-----------------------------------|
| id    | int           | PK, Increment | Unique identifier for each topic. |
| name  | varchar(100)  | Not Null, Unique | Name of the topic.                |

### 3. Article_Topic Table

| Field      | Type | Constraint | Description                                    |
|------------|------|------------|------------------------------------------------|
| article_id | int  | Not Null   | References `id` in the Article table.          |
| topic_id   | int  | Not Null   | References `id` in the Topic table.            |

### 4. Author Table

| Field | Type          | Constraint    | Description                          |
|-------|---------------|---------------|--------------------------------------|
| id    | int           | PK, Increment | Unique identifier for each author.   |
| name  | varchar(255)  | Not Null      | Name of the author.    |
| email | varchar(255)  | Null, Unique  | Email address of the author.         |
| affiliation | varchar(255)  | Null | Affiliation information of this author。         |

### 5. Institution Table

| Field | Type          | Constraint          | Description                             |
|-------|---------------|---------------------|-----------------------------------------|
| id    | int           | PK, Increment       | Unique identifier for each institution. |
| name  | varchar(255)  | Not Null, Unique    | Name of the institution.                |

### 6. Department Table

| Field          | Type         | Constraint       | Description                                |
|----------------|--------------|------------------|--------------------------------------------|
| id             | int          | PK, Increment    | Unique identifier for each department.     |
| name           | varchar(255) | Not Null | Name of the department.                    |
| institution_id | int          | Not Null         | References `id` in the Institution table.  |

### 7. Article_Author Table

| Field      | Type | Constraint | Description                                   |
|------------|------|------------|-----------------------------------------------|
| article_id | int  | Not Null   | References `id` in the Article table.         |
| author_id  | int  | Not Null   | References `id` in the Author table.          |

### 8. Article_Citation Table

| Field            | Type | Constraint | Description                                        |
|------------------|------|------------|----------------------------------------------------|
| citing_article_id| int  | Not Null   | References `id` in the Article table (citing).     |
| cited_article_id | int  | Not Null   | References `id` in the Article table (being cited).|

### 9. TopicRelationship Table

| Field          | Type | Constraint | Description|
|----------------|------|------------|----------------------------------------------|
| parent_topic_id| int  | Not Null   | References `id` in the Topic table (parent). |
| child_topic_id | int  | Not Null   | References `id` in the Topic table (child).  |

### 10. Author_Institution Table

| Field          | Type | Constraint | Description                                         |
|----------------|------|------------|-----------------------------------------------------|
| author_id      | int  | Not Null   | References `id` in the Author table.                |
| institution_id | int  | Not Null   | References `id` in the Institution table.           |

### 11. Author_Department Table

| Field        | Type | Constraint | Description                                       |
|--------------|------|------------|---------------------------------------------------|
| author_id    | int  | Not Null   | References `id` in the Author table.              |
| department_id| int  | Not Null   | References `id` in the Department table.          |



This documentation provides a clear overview of each table's structure within the database, including field names, data types, constraints, and a brief description of what each field represents.