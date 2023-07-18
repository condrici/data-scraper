import unittest
from modules.PriceFormats import PriceFormatFactory, PriceFormat, \
    CommaDecimalsDotThousandsPriceFormat, FORMAT_COMMA_DECIMALS_DOT_THOUSANDS


class TestPriceFormatFactory(unittest.TestCase):

    def test_create(self) -> None:
        with self.assertRaises(ValueError) as context:
            PriceFormatFactory().create('nonexistent_price_format')

        # Test with nonexistent format

        self.assertEqual('Unknown price format', str(context.exception))

        # Test with existing format

        self.assertIsInstance(
            PriceFormatFactory().create(FORMAT_COMMA_DECIMALS_DOT_THOUSANDS),
            PriceFormat
        )


class TestCommaDecimalsDotThousandsPriceFormat(unittest.TestCase):

    PRICE_SCHEMA_MANDATORY_ATTRIBUTES = ['price', 'whole_price']

    def test_get_price(self) -> None:
        self.__xtest_prices_with_incorrect_format()
        self.__xtest_prices_with_correct_format()

    def __xtest_prices_with_incorrect_format(self):
        with self.assertRaises(ValueError) as context:
            price_format = CommaDecimalsDotThousandsPriceFormat()
            for price_string in self.__get_invalid_value_formats():

                # Test exception type

                self.assertRaises(
                    ValueError,
                    price_format.get_price(price_string)
                )

        # Test exception message

        self.assertEqual(
            "Price doesn't have expected format format_comma_decimal_dot_thousands",
            str(context.exception)
        )

    def __xtest_prices_with_correct_format(self):
        price_format = CommaDecimalsDotThousandsPriceFormat()

        for price_string in self.__get_valid_value_formats():
            price_schema = price_format.get_price(price_string)

            # Test mandatory attributes
            self.assertEqual(hasattr(price_schema, 'price'), True)
            self.assertEqual(hasattr(price_schema, 'whole_price'), True)

            # Test mandatory attribute values

            self.assertEqual(price_schema.price, price_string)

    def __get_invalid_value_formats(self):
        return [
            ',', '.', '#', '!', '...', '~', '@', '-', '?', '%', '"',
            '.0', ',0', '.000', ',000',
            '1000', '1000,' '1000.', '1000.,'
            '1.0', '1.00', '1,0,0', '1.1.1', '1,00',
            '100,000,000', '100,000.000', '100.000,000,000'
        ]

    def __get_valid_value_formats(self):
        return [
            '1', '10', '100',                     # whole numbers
            '1.000', '100.000', '100.000.000',    # with thousands
            '100,10', '100,20', '100.000.000,20'  # with decimals
        ]
