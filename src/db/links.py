


class Links:


  def __int__(self, connect):
    self.connection = connect
    self.cursor = self.connection.cursor()

  def insert(self, id, page_id, url):
    self.cursor.execute("INSERT INTO table (id,page_id,url) VALUES ( %s, %s, %s)", (id,page_id,url))
    self.connection.commit()






  def select(self, page_id):
    self.cursor.execute('SELECT id,url FROM links')
    record = self.cursor.fetchall()
    return record



  def delete(self):
    self.cursor.execute('DELETE FROM links')
    self.connect.commit()






