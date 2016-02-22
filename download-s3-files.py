from pprint import pprint
from os.path import expanduser
import os
import boto3

home = expanduser("~")
LOCAL_PATH = home + '/bucket/'

s3 = boto3.resource('s3')
bucket = s3.Bucket('bucket-name')
for object_summary in bucket.objects.all():
    try:
        filename = LOCAL_PATH + str(object_summary.key)
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            #pprint("CREATING LOCATION: " + dirname)
            os.makedirs(dirname)

        if not os.path.isdir(filename):
            res = bucket.download_file(object_summary.key, filename)
    except:
        pprint(object_summary.key.name + ":" + "FAILED")
        raise e
