import mysql.connector
import prettytable


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
							expiry_date date,
							storage_location varchar(20),
							purchase_price float not null
						)
						;
						""".format(user))
		self.cursor.execute("""
						CREATE TABLE IF NOT EXISTS
						products(
							ID integer primary key,
							Name varchar(50) NOT NULL,
							Category varchar(20)
						);
						""")

		self.PrettyTable = prettytable.PrettyTable
		self.tabulate = prettytable.from_db_cursor

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