# boa-vista-test-iac
# This repo contains the Code for create an IaC with Redshift cluster, S3 and IAM Roles, used to create the ingestion based on the files that come on the S3 bucket, and the code to load the files to the Redshift tables.

Let's get started with this code

## Table of Contents

1. [Quick start](#quick-start)
1. [Prepare the environment](#Prepare-the-environment)
1. [Clean the environment](#Clean-env)


## Quick start

1. The purpose here, is to ingest some data, thinking in a self service architecture that can be composed by:

Notes:
*A kinesis firehose, to collect the files on the source and stores on S3 bucket, in CSV format (not included in this code)
*After that, control the events with aws lambda events.
*When the file comes, the process starts automatically.

The code here, will build an architecture, to create and load the data inside a Redshift cluster.

So, to run the code, you will need to follow these steps:
1) To create the redshift cluster, and the IAM roles and config the dwh.cfg file
    $ %run create_stucture_IaC.py
2) To drop/create the tables inside the Redshift cluster
    $ %run create_tables.py
3)  To load the tables based on the files on the S3 bucket (CSV)
    $ %run etl.py
    
# If you have some problems with the execution, install the following requirements:

## Prepare the environment

```
$ pip install boto3 && pip install psycopg2
```

## Clean the environment

At the end of the process

```
Follow the comments inside the main function, and uncomment the clean line, and comment the others, in the create_stucture_IaC.py file

    #clean_redshift_cluster()
    #clean_iam_roles()
    
    
And after you comment the other lines, run it again:

    $ %run create_stucture_IaC.py
    
```

##End of README

