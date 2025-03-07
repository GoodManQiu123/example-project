"""
Overview:
This FastAPI application serves as a backend service providing various APIs related to catalog and
analysis functionalities. It includes Cross-Origin Resource Sharing (CORS) middleware to handle cross-origin
requests, ensuring the API can be accessed from different domains. The application defines multiple routes through
the inclusion of router modules for catalog and analysis features, facilitating modular development and easy
maintenance. The root endpoint provides a basic check to see if the API is operational and offers information about
the API's base URI.

Dependencies:
- FastAPI: Web framework for building APIs with Python 3.6+ based on standard Python type hints.
- CORSMiddleware: Middleware for handling Cross-Origin Resource Sharing (CORS), allowing cross-origin requests.
- uvicorn: ASGI server for running the application, enabling async programming and providing lightning-fast performance.

Structure:
- The application instance is created.
- CORS middleware is added to the application configuration to allow cross-origin requests.
- Router modules for catalog and analysis functionalities are included, defining specific API endpoints.
- A root endpoint ('/') is defined for basic API interaction and status checking.
- The application is configured to run using Uvicorn with the specified host and port.
"""

from fastapi import FastAPI
from .routers import catalog_api, analysis_api
from starlette.middleware.cors import CORSMiddleware

# Create a FastAPI application instance
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(catalog_api.router)
app.include_router(analysis_api.router)


@app.get("/",
         summary="API Root",
         description="This is the root endpoint of the API. It serves as an initial point to check the API status "
                     "and discover the base URI.",
         response_description="Provides the base URI of the API.",
         responses={
             200: {
                 "description": "Successful Response",
                 "content": {
                     "application/json": {
                         "example": {"uri": "/"}
                     }
                 },
             },
             500: {
                 "description": "Internal Server Error",
                 "content": {
                     "application/json": {
                         "example": {"detail": "Internal server error"}
                     }
                 },
             },
         })
async def root() -> dict:
    """
    The API's root endpoint.

    This endpoint offers a simple JSON response that includes the base URI for the API. It's an excellent starting
    point to explore the API's features.

    @return: dict: A dictionary containing the base URI of the API.
    """
    return {"uri": "/"}


if __name__ == '__main__':
    """
    Run the FastAPI application using Uvicorn when the script is executed directly.
    """
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
