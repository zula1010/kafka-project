import sqlite3, os


if os.path.exists('testdb.db'):
	os.remove('testdb.db')
conn = sqlite3.connect('testdb.db')
cursor = conn.cursor()
sql_create_datas_table ='''CREATE TABLE IF NOT EXISTS datas(
	id integer PRIMARY KEY,
	business_id text,
	name text,
	address text,
	city text,
	state char(2),
	postal_code char(12),
	latitude float, 
	longitude float,
	stars float,
	review_count integer,
	is_open boolean,
	categories text
)'''
cursor.execute(sql_create_datas_table)
sql_create_attributes_table = '''CREATE TABLE IF NOT EXISTS attributes(
	id integer PRIMARY KEY ,
	RestaurantsTableService boolean,
	WiFi text,
	BikeParking boolean,
	BusinessAcceptsCreditCards boolean,
	RestaurantsReservations boolean,
	WheelchairAccessible boolean,
	Caters boolean,
	OutdoorSeating boolean,
	RestaurantsGoodForGroups boolean,
	HappyHour boolean,
	BusinessAcceptsBitcoin boolean,
	RestaurantsPriceRange2 integer,
	HasTV boolean,
	Alcohol text,
	DogsAllowed boolean,
	RestaurantsTakeOut boolean,
	NoiseLevel text,
	RestaurantsAttire text,
	RestaurantsDelivery text,
	data_id integer not null,
   FOREIGN KEY (data_id) REFERENCES datas (id)
)'''
cursor.execute(sql_create_attributes_table)

sql_create_business_parking_table ='''CREATE TABLE IF NOT EXISTS business_parking(
	id integer PRIMARY KEY,
	garage boolean,
	street boolean,
	validated boolean,
	lot boolean,
	valet boolean,
	attribute_id integer not null,
   	FOREIGN KEY (attribute_id) REFERENCES attributes (id)
)'''
cursor.execute(sql_create_business_parking_table)

sql_create_ambience_table ='''CREATE TABLE IF NOT EXISTS ambience(
	id integer PRIMARY KEY,
	touristy boolean,
	hipster boolean,
	romantic boolean,
	divey boolean,
	intimate boolean,
	trendy boolean,
	upscale boolean,
	classy boolean,
	casual boolean,
	attribute_id integer not null,
   	FOREIGN KEY (attribute_id) REFERENCES attributes (id)
)'''
cursor.execute(sql_create_ambience_table)

sql_create_good_for_meal_table ='''CREATE TABLE IF NOT EXISTS good_for_meal(
	id integer PRIMARY KEY,
	dessert boolean,
	lunch boolean,
	dinner boolean,
	brunch boolean,
	breakfast boolean,
	attribute_id integer not null,
   	FOREIGN KEY (attribute_id) REFERENCES attributes (id)
)'''
cursor.execute(sql_create_good_for_meal_table)

sql_create_hours_table ='''CREATE TABLE IF NOT EXISTS hours(
	id integer PRIMARY KEY,
	Monday integer,
	Tuesday integer,
	Wednesday integer,
	Thursday integer,
	Friday integer,
	Saturday integer,
	Sunday integer,
	data_id integer not null,
   	FOREIGN KEY (data_id) REFERENCES datas (id)
)'''

cursor.execute(sql_create_hours_table)
conn.commit()