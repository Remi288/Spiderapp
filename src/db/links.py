


class Links:
  ''' class that handle the link table in the database interface
  insert function insert all id, url, page-id in the link table
  select function select all the id, url form the link table
  delect function delect all values from the link table
  '''


  def __init__(self, connect):
    self.connection = connect
    self.cursor = self.connection.cursor()

  def insert(self, id, page_id, url):
    self.cursor.execute("INSERT INTO links (id,page_id,url) VALUES ( %s, %s, %s)", (id,page_id,url))
    self.connection.commit()



  def select(self, page_id):
    self.cursor.execute('SELECT id,url FROM links')
    record = self.cursor.fetchall()
    return record



  def delete(self):
    self.cursor.execute('DELETE FROM links')
    self.connection.commit()






