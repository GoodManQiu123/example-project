"""
Overview:
This module provides a comprehensive XML parsing utility specifically designed for academic articles. Utilizing the
ElementTree XML API, it defines a Parser class that extracts structured data from XML documents, including article
metadata, content, authors, and references. Helper functions facilitate text extraction using XPath queries and
namespaces, handling various text structures within XML. The module also incorporates external tools like Anystyle CLI
to parse bibliographic references into structured data. The extracted information is mapped onto custom data classes,
providing a structured and standardized representation of articles suitable for further processing or storage in
academic databases, content management systems, or for bibliometric analysis.

Key Components:
- _find_text_single and _find_text_paragraph: Helper functions for extracting text based on XPath queries.
- Parser class: Core utility for parsing XML documents, capable of extracting comprehensive article data.
- Integration with Anystyle CLI for advanced reference parsing, converting raw bibliographic data into structured
  formats.
- Use of Python data classes for standardized representation of articles, metadata, content, authors, and references.

Usage:
This module is ideal for projects involving the extraction, analysis, and management of scholarly article data from
XML documents, such as digital libraries, academic research databases, and bibliometric analysis tools.
"""

import io
import json
import subprocess
import tempfile
from .types import Metadata, Content, ArticleObject, Reference, Author
from typing import AnyStr, Dict, List, Optional
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import re


def _find_text_single(node: Element, xPath: AnyStr, namespaces: Dict) -> Optional[AnyStr]:
    """
    Helper functions for parsing XML for metadata

    @param node: The node to search from
    @param xPath: The xPath to search for
    @param namespaces: The namespaces to use
    @return: The text of the element found, or None
    @note: This function can only be used to parse the single text
    """

    element = node.find(xPath, namespaces=namespaces)
    return element.text if element is not None else None


def _find_text_paragraph(node: Element, xPath: AnyStr, namespaces: Dict) -> Optional[AnyStr]:
    """
    Helper functions for parsing XML for metadata

    @param node: The node to search from
    @param xPath: The xPath to search for
    @param namespaces: The namespaces to use
    @return: The text of the element found, or None
    @note: This function can only be used to parse the text paragraph
    """
    # Find all <div> elements specified by the XPath
    div_elements = node.findall(xPath, namespaces=namespaces)
    paragraphs_text = []

    for div in div_elements:
        # Check if this <div> contains a <head>. Skip it if yes.
        if div.find('.//tei:head', namespaces=namespaces) is None:
            # For each <div> without a <head>, concatenate the text of all <p> elements
            for p in div.findall('.//tei:p', namespaces=namespaces):
                text = " ".join(p.itertext())
                if text:
                    paragraphs_text.append(text.strip())

    # Return concatenated text of all paragraphs, separated by a space
    return " ".join(paragraphs_text) if paragraphs_text else None


def _find_words_list(node: Element, xPath: AnyStr, namespaces: Dict) -> Optional[List[AnyStr]]:
    """
    Helper functions for parsing XML for list of words

    @param node: The node to search from
    @param xPath: The xPath to search for
    @param namespaces: The namespaces to use
    @return: The text of the element found, or None
    @note: This function can only be used to parse the list of words
    """
    elements = node.findall(xPath, namespaces=namespaces)
    return [element.text for element in elements] if elements is not None else None


