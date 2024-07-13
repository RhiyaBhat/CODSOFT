import random
import string

password=string.ascii_letters+string.digits+string.punctuation

print("Password generator:")
#User asked to enter password length
length=int(input("Enter the length of the password to be generated:"))

password="".join(random.choices(password, k=length))

#Printing generated password
print("Your password is:",password)