from marshmallow_sqlalchemy import ModelConverter
import sqlalchemy
from marshmallow_enum.marshmallow_enum import EnumField


class EnumConverter(ModelConverter):
    SQLA_TYPE_MAPPING = dict(
        list(ModelConverter.SQLA_TYPE_MAPPING.items()) +
        [(sqlalchemy.Enum, EnumField)]
    )


class EnumMeta:
    model_converter = EnumConverter
