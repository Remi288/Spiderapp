import psycopg2
from psycopg2 import connect, sql, extensions
from decouple import config
from src.db.links import Links
from src.db.pages import Pages
# from src.spider import get_url



class DB:


  @classmethod
  def connect(cls):
    # Connect to the database
    # Return the connection object
    try:
      conn = psycopg2.connect(
        host=config('DB_HOST'),
        database=None,
        # user=config('user'),
        # password=config('password'),
        port=config('DB_PORT', cast=int))
      conn.autocommit = True
      cursor = conn.cursor()
      cursor.execute(sql.SQL('''DROP DATABASE IF EXISTS scraperdb'''))
      cursor.execute(sql.SQL('''CREATE DATABASE scraperdb'''))

      # cur = conn.cursor()
      # self.cur = cur
      # self.conn = conn
      return conn
    except (psycopg2.Error) as err:
      print('Error while connecting to postgreSQL', err)

  @classmethod
  def new_connect(cls):
    # Connect to the database
    # Return the connection object
    try:
      conn = psycopg2.connect(
        host=config('DB_HOST'),
        database=config('DB_NAME'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        port=config('DB_PORT', cast=int))
      # cursor = conn.cursor()
      # cursor.execute('''DROP DATABASE IF EXISTS scraperdb''')
      # cursor.execute('''CREATE DATABASE scraperdb''')
      #

      # cur = conn.cursor()
      # self.cur = cur
      # self.conn = conn
      conn.autocommit = True
      return conn
    except (psycopg2.Error) as err:
      print('Error while connecting to postgreSQL', err)


  @classmethod
  def setup(cls):
    connect = DB().new_connect()
    cur = connect.cursor()
    with open('/Users/user/PycharmProjects/week-8-task-python-Remi288/src/schemas/structure.sql') as s:
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
    with open('/Users/user/PycharmProjects/week-8-task-python-Remi288/src/schemas/seed.sql') as ss:
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
    # Returns a reference to the pages interface
    pages = Pages(cls.new_connect())
    return pages
# db = DB()
# db.connect()
# db.new_connect()
# db.setup()
# db.seed()
# page = db.pages(1)