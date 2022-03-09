# Cloud Trail Search
(eventually) A search utility for AWS Cloud Trails

## Testing

* use TDD
Next week we will be concentrating on testing
we definitely need  to test the objectFilter

## S3

* list S3
    * create boto3 s3 client - DONE
    * create a bucket lister - DONE
    * create a naive file lister - DONE
    * investigate server side filtering - DONE
    * investigate generators - DONE
    * create a generator for file listing - DONE
    * filter more (endswith, contains) - DONE - REQUIRES TESTING
* download specific files from S3
* create filters for
    * name
    * timestamp
    * timestamp within name
    * size
* filter S3 listing
* download filtered files

## Cloud Trail
* JSON => python objects
* Extraction of specific fields
* search strategies
    * incremental
    * divide and conquer (start in the middle and work out)
    * parallel blocks
