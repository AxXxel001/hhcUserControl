import sqlite3

class Database(object):

	def __init__(self):
		self.connection = sqlite3.connect("hhcUserControl.db")
		self.cursor = self.connection.cursor()
		self.createTables()

	def createTables(self):
		self.cursor.execute(
			"""CREATE TABLE IF NOT EXISTS `contact` (
				`id` INTEGER PRIMARY KEY AUTOINCREMENT,
				`prefix` TEXT,
				`first_name` TEXT,
				`last_name` TEXT,
				`birth_date` DATE,
				`comment` TEXT
		)""")

		self.cursor.execute(
			"""CREATE TABLE IF NOT EXISTS `mail` (
				`id` INTEGER PRIMARY KEY AUTOINCREMENT,
				`contact_id` INTEGER REFERENCES contact(id),
				`description` TEXT,
				`address` TEXT
		)""")

		self.cursor.execute(
			"""CREATE TABLE IF NOT EXISTS `phone` (
				`id` INTEGER PRIMARY KEY AUTOINCREMENT,
				`contact_id` INTEGER REFERENCES contact(id),
				`description` TEXT,
				`number` TEXT
		)""")

		self.cursor.execute(
			"""CREATE TABLE IF NOT EXISTS `address` (
				`id` INTEGER PRIMARY KEY AUTOINCREMENT,
				`contact_id` INTEGER REFERENCES contact(id),
				`description` TEXT,
				`street` TEXT,
				`number` INTEGER(8),
				`addr_extra` TEXT,
				`postal` TEXT,
				`city` TEXT
		)""")

		self.cursor.execute(
			"""CREATE TABLE IF NOT EXISTS `study` (
				`id` INTEGER PRIMARY KEY AUTOINCREMENT,
				`contact_id` INTEGER REFERENCES contact(id),
				`status` TEXT,
				`school` TEXT,
				`course` TEXT,
				`start` DATE,
				`end` DATE,
				`focus` TEXT,
				`degree` TEXT
		)""")

		self.cursor.execute(
			"""CREATE TABLE IF NOT EXISTS `member` (
				`contact_id` INTEGER PRIMARY KEY REFERENCES contact(id),
				`ressort` TEXT,
				`active` INTEGER(1),
				`position` TEXT,
				`joined` DATE,
				`left` DATE
		)""")

	def commit(self):
		return self.database.commit()


if __name__ == "__main__":
	db = Database()