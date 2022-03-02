import sys

import boto3

from cloudtrail import errorNotify
from cloudtrail.s3 import s3client


def getBucketListing():
    try:
        s3 = s3client()
        buckets = s3.list_buckets()
        for bucket in buckets["Buckets"]:
            yield bucket
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def objectFilter(objname, filters=[]):
    try:
        score = 0
        if filters:
            for filt in filters:
                if filt in objname:
                    score += 1
            return True if score == len(filters) else False
        return True
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise

def getObjectList(
    bucket, prefix="", filters=[], postfix="", pagesize=1000, maxpages=None
):
    try:
        s3 = s3client()
        pages = 0
        kwargs = {"Bucket": bucket, "MaxKeys": pagesize}
        if prefix != "":
            kwargs["Prefix"] = prefix
        finished = False
        while not finished:
            res = s3.list_objects_v2(**kwargs)
            if "Contents" in res:
                contents = res["Contents"]
                for obj in contents:
                    if objectFilter(obj["Key"], filters):
                        if not postfix:
                            yield obj
                        elif postfix and obj["Key"].endswith(postfix):
                            yield obj
            if "NextContinuationToken" in res:
                kwargs["ContinuationToken"] = res["NextContinuationToken"]
            else:
                finished = True
            pages += 1
            if maxpages is not None and pages >= maxpages:
                finished = True
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def printBucketList():
    try:
        for bkt in getBucketListing():
            print(f"{bkt['Name']}")
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def printObjectList():
    try:
        for obj in getObjectList(
            "cloudtrail-secadmin-146be99826c04fd80739c629383bffb8",
            pagesize=10,
            maxpages=2,
        ):
            print(f"{obj['Key']}")
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


if __name__ == "__main__":
    # printBucketList()
    printObjectList()
