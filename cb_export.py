import argparse
import json

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery


def load_all(bucket):
    q = N1QLQuery('SELECT META(default).id, * from default')
    data = {}
    for row in bucket.n1ql_query(q):
        data[row['id']] = row['default']
    return data


def load_by_view(bucket, design_document):
    result = bucket.query(design_document, "all", reduce=False, include_docs=True)
    data = {}
    for row in result:
        data[row.key] = row.doc.value


def store_data(file_name, data):
    with open(file_name, 'w') as data_file:
        json.dump(data, data_file, indent=2)

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", default="localhost",
                    help="specify server host")
parser.add_argument("-b", "--bucket", default="default",
                    help="bucket name")
parser.add_argument("-v", "--view",
                    help="load data based on specific view, use design_document/view_name format")
args = parser.parse_args()

bucket = Bucket("couchbase://" + args.server + "/" + args.bucket)

data = load_all(bucket)
store_data('data.json', data)
