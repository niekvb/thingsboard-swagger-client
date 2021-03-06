# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import thingsboard_client
from api.entity_relation_controller_api import EntityRelationControllerApi  # noqa: E501
from thingsboard_client.rest import ApiException


class TestEntityRelationControllerApi(unittest.TestCase):
    """EntityRelationControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.entity_relation_controller_api.EntityRelationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_relation_using_delete(self):
        """Test case for delete_relation_using_delete

        deleteRelation  # noqa: E501
        """
        pass

    def test_delete_relations_using_delete(self):
        """Test case for delete_relations_using_delete

        deleteRelations  # noqa: E501
        """
        pass

    def test_find_by_from_using_get(self):
        """Test case for find_by_from_using_get

        findByFrom  # noqa: E501
        """
        pass

    def test_find_by_from_using_get1(self):
        """Test case for find_by_from_using_get1

        findByFrom  # noqa: E501
        """
        pass

    def test_find_by_query_using_post2(self):
        """Test case for find_by_query_using_post2

        findByQuery  # noqa: E501
        """
        pass

    def test_find_by_to_using_get(self):
        """Test case for find_by_to_using_get

        findByTo  # noqa: E501
        """
        pass

    def test_find_by_to_using_get1(self):
        """Test case for find_by_to_using_get1

        findByTo  # noqa: E501
        """
        pass

    def test_find_info_by_from_using_get(self):
        """Test case for find_info_by_from_using_get

        findInfoByFrom  # noqa: E501
        """
        pass

    def test_find_info_by_query_using_post(self):
        """Test case for find_info_by_query_using_post

        findInfoByQuery  # noqa: E501
        """
        pass

    def test_find_info_by_to_using_get(self):
        """Test case for find_info_by_to_using_get

        findInfoByTo  # noqa: E501
        """
        pass

    def test_get_relation_using_get(self):
        """Test case for get_relation_using_get

        getRelation  # noqa: E501
        """
        pass

    def test_save_relation_using_post(self):
        """Test case for save_relation_using_post

        saveRelation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
