from atexit import register
from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase(
    "cogoport_api_spark2",
    user="spark2",
    password="82f55836",
    host="login-spark2.dev.cogoport.io",
    port=6432,
    autorollback=True,
)