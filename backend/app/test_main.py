"""
Overview:
This script is designed to conduct asynchronous tests on various endpoints of a FastAPI application. It leverages pytest
for testing, along with httpx's AsyncClient for making asynchronous HTTP requests. The script includes tests for the
root endpoint ("/") as well as other specific endpoints like "/catalog/" and "/analysis/". Each test function is
asynchronously defined, utilizing the AsyncClient to send GET requests to the respective endpoints and asserting the
expected response status codes and JSON content.

Key Components:
- pytest: A framework that makes it easy to write simple tests, yet scales to support complex functional testing.
- httpx: A fully featured HTTP client for Python 3, which provides async capabilities.
- AsyncClient: Part of httpx, used here for making asynchronous requests within the tests.
- ASGITransport: Also from httpx, used to wrap the FastAPI application for testing without running a server.

Test Functions:
- test_root: Tests the root endpoint ("/") to ensure it responds with the correct status code and JSON response.
- test_catalog_root: Tests the "/catalog/" endpoint for the expected status code and JSON response.
- test_analysis_root: Tests the "/analysis/" endpoint, checking for the correct status code and JSON response.

Usage:
The tests are meant to be run using the pytest framework. Ensure all dependencies are installed and execute the tests
by running 'pytest' in the command line within the project directory where this test script is located.
"""

import pytest
from httpx import AsyncClient, ASGITransport
from .main import app  # Import the FastAPI application instance


@pytest.mark.asyncio
async def test_root() -> None:
    """
    Asynchronously test the root endpoint "/"

    @return: None
    """
    # Asynchronously send a GET request to the root endpoint and assert response
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"uri": "/"}


@pytest.mark.asyncio
async def test_catalog_root() -> None:
    """
    Asynchronously test the "/catalog" endpoint

    @return: None
    """
    # Asynchronously send a GET request to the "/catalog/" endpoint and assert response
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/catalog/")
    assert response.status_code == 200
    assert response.json() == {"uri": "/catalog"}


@pytest.mark.asyncio
async def test_analysis_root() -> None:
    """
    Asynchronously test the "/analysis" endpoint

    @return: None
    """
    # Asynchronously send a GET request to the "/analysis/" endpoint and assert response
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/analysis/")
        print(response)
    assert response.status_code == 200
    assert response.json() == {"uri": "/analysis"}
