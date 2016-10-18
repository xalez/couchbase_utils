import argparse
import json

from couchbase.bucket import Bucket

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", default="localhost",
                    help="specify server host")
parser.add_argument("-b", "--bucket", default="default",
                    help="bucket name")
parser.add_argument("file_name", nargs='?', default="data.json",
                    help="Name of file which contains data for import")
args = parser.parse_args()

bucket = Bucket("couchbase://" + args.server + "/" + args.bucket)

with open(args.file_name) as data_file:
    data = json.load(data_file)

for key, value in data.iteritems():
    bucket.upsert(key, value)
