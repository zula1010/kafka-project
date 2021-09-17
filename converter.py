

def bool_converter(value):
	if not value:
		return None

	return True if value.lower() == 'true' else False

def int_converter(value):
	if value is None or type(value) != int:
		return -1

	return int(value)

def str_converter(value):
	if value is None or type(value) != str:
		return None

	return eval(str(value))