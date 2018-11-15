from mongoengine import Document, StringField, ListField, DictField

class User(Document):
    user_id = StringField()
    full_name = StringField()
    email = StringField()
    password = StringField()
    banks = DictField(default = None)   