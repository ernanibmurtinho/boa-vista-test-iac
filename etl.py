import configparser
from sql_queries import copy_table_queries
from time import time
import configparser
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import os 

#loading sql libs

#%load_ext sql 

def loadTables(cur, conn, schema, tables, role_arn):
    loadTimes = []
    
    SQL_SET_SCEMA = "SET search_path TO {};".format(schema)
    cur.execute(SQL_SET_SCEMA)
    DWH_ROLE_ARN = role_arn
    
    for table in tables:
        SQL_COPY = """
                    copy {} from 's3://awsds/fornecedores_tubos/{}' 
                    credentials 'aws_iam_role={}'
                    region 'us-west-2' delimiter ','
                            """.format(table,table, DWH_ROLE_ARN)

        print("======= LOADING TABLE: ** {} ** IN SCHEMA ==> {} =======".format(table, schema))
        print(SQL_COPY)

        t0 = time()
        cur.execute(SQL_COPY)
        loadTime = time()-t0
        loadTimes.append(loadTime)

        print("=== DONE IN: {0:.2f} sec\n".format(loadTime))
    return pd.DataFrame({"table":tables, "loadtime_"+schema:loadTimes}).set_index('table')


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    DWH_ROLE_ARN = config.get("DWH", "DWH_ROLE_ARN")
    
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    fornecedores_tubos = loadTables(cur, conn, "fornecedores_tubos", copy_table_queries, DWH_ROLE_ARN)

    conn.close()


if __name__ == "__main__":
    main()