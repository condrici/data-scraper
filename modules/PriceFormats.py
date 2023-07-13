import re
from abc import abstractmethod

from modules.Schema import PriceSchema


class PriceFormat:

    @abstractmethod
    def get_price(self, uri: str) -> PriceSchema | ValueError:
        pass

    @abstractmethod
    def __validate(self, price: str) -> bool | ValueError:
        pass


class CommaDecimalsDotThousandsPriceFormat(PriceFormat):
    __regex: str = "^[0-9]{1,3}([.]{1}[0-9]{3})*([,]{1}[0-9]+){0,1}$"

    """ Price string is validated and converted 
    into a standardized JSON API schema 
    """

    def get_price(self, price_string: str) -> PriceSchema:
        self.__validate(price_string)

        price_schema = PriceSchema()
        price_schema.price = price_string
        price_schema.whole_price = int(price_string.split(',')[0])

        return price_schema

    def __validate(self, price: str) -> bool | ValueError:
        if not re.search(self.__regex, price):
            raise ValueError(
                "Price doesn't have expected format "
                "format_comma_decimal_dot_thousands"
            )

        return True