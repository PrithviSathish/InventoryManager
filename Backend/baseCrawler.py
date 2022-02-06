from unicodedata import category
import mysql.connector
import prettytable
import random


class crawl:

	def __init__(self, user) -> None:
		
		self.connection = mysql.connector.connect(host="remotemysql.com", user="5jBdUHTRPG", passwd = "QPMKcvQU51", database="5jBdUHTRPG")
		self.cursor = self.connection.cursor()

		self.cursor.execute("""
						CREATE TABLE IF NOT EXISTS
						{}(
							serial_number integer primary key,
							product_code integer not null,
							quantity float not null,
							expiry_date date not null,
							storage_location varchar(20) not null,
							purchase_price float not null
						)
						;
						""".format(user))
		self.cursor.execute("""
						CREATE TABLE IF NOT EXISTS
						products(
							ID integer primary key,
							Name varchar(50) NOT NULL,
							Category varchar(20) not null
						);
						""")

		self.PrettyTable = prettytable.PrettyTable
		self.tabulate = prettytable.from_db_cursor
		self.serial = -1
		self.cursor2 = self.connection.cursor()

		# Hi Prithvi, store the username in this variable
		self.user = user

	def select_product(self) -> int:
		"""Displays list of products available in the user's database, and returns the corresponding product code that the user selects"""
		
		self.cursor.execute("""
				SELECT
					products.name, {0}.product_code
				FROM
					{0}, products
				WHERE
					{0}.product_code = products.id
				GROUP BY
					{0}.product_code
				ORDER BY
					products.name
				;
				""".format(self.user))
		print(self.tabulate(self.cursor))
		return int(input("Enter selected product code: "))

	def show_products(self):
		self.cursor.execute(f"SELECT * FROM {self.user}")
		print(self.tabulate(self.cursor))

	def sell(self, product : int, selling_price : int, quantity_sold : float) -> tuple:
		"""Always sells off the oldest stock first and returns the profit and profit percentage or loss and loss percentage according to the inputs. If a particular batch is sold out completely, it'll be deleted from the records"""

		statement = f"""
	SELECT
		{{}}
	FROM
		{self.user}
	WHERE
		product_code = {product}
	ORDER BY
		expiry_date
	;
	"""
		self.cursor.execute(statement.format("serial_number, expiry_date, storage_location, quantity as 'Initial Quantity'"))
		table = self.tabulate(self.cursor)
		self.cursor.execute(statement.format("serial_number, quantity, purchase_price"))
		records = self.cursor.fetchall()
		quantity = quantity_sold
		deducted = 0
		delete_tuple = ()
		cost = 0
		for record in records:
			if record[1] <= quantity:
				delete_tuple += record[0]
				deducted += record[0]
				cost += record[1] * record[2]
			elif quantity:
				updated_quantities = [0]*len(delete_tuple)
				self.cursor.execute("""
	DELETE FROM
		{}
	WHERE
		serial_number in {}
	;
	""".format(self.user, delete_tuple))
				remainder = record[1] - quantity
				quantity = 0
				updated_quantities += [remainder]
				self.cursor.execute("""
	UPDATE
		{}
	SET
		quantity = {}
	WHERE
		serial_number = {}
	;
	""".format(self.user, remainder, record[0]))
				cost += remainder * record[2]
			else:
				updated_quantities += [record[1]]
		table.add_column("Updated Quantity", updated_quantities)
		print(table)
		money_received = quantity_sold * selling_price
		profit = money_received - cost
		return (profit, profit/money_received*100)

	# Hi Prithvi, use this if the option is selected
	def profit_calc(self):
		product = self.select_product()	
		selling_price = int(input("Enter the price it was sold for: "))
		quantity_sold = int(input("Enter the total quantity sold: "))
		profit, money_received = self.sell(product, selling_price, quantity_sold)
		if profit >= 0:
			print(f"Profit: {profit} ({profit/money_received*100}%)")
		else:
			print(f"Loss: {-profit} ({-profit/money_received*100}%)")

	def serial_generator(self, table_name, column_name):
		self.cursor2.execute(f"SELECT MAX({column_name}) FROM {table_name}")
		fetchnum = self.cursor2.fetchone()[0]
		if fetchnum == None:
			return 0
		else:
			return fetchnum + 1


	def insert(self):
		n='y'
		while n.lower()=="y":
			serial = self.serial_generator(self.user, "serial_number")
			if input("Existing product / New product? (E/N): ").lower() == "e":
				product_code = self.select_product()
			else:
				product_name = input("Enter the product name: ")
				category = input("Enter the category: ")
				product_code = self.serial_generator("products", "id")
				self.cursor.execute(f"INSERT INTO products VALUES {(product_code, product_name, category)}")
				self.connection.commit()
			quantity=float(input("Enter the quantity of the desired product: "))
			expiry_date=input("Enter the expiry date of the product: ")
			storage_location=input(" Enter the place where the product is stored: ")
			if expiry_date == '':
				expiry_date = "NULL"
			if storage_location == '':
				storage_location = "NULL"
			purchase_price=float(input(" Enter the purchase price of the product: "))
			es=f"insert into {self.user}(serial_number,product_code,quantity,expiry_date,storage_location,purchase_price) values ({serial}, {product_code}, {quantity}, '{expiry_date}', '{storage_location}', {purchase_price})"
			self.cursor.execute(es)
			self.connection.commit()
			n=input("Enter y to insert more records or n to terminate: ")

	def update(self):
		ch=0
		while ch==0:
			num=int(input("Enter\n1. To update product_code\n2. To update the quantity\n3. To update the expiry_date\n4. To update the the storage_location\n5. To update the purchase_price"))
			if num==1:
				new_pc=int(input("Enter the new product_code"))
				self.cursor.execute(f"update {self.user} set product_code={new_pc}") #Enter the table name
				self.connection.commit()               
			elif num==2:
				new_qt=float(input("Enter the new quantity"))
				self.cursor.execute(f"update {self.user} set quantity={new_qt}") #Enter the table name
				self.connection.commit()               
			elif num==3:
				new_ed=input("Enter the new expiry_date")
				self.cursor.execute(f"update {self.user} set expiry_date={new_ed}") #Enter the table name
				self.connection.commit()
			elif num==4:
				new_sl=input("Enter the new storage location")
				self.cursor.execute(f"update {self.user} set storage_location={new_sl}") #Enter the table name
				self.connection.commit()               
				
			elif num==5:
				new_pp=float(input("Enter the new purchase price"))
				self.cursor.execute(f"update {self.user} set purchase_price={new_pp}") #Enter the table name
				self.connection.commit()               
			else:
				ch=int(input("Enter a non null value to terminate the updation process"))
				break