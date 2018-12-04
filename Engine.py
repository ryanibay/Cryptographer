# Enigma Engine
# Ryan Marcel Ibay (2018-21278)
# Please type your names and student numbers!

# File Editing (Cipher and Message):
def SaveItem(item, file_name):
	file = open(file_name, "w")
	file.write(item)
	file = file.close()

def OpenItem(file_name):
	file = open(file_name, "r")
	file_l = []
	for item in file:
		file_l.append(item)
	file.close()
	return file_l[0]

# Encrypting Algorithms:
def CaesarE(mode, message, key):
	max_k = 26
	translated = ''
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated += chr(num)
		else:
			translated += symbol

	return translated

def SubstitutionCipherE(mode, message, key):
	alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	message = message.lower()
	message = list(message)
	key = list(key)

	full_message = []

	for m in message:	
		if m == ' ':
			full_message.append(m)
		elif m in alph:
			for item in alph:
				if m == item:
					match = alph.index(item)
					code = key[match]
					full_message.append(code)
		else:
			full_message.append(m)
	s = ''
	return s.join(full_message)

 # Decrypting Alogrithms
def CaesarD(mode, message, key):
	max_k = 26
	translated = ''
	key = -key
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			translated += chr(num)
		else:
			translated += symbol
	return translated

def SubstitutionCipherD(mode, message, key):
	alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	message = message.lower()
	message = list(message)
	key = list(key)
	full_message = []
	for m in message:	
		if m == ' ':
			full_message.append(m)
		elif m in key:
			for item in key:
				if m == item:
					match = key.index(item)
					code = alph[match]
					full_message.append(code)
		else:
			full_message.append(m)
	s = ''
	return s.join(full_message)
	if mode[0] == 'd' or 'D' or 'Decrypt' or 'decrypt':
		key = -key