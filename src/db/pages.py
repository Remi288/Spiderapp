class Pages:
  '''this class handle the page table interface'''

  def __init__(self, conn):
    self.connection = conn
    self.cursor = self.connection.cursor()

  def select(self):
    ''' function that select id and url from page table'''
    self.cursor.execute('SELECT id, url FROM pages')
    record = self.cursor.fetchall()
    return record

  def fetch_url(self, page_id):
    '''function return the url in string from the id inserted in the page table'''
    self.cursor.execute('SELECT url FROM Pages WHERE id=%s', (page_id,))
    url = self.cursor.fetchone()
    return url

  def find(self, id):
    ''' function return the row with the id inserted from the page table'''
    self.cursor.execute('SELECT * FROM Pages WHERE id=%s', (id,))
    row = self.cursor.fetchone()
    return row


  def update_id_false(self, id):
    '''function update the is_scraping to false with the page id given '''
    self.id = id
    self.cursor.execute('UPDATE Pages SET is_scraping= False WHERE id=%s', (id,))
    return self.find(id)


  def update_id_true(self, id):
    '''function update the is_scraping to true with the page id given '''
    self.id = id
    self.cursor.execute('UPDATE Pages SET is_scraping= True WHERE id=%s', (id,))
    return self.find(id)

