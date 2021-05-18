from mongoengine import (
    Document,
    DateTimeField,
    StringField,
    IntField)

class Register(Document):
    create_date = DateTimeField()
    aplication_name = StringField()
    code = IntField()
    message = StringField()