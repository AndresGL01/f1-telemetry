from peewee import (
    SqliteDatabase,
    Model,
    UUIDField,
    TextField,
    IntegerField
)

db = SqliteDatabase('../logs.db')


class Packet(Model):
    id = UUIDField(primary_key=True)
    payload = TextField()
    packet_id = IntegerField()
    timestamp = IntegerField()

    class Meta:
        database = db
