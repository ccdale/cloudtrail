from pprint import pprint
import sys

import boto3

from cloudtrail import errorNotify

def doS3():
    try:
        pass
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)

def s3client():
    try:
        return boto3.client("s3")
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)

def listBuckets():
    try:
        s3 = s3client()
        buckets = s3.list_buckets()
        getObjects(s3)
        # for bucket in buckets["Buckets"]:
            # print(bucket["Name"])
        # pprint(buckets)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)

def getObjects(s3):
    try:
        objs = s3.list_objects_v2(Bucket="bucketname")
        for obj in objs["Contents"]:
            print(f'{obj["Size"]:>6} {obj["Key"]}')
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)

if __name__ == "__main__":
    listBuckets()
