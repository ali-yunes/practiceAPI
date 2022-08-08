# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FileBody1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None, title: str=None, description: str=None, file: str=None):  # noqa: E501
        """FileBody1 - a model defined in Swagger

        :param username: The username of this FileBody1.  # noqa: E501
        :type username: str
        :param title: The title of this FileBody1.  # noqa: E501
        :type title: str
        :param description: The description of this FileBody1.  # noqa: E501
        :type description: str
        :param file: The file of this FileBody1.  # noqa: E501
        :type file: str
        """
        self.swagger_types = {
            'username': str,
            'title': str,
            'description': str,
            'file': str
        }

        self.attribute_map = {
            'username': 'username',
            'title': 'title',
            'description': 'description',
            'file': 'file'
        }
        self._username = username
        self._title = title
        self._description = description
        self._file = file

    @classmethod
    def from_dict(cls, dikt) -> 'FileBody1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The file_body_1 of this FileBody1.  # noqa: E501
        :rtype: FileBody1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this FileBody1.


        :return: The username of this FileBody1.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this FileBody1.


        :param username: The username of this FileBody1.
        :type username: str
        """

        self._username = username

    @property
    def title(self) -> str:
        """Gets the title of this FileBody1.


        :return: The title of this FileBody1.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this FileBody1.


        :param title: The title of this FileBody1.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this FileBody1.


        :return: The description of this FileBody1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this FileBody1.


        :param description: The description of this FileBody1.
        :type description: str
        """

        self._description = description

    @property
    def file(self) -> str:
        """Gets the file of this FileBody1.


        :return: The file of this FileBody1.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file: str):
        """Sets the file of this FileBody1.


        :param file: The file of this FileBody1.
        :type file: str
        """

        self._file = file