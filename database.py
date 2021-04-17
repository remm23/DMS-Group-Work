# Database code
import sqlite3

con = sqlite3.connect("example.db")
cur = con.cursor()

## Customer Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Customer(
	id TEXT PRIMARY KEY, 
	email TEXT,
	password TEXT,
	first_name TEXT,
	last_name TEXT,
	billing_address TEXT,
	shipping_address TEXT,
	country TEXT,
	phone TEXT);
""")


## Address Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Address(
	id TEXT,
	customer_id TEXT, --maps to Customer.id
	first_name TEXT,
	last_name TEXT,
	building_no TEXT,
	street TEXT,
	city TEXT,
	country TEXT, --maps to Customer.country
	post_code TEXT,
	is_default BOOL,
	PRIMARY KEY (id, customer_id),
	FOREIGN KEY (customer_id) REFERENCES Customer(id)
);
""")

## Customer_Order Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Customer_Order(
	id TEXT,
	customer_id TEXT,
	product_id TEXT,
	billing_address TEXT,
	shipping_address TEXT,
	order_name TEXT,
	order_email TEXT,
	order_date TEXT, --SQLite needs to store date as text
	order_status TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (customer_id) REFERENCES Customer(id),
	FOREIGN KEY (product_id) REFERENCES Product(id)
);
""")

## Payment Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Payment(
	id TEXT,
	order_id TEXT,
	payment_method TEXT,
	payment_accepted,
	first_name,
	last_name,
	card_name,
	card_number,
	expire_date TEXT,
	default_payment BOOL,
	PRIMARY KEY (id)
	FOREIGN KEY (order_id) REFERENCES Customer_Order(id)
);
""")

## Product Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Product(
	id TEXT,
	name TEXT,
	brand TEXT,
	price INTEGER, --Store the price as pennies
	stock iNTEGER,
	weight TEXT,
	description TEXT,
	image BLOB,
	thumbnail BLOB,
	has_camera BOOL,
	resolution TEXT,
	screen_size TEXT,
	energy_rating CHAR,
	OS_compatibility TEXT,
	has_battery BOOL,
	battery_life TEXT,
	processor TEXT,
	option TEXT,
	PRIMARY KEY (id)
);
""")

## Basket Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Basket(
	customer_id TEXT,
	product_id TEXT,
	product_name TEXT,
	brand TEXT,
	color TEXT,
	quantity INTEGER,
	in_stock BOOL,
	saved_for_later BOOL,
	option TEXT,
	PRIMARY KEY (customer_id, product_id),
	FOREIGN KEY (customer_id) REFERENCES Customer(id),
	FOREIGN KEY (product_id) REFERENCES Product(id)
);
""")

## Wishlist Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Wishlist(
	customer_id TEXT,
	product_id TEXT,
	name TEXT,
	product_name TEXT,
	brand TEXT,
	color TEXT,
	in_stock BOOL,
	option TEXT,
	PRIMARY KEY (customer_id, product_id),
	FOREIGN KEY (customer_id) REFERENCES Customer(id),
	FOREIGN KEY (product_id) REFERENCES Product(id)
);
""")

## Refund Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Refund(
	id TEXT,
	customer_id TEXT,
	product_id TEXT,
	quantity INTEGER,
	status TEXT,
	reson_description TEXT,
	reson_option TEXT,
	approved TEXT,
	PRIMARY KEY (id, customer_id),
	FOREIGN KEY (customer_id) REFERENCES Cancellation(customer_id)
);
""")

## Cancellation Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Cancellation(
	id TEXT,
	customer_id TEXT,
	product_id TEXT,
	billing_address TEXT,
	shipping_address TEXT,
	status TEXT,
	PRIMARY KEY (id, customer_id),
	FOREIGN KEY (customer_id) REFERENCES Customer_Order(customer_id)
);
""")

## Promotion Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Promotion(
	id TEXT,
	product_id TEXT,
	start_date TEXT,
	end_date TEXT, --SQLite needs to store date as text
	price INTEGER, -- price is stored as pennies
	price_cut INTEGER,
	PRIMARY KEY (id, product_id),
	FOREIGN KEY (product_id) REFERENCES Product(id)
);
""")


# cur.execute("""
# INSERT INTO Customer
# 	(id) VALUES (1234
# );
# """)

# cur.execute("""
# INSERT INTO Customer
# 	VALUES (
# 		'1236',
# 		'Johndoe@example.com',
# 		'password',
# 		'John',
# 		'Doe',
# 		'64 Zoo Lane',
# 		'64 Zoo Lane',
# 		'United Kingdom',
# 		'555-555-5555'
# 	);
# """)

# cur.execute("""
# INSERT INTO Address
# 	VALUES (
# 		'1',
# 		'1237',		
# 		'John',
# 		'Doe',
# 		'64',
# 		'Zoo Lane',
# 		'London',
# 		'United Kingdom',
# 		'W5 1XB',
# 		'1'
# 	);
# """)

# Save the changes 
con.commit()

# Close the connection when complete
con.close()

