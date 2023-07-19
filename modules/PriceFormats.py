import re
from abc import abstractmethod

from modules.Schema import PriceSchema

FORMAT_COMMA_DECIMALS_DOT_THOUSANDS = "comma_decimals_dot_thousands"


class PriceFormat:

    @property
    @abstractmethod
    def __regex(self) -> str:
        pass

    @abstractmethod
    def get_price(self, price: str) -> PriceSchema | ValueError:
        pass

    """ Validation has to be used in the get_price implementation """
    def _validate(self, price: str, regex) -> bool | ValueError:
        if not re.search(regex, price):
            raise ValueError(
                "Price doesn't have expected format "
                "format_comma_decimal_dot_thousands"
            )

        return True


class CommaDecimalsDotThousandsPriceFormat(PriceFormat):
    __regex: str = "^[0-9]{1,3}([.]{1}[0-9]{3})*([,]{1}[0-9]+){0,1}$"

    """ Price string is validated and converted 
    into a standardized JSON API schema 
    """

    def get_price(self, price_string: str) -> PriceSchema | ValueError:
        self._validate(price_string, self.__regex)

        price_schema = PriceSchema()
        price_schema.price = price_string
        price_schema.whole_price = price_string.split(',')[0]

        return price_schema


class PriceFormatFactory:
    def create(self, price_format: str) -> PriceFormat:
        if price_format == FORMAT_COMMA_DECIMALS_DOT_THOUSANDS:
            return CommaDecimalsDotThousandsPriceFormat()

        raise ValueError("Unknown price format")
