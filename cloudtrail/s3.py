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
        # getObjects(s3, buckets["Buckets"][0]["Name"])
        getObjects(s3, "cloudtrail-secadmin-146be99826c04fd80739c629383bffb8")
        # for bucket in buckets["Buckets"]:
        # print(bucket["Name"])
        # pprint(buckets)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def getObjects(s3, bucketname):
    try:
        # prefix = "AWSLogs/211437271944/CloudTrail/eu-west-1/2018/02/01/211437271944_CloudTrail_eu-west-1_20180201T01"
        prefix = "AWSLogs/442759342293/CloudTrail/eu-west-1/2022/01/10/442759342293_CloudTrail_eu-west-1_20220110T012"
        print(bucketname)
        objs = s3.list_objects_v2(Bucket=bucketname, Prefix=prefix)
        cn = 0
        if "Contents" in objs:
            for obj in objs["Contents"]:
                print(f'{obj["Size"]:>6} {obj["Key"]}')
                cn += 1
        print(cn)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


if __name__ == "__main__":
    listBuckets()
