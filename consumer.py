from kafka import KafkaConsumer, TopicPartition
import sqlite3
from converter import int_converter, str_converter, bool_converter
from db import cursor, conn
from kafka_func import TOPIC_NAME, decode, KAFKA_SERVER


consumer = KafkaConsumer(TOPIC_NAME, group_id="main", auto_offset_reset='earliest', enable_auto_commit=True, auto_commit_interval_ms=1000, bootstrap_servers=KAFKA_SERVER)
for message in consumer:
	data = decode(message.value)

	columns_datas = [
		'business_id', 'name', 'address', 'city', 'state',
		'postal_code', 'latitude', 'longitude', 'stars',
		'review_count', 'is_open', 'categories'
	]

	keys = [data.get(c) for c in columns_datas]

	cursor.execute("""
		INSERT INTO datas(
			business_id,
			name,
			address,
			city,
			state,
			postal_code,
			latitude,
			longitude,
			stars,
			review_count,
			is_open,
			categories
		)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
	""", keys)

	data_id = cursor.lastrowid

	if data.get('hours'):
		columns_hours = [
		'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
		'Saturday', 'Sunday'
		]
		keys = [data.get('hours').get(c) for c in columns_hours]
		keys.append(data_id)
		cursor.execute("""
			INSERT INTO hours(
				Monday,
				Tuesday,
				Wednesday,
				Thursday,
				Friday,
				Saturday,
				Sunday,
				data_id
			)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?)
		""", keys)


	if data.get('attributes'):
		attributes = data.get('attributes')
		columns_attributes = {
			'RestaurantsTableService': bool_converter,
			'WiFi': str_converter,
			'BikeParking': bool_converter,
			'BusinessAcceptsCreditCards': bool_converter,
			'RestaurantsReservations': bool_converter,
			'WheelchairAccessible': bool_converter,
			'Caters': bool_converter,
			'OutdoorSeating': bool_converter,
			'RestaurantsGoodForGroups': bool_converter,
			'HappyHour': bool_converter,
			'BusinessAcceptsBitcoin': bool_converter,
			'RestaurantsPriceRange2': int_converter,
			'HasTV': bool_converter,
			'Alcohol': str_converter,
			'DogsAllowed': bool_converter,
			'RestaurantsTakeOut': bool_converter,
			'NoiseLevel': str_converter,
			'RestaurantsAttire': str_converter,
			'RestaurantsDelivery': str_converter
		}

		keys = [
			_conv((attributes).get(_key))
			for _key, _conv in columns_attributes.items()
		]
		keys.append(data_id)
		cursor.execute("""
			INSERT INTO attributes(
				RestaurantsTableService,
				WiFi,
				BikeParking,
				BusinessAcceptsCreditCards,
				RestaurantsReservations,
				WheelchairAccessible,
				Caters,
				OutdoorSeating,
				RestaurantsGoodForGroups,
				HappyHour,
				BusinessAcceptsBitcoin,
				RestaurantsPriceRange2,
				HasTV,
				Alcohol,
				DogsAllowed,
				RestaurantsTakeOut,
				NoiseLevel,
				RestaurantsAttire,
				RestaurantsDelivery,
				data_id
			)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
		""", keys)
		attribute_id = cursor.lastrowid

		business_parking = attributes.get('BusinessParking')
		if business_parking and eval(business_parking):
			columns_business_parking = [
				'garage', 'street', 'validated', 'lot', 'valet'
			]
			keys = [
				eval(business_parking).get(c) for c in columns_business_parking
			]
			keys.append(attribute_id)
			cursor.execute("""
				INSERT INTO business_parking(
					garage,
					street,
					validated,
					lot,
					valet,
					attribute_id
				)
				VALUES (?, ?, ?, ?, ?, ?)
			""", keys)

		ambience = attributes.get('Ambience')
		if ambience and eval(ambience):
			columns_ambience = [
				'touristy', 'hipster', 'romantic', 'divey', 'intimate',
				'trendy', 'upscale', 'classy', 'casual'
			]
			keys = [
				eval(ambience).get(c)
				for c in columns_ambience
			]
			keys.append(attribute_id)
			cursor.execute("""
				INSERT INTO ambience(
					touristy,
					hipster,
					romantic,
					divey,
					intimate,
					trendy,
					upscale,
					classy,
					casual,
					attribute_id
				)
				VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
			""", keys)


		good_for_meal = attributes.get('GoodForMeal')
		if good_for_meal and eval(good_for_meal):
			columns_good_for_meal = [
				'dessert', 'lunch', 'dinner', 'brunch', 'breakfast'
			]
			keys = [
				eval(good_for_meal).get(c)
				for c in columns_good_for_meal
			]
			keys.append(attribute_id)
			cursor.execute("""
				INSERT INTO good_for_meal(
					dessert,
					lunch,
					dinner,
					brunch,
					breakfast,
					attribute_id
				)
				VALUES (?, ?, ?, ?, ?, ?)
			""", keys)

	conn.commit()
	print(f'Message with ID: {data_id} written to db.')
conn.close()
