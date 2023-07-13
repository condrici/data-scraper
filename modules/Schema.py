from marshmallow_jsonapi import Schema, fields


class PriceSchema(Schema):
    id = fields.Str(dump_only=True)
    price = fields.Str()
    whole_price = fields.Str()

    class Meta:
        type_ = "price"

    def create(self):
        return self
