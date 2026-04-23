from peewee import *
from datetime import datetime

db = SqliteDatabase('sqlite3.db')

class Message(Model):
    create_at = DateField(default=datetime.now)
    text = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Message])