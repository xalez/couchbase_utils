import json

from couchbase.bucket import Bucket

bucket = Bucket("couchbase://localhost/default")

with open('data.json') as data_file:
    data = json.load(data_file)

for key, value in data.iteritems():
    bucket.upsert(key, value)