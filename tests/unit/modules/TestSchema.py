import unittest

from marshmallow_jsonapi import Schema

from modules.Schema import PriceSchema


class TestSchema(unittest.TestCase):

    def test_create(self):
        price_schema = PriceSchema()
        price_schema.price = '100,10'
        price_schema.whole_price = '100'

        self.assertIsInstance(price_schema, PriceSchema)
        self.assertIsInstance(price_schema, Schema)

        self.assertEqual(price_schema.price, '100,10')
        self.assertEqual(price_schema.whole_price, '100')

        total_class_attributes = len(price_schema.__dict__['declared_fields'])
        self.assertEqual(total_class_attributes, 3)


