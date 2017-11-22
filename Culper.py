#Culper Cipher
#A fun experiment in coding by Kevin Ruth
#11/21/2017

#Cipher dictionary
cipher = {"A":"e",
          "B":"f",
          "C":"g",
          "D":"h",
          "E":"i",
          "F":"j",
          "G":"a",
          "H":"b",
          "I":"c",
          "J":"d",
          "K":"o",
          "L":"m",
          "M":"n",
          "N":"p",
          "O":"q",
          "P":"r",
          "Q":"k",
          "R":"l",
          "S":"u",
          "T":"v",
          "U":"w",
          "V":"x",
          "W":"y",
          "X":"z",
          "Y":"s",
          "Z":"t",
          "1":"E",
          "2":"F",
          "3":"G",
          "4":"I",
          "5":"K",
          "6":"M",
          "7":"N",
          "8":"O",
          "9":"Q",
          "0":"U",
          }

#Message to be encrypted - saving as variable and capitalizing
msg = input("Message to encrypt = ").upper()

#Empty list to collect translated characters
rply_list = []

"""
for loop which goes through the characters in the message and sees if 
that character is a key value in the cipher dictionary. If it is, it
translates it to the designated value. If not, it keeps the character
the same (in order to deal with blank spaces and special characters).
This translated characters are then appended to the end of the blank 
reply message list and then the loop repeats until the end
"""
for character in msg:
	if character in cipher.keys():
		rply_list.append(cipher.get(character))
	else:
		rply_list.append(character)

"""
Combines all of the entries in the reply message list to be a single
string
"""
rply = "".join(rply_list)

"""
Prints the encrypted reply
"""
print(rply)
