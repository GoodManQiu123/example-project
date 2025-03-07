"""
Overview:
This module introduces an Extractor class designed to convert PDF files into XML format by leveraging Grobid, an
open-source application for extracting and processing PDF documents in the domain of scholarly articles. It includes
a utility function to construct the expected XML file path based on the PDF file location, replacing the 'Papers'
directory with 'xml' in the path and changing the file extension. The Extractor class initializes with the PDF file
path and the Grobid server URL, then executes the conversion process, ensuring the Grobid service is running by making
a preliminary check. The conversion utilizes Grobid's 'processFulltextDocument' service, and the resulting XML content
is written to the designated file path. This module is crucial for automated document processing pipelines, facilitating
the extraction of structured scholarly content from unstructured PDF files for subsequent analysis or data extraction
tasks.

Key Components:
- _generate_xml_path: Generates the file path for the XML version of a PDF file.
- Extractor class: Manages the conversion of PDF to XML using Grobid, including service availability checks.
- pdf_to_xml: Primary method for converting the PDF file to XML and saving the output.
- _check_grobid_running: Verifies the availability of the Grobid service before attempting conversion.

Usage:
This module is suited for applications in digital libraries, content management systems for academic publications, and
research platforms requiring the extraction of structured data from scholarly PDF documents.
"""

from .Grobid.grobid_client import GrobidClient
from pathlib import Path
import subprocess


def _generate_xml_path(pdf_file_path):
    """
    Generate the file path for the XML file corresponding to the PDF file.

    @param pdf_file_path: str: The path to the PDF file.
    @return: str: The path to the XML file.
    """
    pdf_path = Path(pdf_file_path)
    pdf_dir = str(pdf_path.parent)
    xml_dir = pdf_dir.replace("Papers", "xml")
    xml_file_path = Path(xml_dir) / (pdf_path.stem + ".xml")
    return str(xml_file_path)


class Extractor(object):
    """
    Extractor class to convert PDF files to XML using Grobid.
    """
    def __init__(self, artical_path, grobid_server="http://10.1.0.10:8070"):
        """
        Initialize the Extractor object with the path to the PDF file and the URL of the Grobid server.

        @param artical_path: str: The path to the PDF file.
        @param grobid_server: str: The URL of the Grobid server.
        @return: None
        """
        self.pdf_file_path = artical_path
        self.xml_path = _generate_xml_path(artical_path)
        self.grobid_server = grobid_server
        self.pdf_to_xml()

    def pdf_to_xml(self):
        """
        Convert the PDF file to XML using Grobid.

        @return: None
        """
        if not self._check_grobid_running():
            return

        client = GrobidClient(grobid_server=self.grobid_server,
                              batch_size=1000,
                              sleep_time=5,
                              timeout=1200,
                              coordinates=["persName", "figure", "ref", "biblStruct", "formula", "s", "note", "title"])

        req = client.process_pdf(
            service="processFulltextDocument",
            pdf_file=self.pdf_file_path,
            generateIDs=True,
            consolidate_header=True,
            consolidate_citations=True,
            include_raw_citations=True,
            include_raw_affiliations=True,
            tei_coordinates=True,
            segment_sentences=True
        )
        with open(self.xml_path, "w", encoding="utf-8") as file:
            file.write(req[2])

    def _check_grobid_running(self):
        """
        Check if the Grobid service is running by making a request to the specified URL using curl.

        @return: bool: True if the Grobid service is running, False otherwise.
        """
        try:
            # Use curl to make a request to the Grobid service and capture the HTTP status code
            result = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', self.grobid_server],
                                    capture_output=True,
                                    text=True)
            status_code = result.stdout.strip()

            # Check if the status code is 200 (OK)
            if status_code == "200":
                print("Grobid service is running.")
                return True
            # If the status code is not 200, the service might not be running
            else:
                print(f"Grobid service might not be running. HTTP status code: {status_code}")
                return False
        except subprocess.CalledProcessError as e:
            # If an error occurs, the service is not running
            print(f"Failed to check Grobid service with curl: {e}")
            return False