class Parser(object):
    """
    The Parser class is used to parse the XML file into an ArticleObject.
    """
    def __init__(self, xml_path: AnyStr):
        """
        Initialize the Parser object with the path to the XML file.

        @param xml_path: The path to the XML file.
        @return: None
        """
        self.xml_path = xml_path
        self.xml_namespace = "http://www.w3.org/XML/1998/namespace"
        self.tei_namespace = "http://www.tei-c.org/ns/1.0"
        self.etree = self._string_to_tree()
        self.article = self.parse_article()

    def parse_article(self):
        """
        Parse the XML file into an ArticleObject.

        @return: ArticleObject: The parsed article object.
        @note: This function is the main function to parse the XML file into an ArticleObject.
        """
        return ArticleObject(
            metadata=self._parse_metadata(),
            content=self._parse_content(),
            references=self._parse_reference(),
            authors=self._parse_author
        )

    def _string_to_tree(self) -> ET.ElementTree:
        """
        Parse the XML string into an ElementTree object.

        @return: ET.ElementTree: The ElementTree object.
        @note: This function is used to parse the XML string into an ElementTree object.
        """
        with open(self.xml_path, 'r') as xml_file:
            content = xml_file.read()
        if isinstance(content, str):
            return ET.parse(io.StringIO(content))
        else:
            raise TypeError(f"Expected string, got {type(content)}")

    def _parse_metadata(self) -> Metadata:
        """
         Parse the metadata of the article.

         @return: Metadata: The metadata of the article.
         """
        tei_root = self.etree.getroot()
        title = _find_text_single(tei_root,
                                  './/tei:titleStmt/tei:title[@level="a"]',
                                  namespaces={'tei': self.tei_namespace})
        doi = _find_text_single(tei_root,
                                './/tei:sourceDesc/tei:biblStruct/tei:idno[@type="DOI"]',
                                namespaces={'tei': self.tei_namespace})
        publisher = _find_text_single(tei_root,
                                      './/tei:publicationStmt/tei:publisher',
                                      namespaces={'tei': self.tei_namespace})
        published_date = _find_text_single(tei_root,
                                           './/tei:publicationStmt/tei:date[@type="published"]',
                                           namespaces={'tei': self.tei_namespace})
        journal = _find_text_single(tei_root,
                                    './/tei:sourceDesc/tei:biblStruct/tei:monogr/tei:title[@level="j"]',
                                    namespaces={'tei': self.tei_namespace})
        return Metadata(
            title=title,
            doi=doi,
            publisher=publisher,
            journal=journal,
            published_date=published_date
        )

    def _parse_content(self) -> Content:
        """
        Parse the content of the article.

        @return: Content: The content of the article.
        """
        tei_root = self.etree.getroot()
        abstract = _find_text_paragraph(tei_root,
                                        './/tei:profileDesc/tei:abstract/tei:div',
                                        namespaces={'tei': self.tei_namespace})
        keywords = _find_words_list(tei_root,
                                    './/tei:profileDesc/tei:textClass/tei:keywords/tei:term',
                                    namespaces={'tei': self.tei_namespace})
        return Content(
            abstract=abstract,
            keywords=keywords
        )

    @property
    def _parse_author(self) -> List[Author]:
        """
        Parse the XML string into an ElementTree object.

        @return: List[Author]: The list of authors of the article.
        """
        # Parse the XML string into an ElementTree object.
        tree = self.etree.getroot()
        authors = []

        # Find all author elements in the XML.
        author_elements = tree.findall('.//tei:sourceDesc/tei:biblStruct/tei:analytic/tei:author',
                                       namespaces={'tei': self.tei_namespace})

        for author_elem in author_elements:
            # Extract forenames (including middle names) and surnames for each author.
            forenames = author_elem.findall('.//tei:persName/tei:forename', namespaces={'tei': self.tei_namespace})
            # Remove numbers and subsequent spaces, then remove extra spaces
            forename_texts = [' '.join(re.sub(r'\s+', ' ', re.sub(r'\d+\s*', '', forename.text)).split()) for forename
                              in forenames if forename.text]
            surname_element = author_elem.find('.//tei:persName/tei:surname', namespaces={'tei': self.tei_namespace})
            surname = surname_element.text if surname_element is not None else None

            # Combine forenames and surname into a full name and remove leading/trailing spaces
            full_name = ' '.join([name for name in forename_texts + [surname] if name]).strip()

            # Find affiliation and email elements, if available
            affiliation_element = author_elem.find('.//tei:affiliation/tei:orgName',
                                                   namespaces={'tei': self.tei_namespace})
            affiliation = affiliation_element.text if affiliation_element is not None else None
            email_element = author_elem.find('.//tei:email', namespaces={'tei': self.tei_namespace})
            email = email_element.text if email_element is not None else None

            # Create an Author dataclass instance and add it to the list
            if full_name:  # This checks if full_name is not None and not an empty string
                authors.append(Author(name=full_name, affiliation=affiliation, email=email))

        return authors

    def _find_raw_reference(self, ns=None):
        """
        Extract raw references from the XML document.

        @param ns: The namespace dictionary.
        @return: List[str]: The list of raw references.
        """
        # print("extracting raw reference")
        if ns is None:
            ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        raw_references = []
        for note in root.findall('.//tei:note[@type="raw_reference"]', ns):
            ref = note.text
            ref = ref.replace('Ű', '-')
            ref = ref.replace('&apos;', "'")
            cleaned_ref = re.sub(r'-\s*', '-', ref)
            if cleaned_ref != "REFERENCES":
                raw_references.append(cleaned_ref)
        # print(len(raw_references))
        # print(raw_references[0])
        return raw_references

    def _store_references(self, raw_references):
        """
        Store the references in a temporary file and call Anystyle CLI to parse them.

        @param raw_references: The list of raw references.
        @return: List[Dict]: The list of parsed references.
        """
        # Write the references to a temporary file
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            # Each reference on a new line
            tmp.write('\n'.join(raw_references))
            tmp_path = tmp.name

        # Define the command to call Anystyle with the appropriate options
        # This command assumes Anystyle CLI is installed and `anystyle` is in your PATH
        cmd = ['anystyle', '-f', 'json', 'parse', tmp_path]

        try:
            # Run the Anystyle command （synchronously）
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Parse the JSON output
            parsed_references = json.loads(result.stdout)
            return parsed_references

        except subprocess.CalledProcessError as e:
            # Handle errors in the subprocess
            print(f"An error occurred while running Anystyle: {e}")
            return None

        finally:
            # Remove the temporary file
            subprocess.run(['rm', tmp_path])

    def _parse_reference(self):
        """
        Parse the references from the XML document.

        @return: List[Reference]: The list of parsed references.
        """
        raw_references = self._find_raw_reference()
        stored_json_references = self._store_references(raw_references)
        if not stored_json_references:
            return []
        return [
            Reference(
                authors=ref.get('author', []),
                title=''.join(ref.get('title', '')) if isinstance(ref.get('title'), list) else ref.get('title', ''),
                type=ref.get('type', ''),
                container_title=ref.get('container-title', ''),
                doi=''.join(ref.get('doi', '')) if isinstance(ref.get('doi'), list) else ref.get('doi', ''),
                published_date=ref.get('date', [])[0] if ref.get('date') else ''
            )
            for ref in stored_json_references
        ]
