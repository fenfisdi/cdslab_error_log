from mongoengine import (
    DateTimeField,
    IntField,
    StringField,
    UUIDField
)

from .base import BaseDocument


class Register(BaseDocument):
    uuid = UUIDField(binary=False, unique=True, required=True)
    reported_at = DateTimeField()
    application = StringField()
    code = IntField()
    message = StringField()
