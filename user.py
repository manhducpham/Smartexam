from mongoengine import Document, StringField

class User(Document):
    user_id = StringField()
    email = StringField()
    password = StringField()   