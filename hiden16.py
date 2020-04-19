from random import randint
from re import findall


ALPHABET = ['a','b','c','d','e','f']


def append_some_random_chars(data):
	count_new_symbols = randint(1,4)
	for i in range(0,count_new_symbols):
		index_char_from_alphabet = randint(0,5)
		data += ALPHABET[index_char_from_alphabet]
	return data


def encoding(plain_text):
	encoded_text = ""
	for character in plain_text:
		character_ascii_code = ord(character)
		encoded_text = append_some_random_chars(encoded_text)
		encoded_text += str(character_ascii_code)
		encoded_text = append_some_random_chars(encoded_text)
	return encoded_text


def decoding(encoded_text):
	digit_from_data = findall("\d+", encoded_text)
	decoded_text = ""
	for i in digit_from_data:
		decoded_text += chr(int(i))
	return decoded_text	