from pprint import pprint
from boto.s3.connection import S3Connection
from os.path import expanduser
import os

home = expanduser("~")
LOCAL_PATH = home + '/local_folder/'

#pprint("CONTENT will be stored here:" + LOCAL_PATH)

conn = S3Connection()
bucket = conn.get_bucket('bucket-name')
for key in bucket.list():
    try:
        filename = str(key.key)
        dirname = os.path.dirname(filename)

        pprint(filename)

    except:
        pprint(key.name + ":" + "FAILED")
        raise e
