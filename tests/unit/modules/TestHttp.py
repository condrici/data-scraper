import unittest
from unittest.mock import patch, MagicMock
from requests import Response

from modules.Http import HttpRequestSettings, HttpRequest, DEFAULT_USER_AGENT


class TestHttpRequestSettings(unittest.TestCase):

    def test_get_use_default_user_agent(self) -> None:
        http_request_settings = HttpRequestSettings(
            use_default_user_agent=True
        )
        self.assertIsInstance(http_request_settings, HttpRequestSettings)
        self.assertEqual(
            http_request_settings.get_use_default_user_agent(),
            True
        )


class TestHttpRequest(unittest.TestCase):

    def test_get_with_http_headers_user_agent(self) -> None:
        request_api_mock = self.__get_mock_request_api()
        http_request = self.__get_requset_decorator(request_api_mock)

        # Filled headers= with user-agent
        # When this happens, the settings set in headers=
        # will take precedence

        http_response = http_request.get(
            'http://example.com',
            None,
            headers={'user-agent': 'Mozilla'}
        )

        self.assertIsInstance(http_response, Response)
        request_api_mock.get.assert_called_once_with(
            url='http://example.com',
            headers={'user-agent': 'Mozilla'},
            params=None
        )

    def test_get_with_empty_http_headers(self) -> None:
        request_api_mock = self.__get_mock_request_api()
        http_request = self.__get_requset_decorator(request_api_mock)

        # Empty headers={}
        # When this happens, the settings defined in HttpRequestSettings,
        # like the user-agent, will take precedence

        http_response = http_request.get(
            'http://example.com',
            None,
            headers={}
        )

        request_api_mock.get.assert_called_once_with(
            url='http://example.com',
            headers={'user-agent': DEFAULT_USER_AGENT},
            params=None
        )
        self.assertIsInstance(http_response, Response)

    def test_get_with_unset_http_headers(self) -> None:
        request_api_mock = self.__get_mock_request_api()
        http_request = self.__get_requset_decorator(request_api_mock)

        # Undefined headers=
        # When this happens, the settings defined in HttpRequestSettings,
        # like the user-agent, will take precedence

        http_response = http_request.get(
            'http://example.com',
            None,
        )

        request_api_mock.get.assert_called_once_with(
            url='http://example.com',
            headers={'user-agent': DEFAULT_USER_AGENT},
            params=None
        )
        self.assertIsInstance(http_response, Response)

    def __get_requset_decorator(self, request_api_mock) -> HttpRequest:
        request_settings = HttpRequestSettings(use_default_user_agent=True)
        return HttpRequest(request_api_mock, request_settings)

    def __get_mock_request_api(self) -> MagicMock:
        request_api = MagicMock()
        request_api.get.return_value = Response()

        return request_api
