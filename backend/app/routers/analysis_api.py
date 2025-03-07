"""
Overview:
This script defines API routes for the Analysis module of a document processing service using FastAPI. It provides
endpoints for uploading documents to the server, where they are then processed to extract and analyze content, such
as titles, authors, abstracts, and keywords. The primary functionality includes saving the uploaded document to disk,
converting the document to XML using the GROBID service, parsing the XML to extract relevant information, and then
storing the extracted information in a database. The endpoints are designed to handle file uploads and respond with
the processed information or appropriate error messages.

Key Components:
- APIRouter setup with a prefix and tags for analysis-related routes.
- Root endpoint for checking API operability.
- Endpoint for uploading and processing documents, which includes:
  - Saving uploaded files to a designated directory.
  - Converting documents to XML format for further processing.
  - Extracting relevant information from the XML using custom parsing functions.
  - Storing the extracted information in a database.
  - Cleaning up temporary files to maintain server hygiene.

Usage:
This script can be integrated into a FastAPI application to offer a RESTful API for uploading and analyzing
documents, particularly useful for academic and research purposes. Clients such as academic platforms, data analysis
tools, or personal research repositories can utilize this API to automate the processing and cataloging of
academic papers and articles.
"""


from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path

from starlette.responses import JSONResponse

from ..services import analysis
from ..services.catalog import save_parse_article
import os


# Initialize the API router with a prefix and tags
router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    responses={404: {"description": "Not found"}},
)

# Create directories for storing uploaded papers and extracted XML files
papers_directory = Path().cwd() / "app" / "tmp" / "Papers"
xml_directory = Path().cwd() / "app" / "tmp" / "xml"
papers_directory.mkdir(parents=True, exist_ok=True)
xml_directory.mkdir(parents=True, exist_ok=True)


@router.get("/",
            summary="Analysis API Root",
            description="This is the root endpoint of the Analysis API. It can be used to check if the API is up and "
                        "running.",
            response_description="Provides the root URI for the Analysis API.",
            responses={
                200: {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "example": {"uri": "/analysis"}
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
    The root endpoint of the Analysis API.

    This endpoint provides a simple JSON response indicating the base URI for the analysis routes.

    @return: dict: A dictionary containing the base URI of the Analysis API.
    """
    return {'uri': '/analysis'}


@router.post("/upload/",
             summary="Upload a document",
             description="Upload a document to the server and process it. The document will be saved, analyzed, "
                         "and the extracted information will be stored.",
             response_description="The response contains the status of the upload and any extracted information from"
                                  "the document.",
             responses={
                 200: {
                     "description": "Document uploaded and processed successfully.",
                     "content": {
                         "application/json": {
                             "example": {
                                 "code": 200,
                                 "message": "File uploaded successfully",
                                 "data": {
                                     "title": "Example Title",
                                     "authors": [{"name": "Author One", "affiliation": "University of Examples"}],
                                     "abstract": "This is an example of an abstract from the uploaded document.",
                                     "keywords": ["example", "document", "upload"]
                                 }
                             }
                         }
                     },
                 },
                 500: {
                     "description": "Internal Server Error",
                     "content": {
                         "application/json": {
                             "example": {"detail": "Could not save file"}
                         }
                     },
                 }
             })
async def upload_document(file: UploadFile = File(...,
                                                  description="The document file to be uploaded.")) -> JSONResponse:
    """
    Upload a document to the server and parse it.

    @param file: UploadFile: The document to be uploaded.
    @return: JSONResponse: The response containing the status of the upload and any extracted information.
    @note: Upon successful upload, the document is saved to disk, and various processing tasks are performed on it,
    such as extracting text and analyzing content. The endpoint returns a JSON response containing the results
    of these operations.
    """
    try:
        file_location = papers_directory / Path(file.filename)
        print("File received")
        with open(file_location, "wb+") as file_object:
            content = await file.read()
            file_object.write(content)
        await file.close()
        print("File saved to disk: ", file_location)
        xml_location = analysis.get_extracted_xml(str(file_location), grobid_server="http://localhost:8070")
        article = analysis.get_article_object(xml_location)
        print("Article object created")
        article_vo = save_parse_article(article)
        print("Article saved to database")
        res = {"code": 200,
               "message": "File uploaded successfully",
               "data": article.to_json(article_id=article_vo.article_id)
               }
        os.remove(file_location)
        os.remove(xml_location)
        print("tmp files removed")
        return JSONResponse(status_code=200, content=res)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Could not save file")
