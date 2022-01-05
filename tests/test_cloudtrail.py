from cloudtrail import __version__
from cloudtrail.s3 import doS3


def test_version():
    assert __version__ == '0.1.0'
