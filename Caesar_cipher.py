#function to encrypt
def encrypt(text,shift):
    result = " "
    for i in range (len(text)):
        char = text[i]
        #print("char is ", char) #Check the character being encrypted 
        # Encrypt uppercase characters in plain text
        if (char.isupper()): #if char is upper case Unicode of 'A' (65)
            result += chr((ord(char) + shift-65) % 26 + 65) 
            # ord gives unicode value and chr gives the character representing the unicode value
            #print("result now is ", result) #to print intermediate results
            
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97) #if char is lowercase use Unicode of 'a' (97)
            #print("result now is ", result) #to print intermediate results
    return result

#function to decrypt
def decrypt(cipher,shift):
    result = " "
    for i in range (len(cipher)):
        char = cipher[i]
        #print("char is ", char) #Check the character being encrypted 
        # Encrypt uppercase characters in plain text
        if (char.isupper()): #if char is upper case Unicode of 'A' (65)
            result += chr((ord(char) - shift - 65) % 26 + 65) 
            # ord gives unicode value and chr gives the character representing the unicode value
            #print("result now is ", result) #to print intermediate results
            
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97) #if char is lowercase use Unicode of 'a' (97)
            # print("result now is ", result) #to print intermediate results
    return result

#check the encrypt function
text = str(input("Enter your text to encrypt : "))
shift = int(input ("Enter shift(number between 1 and 26 ) for Caesar Cipher : "))

print ("Plain Text : " + text)
print ("Shift pattern : " + str(shift))
print ("Cipher: " + encrypt(text,shift))

#check the decrypt function
cipher_text = str(input("Enter your ciphertext to decrypt : "))
shift = int(input("Enter shift(number between 1 and 26 ) used for encrypting Caesar Cipher : "))

print ("Cipher: " + cipher_text)
print ("Shift pattern : " + str(shift))
print ("Plain Text: " + decrypt(cipher_text,shift))

