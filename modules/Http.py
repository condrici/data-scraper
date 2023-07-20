""" Decorator for the requests module """
from typing import Optional, Dict

from requests import api
from requests.models import Response

DEFAULT_USER_AGENT = 'Mozilla/5.0 ' \
                     '(Macintosh; Intel Mac OS X 13.4; rv:109.0) ' \
                     'Gecko/20100101 Firefox/115.0'


class HttpRequestSettings:
    def __init__(
            self,
            use_default_user_agent: Optional[bool] = False
    ):
        self.__use_default_user_agent = use_default_user_agent

    def get_use_default_user_agent(self):
        return self.__use_default_user_agent


class HttpRequest:

    __request: api
    __request_settings: HttpRequestSettings

    def __init__(
        self,
        request_api: api,
        request_settings: HttpRequestSettings
    ):
        self.__request = request_api
        self.__request_settings = request_settings

    """ HTTP GET REQUEST """

    def get(
            self,
            url: str,                                 # Request URL
            params: Optional[Dict] = None,            # Query params
            **kwargs: Optional[Dict]                  # Optionals
    ) -> Response:

        overwritten_kwargs = self.__update_empty_kwargs_with_default_settings(
            decorator_settings=self.__request_settings, **kwargs
        )

        return self.__request.get(
            url=url,
            params=params,
            **overwritten_kwargs
        )

    """ Add decorator's default settings, if they are not sent via module """

    def __update_empty_kwargs_with_default_settings(
        self,
        decorator_settings: HttpRequestSettings,
        **kwargs: Dict
    ) -> Optional[Dict]:
        if decorator_settings.get_use_default_user_agent():
            kwargs = self.__add_default_http_headers(
                'user-agent', kwargs
            )

        return kwargs

    def __add_default_http_headers(
            self,
            http_header_name: str,
            module_settings: Dict
    ) -> Dict:
        if 'headers' in module_settings:
            if http_header_name in module_settings['headers']:
                return module_settings
            else:
                module_settings['headers'][http_header_name] = \
                    DEFAULT_USER_AGENT
        else:
            module_settings['headers'] = {
                http_header_name: DEFAULT_USER_AGENT
            }

        return module_settings
