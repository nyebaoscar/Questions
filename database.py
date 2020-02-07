from flask import g
import sqlite3
import psycopg2
from psycopg2.extras import DictCursor

def connect_db():
    conn = psycopg2.connect('postgres://mklcnjiyeceaao:25dc0a9db08d8dd6de52889d3525ff6ec944a1f29f1c00ef215c29a9981051f9@ec2-34-235-108-68.compute-1.amazonaws.com:5432/db75bvk6cnf71f', cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()
    return conn, sql

def get_db():
    db = connect()
    
    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]
        
    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur
