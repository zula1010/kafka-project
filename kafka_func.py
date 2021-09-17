import base64
import io
import json

import avro
import avro.schema
from avro.io import DatumReader, DatumWriter


TOPIC_NAME = 'items'
KAFKA_SERVER = 'localhost:9092'


schema = avro.schema.parse(open("schema.avsc", "rb").read())
avro_reader = avro.io.DatumReader(schema)
avro_writer = avro.io.DatumWriter(schema)


def decode(msg_):
	msg = base64.b64decode(msg_)
	bytes_reader = io.BytesIO(msg)
	decoder = avro.io.BinaryDecoder(bytes_reader)
	decoded_data = avro_reader.read(decoder)
	data = json.loads(decoded_data['msg'])
	return data


def encode(msg):
	bytes_writer = io.BytesIO()
	encoder = avro.io.BinaryEncoder(bytes_writer)
	avro_writer.write({'msg': msg}, encoder)
	raw_bytes = bytes_writer.getvalue()
	return base64.b64encode(raw_bytes)
