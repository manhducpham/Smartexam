import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds159293.mlab.com:59293/se_users

host = "ds159293.mlab.com"
port = 59293
db_name = "se_users"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())