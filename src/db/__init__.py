import psycopg2
from psycopg2 import connect, sql, extensions
from decouple import config
from src.db.links import Links
from src.db.pages import Pages
# from src.spider import get_url



class DB:
  @classmethod
  def connect(cls):
    try:
      connection = psycopg2.connect(
         host=config('DB_HOST'),
         database=None,
         port=config('DB_PORT')
      )
      connection.autocommit = True
      cursor = connection.cursor()
      # cursor.execute("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'scraperdb'")
      cursor.execute('DROP DATABASE IF EXISTS scraperdb')
      cursor.execute('CREATE DATABASE scraperdb')
      return connection
    except psycopg2.Error as e:
      print('Error occurred while trying to connect to postgreSQL', e)



  @classmethod
  def new_connect(cls):
    try:
      connection = psycopg2.connect(
        host=config('DB_HOST'),
        database=config('DB_NAME'),
        port=config('DB_PORT', cast=int),
        user=config('DB_USER'),
        password=('DB_PASSWORD')
      )
      connection.autocommit = True
      return connection
    except (Exception, psycopg2.Error) as e:
      print('Error while connecting to PostgreSQL', e)

  @classmethod
  def setup(cls):
    connect = DB().new_connect()
    cur = connect.cursor()
    with open('src/schemas/structure.sql') as s:
      sql_script = s.readlines()
      for line in sql_script:
        cur.execute(line)
    cls.new_connect().commit()
  # Execute the structure SQL script
    # Return value does not matter


  @classmethod
  def seed(cls):
    connect = DB().new_connect()
    cur = connect.cursor()
    with open('src/schemas/seed.sql') as ss:
      sql_script = ss.readlines()
      for line in sql_script:
        cur.execute(line)
    cls.new_connect().commit()
    # Execute the seed SQL script
    # Return value does not matter
  # @classmethod
  # def close(cls):
  #     cls.close()
  #     DB().connect().close()

  @classmethod
  def links(cls):
    # Returns a reference to the links interface
    links = Links(cls.new_connect())
    return links


  @classmethod
  def pages(cls):
    # Returns a referslence to the pages interface
    result = cls.new_connect()
    pages = Pages(result)
    return pages
