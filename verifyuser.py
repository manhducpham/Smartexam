from mongoengine import Document, StringField, ListField

class Verifyuser(Document):
    user_id = StringField()
    full_name = StringField()
    email = StringField()
    password = StringField()
    code = StringField(default = None)   