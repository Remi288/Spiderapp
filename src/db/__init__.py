import psycopg2
from decouple import config



class DB:


  @classmethod
  def connect(cls):
    # Connect to the database
    # Return the connection object
    try:
      conn = psycopg2.connect(
        host=config('host'),
        database=None,
        # user=config('user'),
        # password=config('password'),
        port=config('port'))
      conn.autocommit = True
      cursor = conn.cursor()
      cursor.execute('''DROP DATABASE IF EXISTS scraperdb''')
      cursor.execute('''CREATE DATABASE scraperdb''')

      # cur = conn.cursor()
      # self.cur = cur
      # self.conn = conn
      return conn
    except (psycopg2.Error) as err:
      print('Error while connecting to postgreSQL', err)


  def new_connect(cls):
    # Connect to the database
    # Return the connection object
    try:
      conn = psycopg2.connect(
        host=config('host'),
        database=config('database'),
        user=config('user'),
        password=config('password'),
        port=config('port'))
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
    # Execute the seed SQL script
    # Return value does not matter
  @classmethod
  def close(cls):
      cls.close()
      DB().connect().close()

  @classmethod
  def links(cls):
    # Returns a reference to the links interface
    pass

  @classmethod
  def pages(cls):
    # Returns a reference to the pages interface
    pass
db = DB()
db.connect()
db.new_connect()
db.setup()
db.seed()