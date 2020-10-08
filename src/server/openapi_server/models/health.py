# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import utility


class Health(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (
    https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status=None):  # noqa: E501
        """Health - a model defined in OpenAPI

        :param status: The status of this Health.  # noqa: E501
        :type status: str
        """
        self.openapi_types = {
            'status': str
        }

        self.attribute_map = {
            'status': 'status'
        }

        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Health':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Health of this Health.  # noqa: E501
        :rtype: Health
        """
        return utility.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this Health.

        Health status  # noqa: E501

        :return: The status of this Health.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Health.

        Health status  # noqa: E501

        :param status: The status of this Health.
        :type status: str
        """
        allowed_values = ["pass", "warn"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
