# Backend Service
This backend service is structured to support various functionalities including database operations, service integration, API routing, and core business logic implementation. It is designed with modularity and scalability in mind.

# Project Structure

This project is organized as follows:

- `.flake8`: Configuration file for the Flake8 Python linter, setting code style rules.
- `Dockerfile`: Contains instructions for Docker to build the project's container, specifying the environment and necessary commands.
- `pytest.ini`: Configuration file for Pytest, defining testing options and behaviors.
- `README.md`: The project's README file, providing an overview, installation instructions, usage, and additional information.
- `requirements.txt`: Lists the Python package dependencies required by the project.

## App Module

The `app` directory contains the main application code and is structured as follows:

### Root

- `app/main.py`: The entry point of the FastAPI application, responsible for setting up routes and configurations.
- `app/test_main.py`: Contains tests for the main application logic.
- `app/__init__.py`: Initializes the FastAPI app and integrates other components.

### Routers

- `app/routers/response_example.py`: Provides examples of response models used by the application's endpoints.
- `app/routers/__init__.py`: Initializes the routers module, often by importing and including router modules.

### Services

Contains the core business logic of the application:

- `app/services/analysis.py`: Implements functions related to data analysis and processing.
- `app/services/catalog.py`: Manages catalog-related operations, such as querying and updating entries.
- `app/services/models.py`: Defines data models used across various services.
- `app/services/schema.py`: Utilizes Pydantic schemas for data validation and serialization.
- `app/services/test_analysis.py`: Includes tests for the analysis service functions.
- `app/services/__init__.py`: Initializes the services module.

#### Extractor Module

Dedicated to extracting content from articles:

- `app/services/Extractor/extractor.py`: Core functions for content extraction from articles.
- `app/services/Extractor/__init__.py`: Initializes the Extractor module.

##### Grobid Submodule

Integrates with the GROBID service for extracting content from PDF documents:

- `app/services/Extractor/Grobid/client.py`: Base client for GROBID service interaction.
- `app/services/Extractor/Grobid/grobid_client.py`: Extended client tailored to this project's needs.
- `app/services/Extractor/Grobid/__init__.py`: Initializes the Grobid submodule.

#### Parser Module

Handles the parsing and interpretation of extracted data:

- `app/services/Parser/parser.py`: Contains functions for parsing raw data into structured formats.
- `app/services/Parser/types.py`: Defines custom types used in the parsing process.
- `app/services/Parser/__init__.py`: Initializes the Parser module.



# Installation

> Please make sure the Python and Grobid are available on your machine. Go [Setup.md](../Documents/Implementation/Setup.md#backend-service) for more information

1. Clone the repository
2. Install dependencies
   ```
   cd backend
   pip install -r requirements.txt
   ```
3. Configure your environment variables as necessary

# Running the Application

1. Enter the `backend` directory
    ```
    cd backend
    ```
2. (Optional) Cancel TEST MODE (default is True) by setting the environment variable `TEST_MODE` to `False`
    ```
    export TEST_MODE=False
    ```
3. Execute the following command
    ```
    python -m app.main
    ```

# Testing

1. To run tests, execute

```
python -m pytest
```

# API Documents

If successfully running the application, you can access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

If not, you can check the API documentation at [API-Doc.md](../Documents/Implementation/API/API-Doc.md).
