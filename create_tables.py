import configparser
import os 
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
      cur.execute('CREATE SCHEMA IF NOT EXISTS fornecedores_tubos;')
      cur.execute(query)
      conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
      cur.execute('CREATE SCHEMA IF NOT EXISTS fornecedores_tubos;')
      cur.execute(query)
      result = cur.execute(""" SELECT table_schema, table_name FROM information_schema.tables WHERE table_name = 'bill_of_materials' """)
      print(cur.fetchall())
      conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()