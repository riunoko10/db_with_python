import psycopg2
import pymysql
import os

def conn_db_postgresql():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        database=os.getenv('POSTGRES_DB'),
        port=os.getenv('POSTGRES_PORT')
        )
    return conn

def conn_db_mysql():
    conn = pymysql.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'), 
            password=os.getenv('MYSQL_PASSWORD'), 
            database=os.getenv('MYSQL_DB'),
            port=int(os.getenv('MYSQL_PORT'))
        )
    return conn

