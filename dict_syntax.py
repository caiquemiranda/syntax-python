"""
syntax template dict

dict()
variable = {}

"""

my_dict = {}
content_of_value1 = 'abcd'
content_of_value2 = 'xyzw'

# adc in dict
my_dict.update({'key_name1': content_of_value1})
my_dict.update({'key_name2': content_of_value2})

print(my_dict)

print(my_dict.get('key_name2'))

print('#####################')

my_dict2 = {'key1': [1, 2, 3], 'key2': 'a string', 123: 456}
print(my_dict2['key1'])
print(my_dict2[123])

# adc
my_dict2['new_key'] = 'New value'
print(my_dict2)
