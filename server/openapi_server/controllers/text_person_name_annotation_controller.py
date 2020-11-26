import connexion
import pandas as pd
import re

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.text_person_name_annotation_request import TextPersonNameAnnotationRequest  # noqa: E501
from openapi_server.models.text_person_name_annotation import TextPersonNameAnnotation  # noqa: E501
from openapi_server.models.text_person_name_annotations import TextPersonNameAnnotations  # noqa: E501


class Data:
    def __init__(self):
        # All first names (1974 to 2019) from https://www.nrscotland.gov.uk
        firstnames_df = pd.read_csv("data/firstnames.csv")
        self._firstnames = firstnames_df['firstname'].str.lower().unique().tolist()  # noqa: E501

        # Top 1000 last names from census.gov (18-10-2020)
        # https://www.census.gov/topics/population/genealogy/data/2000_surnames.html
        lastnames_df = pd.read_csv("data/lastnames.csv")
        self._lastnames = lastnames_df['lastname'].str.lower().unique().tolist()  # noqa: E501


data = Data()


def create_text_person_name_annotations(note=None):  # noqa: E501
    """Annotate person names in a clinical note

    Return the person name annotations found in a clinical note # noqa: E501

    :param note:
    :type note: dict | bytes

    :rtype: TextPersonNameAnnotations
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            annotation_request = TextPersonNameAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
            note = annotation_request._note  # noqa: E501
            annotations = []
            for name in data._firstnames:
                matches = re.finditer(
                    r'\b({})\b'.format(name), note._text, re.IGNORECASE)
                for match in matches:
                    annotations.append(TextPersonNameAnnotation(
                        start=match.start(),
                        length=len(match[0]),
                        text=match[0],
                        confidence=95
                    ))
            for name in data._lastnames:
                matches = re.finditer(
                    r'\b({})\b'.format(name), note._text, re.IGNORECASE)
                for match in matches:
                    annotations.append(TextPersonNameAnnotation(
                        start=match.start(),
                        length=len(match[0]),
                        text=match[0],
                        confidence=95
                    ))

            res = TextPersonNameAnnotations(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status
