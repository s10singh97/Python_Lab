import sqlite3

conn = sqlite3.connect("finance.db")
conn.execute("CREATE TABLE IF NOT EXISTS histories(id integer, screenname text, transacted datetime default CURRENT_TIMESTAMP)")
conn.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key AUTO_INCREMENT not null, username text not null, hash text not null)")
conn.execute("CREATE UNIQUE INDEX username ON users(username)")
conn.commit()
conn.close()