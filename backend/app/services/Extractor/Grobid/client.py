"""
Overview:
This script defines the ApiClient class, a flexible and generic client for interacting with RESTful APIs. It provides
methods for making GET, POST, PUT, and DELETE requests, handling authentication, encoding request data, and decoding
responses. The class is designed to be subclassed and extended for specific API services, with customizable encoding
and decoding methods to support various content types beyond the default JSON. Authentication credentials can be
passed during initialization, and additional headers, query parameters, and file uploads can be included in API
calls. The service status can be checked by specifying a status endpoint. This client is useful in a wide range of
applications that require interaction with RESTful APIs, from simple data retrieval to complex integrations.

Key Components:
- ApiClient class: Provides a structured way to interact with RESTful APIs, including methods for all common HTTP
  verbs.
- _generate_xml_path function: Helper function to create an appropriate file path for XML files derived from PDFs.
- Encoding and decoding methods: Allow for customization of request and response handling, facilitating the use of
  various content types.

Usage:
The ApiClient can be utilized in applications that need to interact with RESTful APIs, such as web services, data
integration platforms, and microservices architectures. It serves as a foundational tool for building API clients for
specific services, streamlining the process of request preparation, execution, and response handling.
"""

from copy import deepcopy
import json
import requests

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class ApiClient(object):
    """
    Client to interact with a generic Rest API.

    Subclasses should implement functionality accordingly with the provided
    service methods, i.e. ``get``, ``post``, ``put`` and ``delete``.
    """

    accept_type = "application/xml"
    api_base = None

    def __init__(
        self, base_url, username=None, api_key=None, status_endpoint=None, timeout=60
    ):
        """
        Initialise client.

        @param base_url: str: The base URL to the service being used.
        @param username: str: The username to authenticate with.
        @param api_key: str: The API key to authenticate with.
        @param status_endpoint: str: The endpoint to check the service status.
        @param timeout: int: Maximum time before timing out.
        @return: None
        """
        self.base_url = base_url
        self.username = username
        self.api_key = api_key
        self.status_endpoint = urljoin(self.base_url, status_endpoint)
        self.timeout = timeout

    @staticmethod
    def encode(request, data):
        """
        Add request content data to request body, set Content-type header.

        Should be overridden by subclasses if not using JSON encoding.

        @param request: HTTPRequest: The request object.
        @param data: dict or None: Data to be encoded.
        @return: HTTPRequest: The request object.
        """
        if data is None:
            return request

        request.add_header("Content-Type", "application/json")
        request.data = json.dumps(data)

        return request

    @staticmethod
    def decode(response):
        """
        Decode the returned data in the response.

        Should be overridden by subclasses if something else than JSON is
        expected.

        @param response: HTTPResponse: The response object.
        @return: dict or None: The decoded data.
        """
        try:
            return response.json()
        except ValueError as e:
            return e.message

    def get_credentials(self):
        """
        Returns parameters to be added to authenticate the request.

        This lives on its own to make it easier to re-implement it if needed.

        @return: dict: The credentials to be used in the request.
        """
        return {"username": self.username, "api_key": self.api_key}

    def call_api(
        self,
        method,
        url,
        headers=None,
        params=None,
        data=None,
        files=None,
        timeout=None,
    ):
        """
        Call API.

        This returns object containing data, with error details if applicable.

        @param method: str: The HTTP method to use.
        @param url: str: Resource location relative to the base URL.
        @param headers: dict or None: Extra request headers to set.
        @param params: dict or None: Query-string parameters.
        @param data: dict or None: Request body contents for POST or PUT requests.
        @param files: dict or None: Files to be passed to the request.
        @param timeout: int: Maximum time before timing out.
        @return: tuple: ResultParser or ErrorParser.
        """
        headers = deepcopy(headers) or {}
        headers["Accept"] = self.accept_type
        params = deepcopy(params) or {}
        data = data or {}
        files = files or {}
        # if self.username is not None and self.api_key is not None:
        #    params.update(self.get_credentials())
        r = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            files=files,
            data=data,
            timeout=timeout,
        )

        return r, r.status_code

    def get(self, url, params=None, **kwargs):
        """
        Call the API with a GET request.

        @param url: str: Resource location relative to the base URL.
        @param params: dict or None: Query-string parameters.
        @return: ResultParser or ErrorParser.
        """
        return self.call_api("GET", url, params=params, **kwargs)

    def delete(self, url, params=None, **kwargs):
        """
        Call the API with a DELETE request.

        @param url: str: Resource location relative to the base URL.
        @param params: dict or None: Query-string parameters.
        @return: ResultParser or ErrorParser.
        """
        return self.call_api("DELETE", url, params=params, **kwargs)

    def put(self, url, params=None, data=None, files=None, **kwargs):
        """
        Call the API with a PUT request.

        @param url: str: Resource location relative to the base URL.
        @param params: dict or None: Query-string parameters.
        @param data: dict or None: Request body contents.
        @param files: dict or None: Files to be passed to the request.
        @return: ResultParser or ErrorParser.
        """
        return self.call_api(
            "PUT", url, params=params, data=data, files=files, **kwargs
        )

    def post(self, url, params=None, data=None, files=None, **kwargs):
        """
        Call the API with a POST request.

        @param url: str: Resource location relative to the base URL.
        @param params: dict or None: Query-string parameters.
        @param data: dict or None: Request body contents.
        @param files: dict or None: Files to be passed to the request.
        @return: ResultParser or ErrorParser.
        """
        return self.call_api(
            method="POST", url=url, params=params, data=data, files=files, **kwargs
        )

    def service_status(self, **kwargs):
        """
        Call the API to get the status of the service.

        @param kwargs: dict: Extra parameters to pass to the request.
        @return: ResultParser or ErrorParser.
        """
        return self.call_api(
            "GET", self.status_endpoint, params={"format": "json"}, **kwargs
        )
