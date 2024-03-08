import art

print(art.logo)
plain_text = input("Enter the plaintext: ") # original text to be encrypted
cipher_text = '' # scrumbled text that is encrypted
key = 3 # by default Ceaser cipher algorithm takes a key of value 3

# You are free to customize the key always to a number ranging from (0, 25)
 
'''
Customizing the key will require you to modify the code to restict the values between a range of (0, 25)
past that or below that range should return an error message or warning output

'''

# Note that if you pick 0 the ciphertext will be same as the plaintext

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in plain_text.lower():
	if char == ' ':
		print(bool(1))

	else:
		plaintext_index = alphabet.find(char)
		ciphertext_index = plaintext_index + key % 26
		cipher_text += alphabet[ciphertext_index]
		print(f"Plaintext character is {char} and the ciphertext character {cipher_text.upper()}")


print(art.logo)