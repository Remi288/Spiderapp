class Pages:

  def __int__(self, conn):
    self.connection = conn
    self.cursor = self.connection.cursor()




  def select(self):
    self.cursor.execute('SELECT id,url FROM Pages')
    record = self.cursor.fetchall()
    return record


  def fetch_url(self, page_id):
    self.cursor.execute('SELECT url FROM Pages WHERE page_id=%s', (page_id,))
    url = self.cursor.fetchone()
    return url



  def find(self, id):
    self.cursor.execute('SELECT * FROM Pages WHERE page_id=%s', (id,))
    row = self.cursor.fetchone()
    return row


  def update_id(self, id):
    self.id = id
    self.cursor.execute('UPDATE Pages SET is_scraping= TRUE WHERE id=%s', (id,))
    return self.find(id)

  # def update_id(self, id):
  #   self.id = id
  #   self.cursor.execute('UPDATE Pages SET is_scraping= TRUE WHERE id=%s', (id,))
  #   return self.find(id)

