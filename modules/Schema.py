from __future__ import annotations

from marshmallow_jsonapi import Schema, fields


class PriceSchema(Schema):
    id = fields.Str(dump_only=True)
    price = fields.Str()
    whole_price = fields.Str()

    class Meta:
        type_ = "price"

    def create(self) -> PriceSchema:
        return self
