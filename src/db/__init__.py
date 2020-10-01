import psycopg2
from psycopg2 import connect, sql, extensions
from decouple import config
from src.db.links import Links
from src.db.pages import Pages
# from src.spider import get_url



class DB:

  @classmethod
  def connect(cls):
    '''Function that Connects to the server,
       drops database if it exists and creates database
       Returns a connection object
    '''
    try:
      print(config('POSTGRES_PASSWORD'))
      connection = psycopg2.connect(
        dbname=None,
        port=config('POSTGRES_PORT', cast=int),
        host=config('POSTGRES_HOST'),
        password=config('POSTGRES_PASSWORD'),
        user=config('POSTGRES_USER')
      )
      connection.autocommit = True
      cursor = connection.cursor()
      cursor.execute(f'''DROP DATABASE IF EXISTS {config("POSTGRES_DB")}''')
      cursor.execute(f'''CREATE DATABASE {config("POSTGRES_DB")}''')
      return connection
    except (Exception, psycopg2.Error) as error:
      print('Error while connecting to PostgreSQL', error)

  @classmethod
  def new_connect(cls):
    '''Function that Connects to the database,
        Returns a connection object
    '''
    # cls.connect()
    try:
      connection = psycopg2.connect(
        dbname=config('POSTGRES_DB'),
        port=config('POSTGRES_PORT', cast=int),
        host=config('POSTGRES_HOST'),
        user=config('POSTGRES_USER'),
        password=config('POSTGRES_PASSWORD')
      )
      connection.autocommit = True
      return connection
    except (Exception, psycopg2.Error) as error:
      print('Error while connecting to PostgreSQL', error)

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
