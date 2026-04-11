#Encryption Prorgram
import string
import random
chars=string.ascii_uppercase + string.punctuation + string.digits + string.ascii_lowercase
chars=list(chars)
key=list.copy(chars)
random.shuffle(key)
plain_text=input("Enter a string: ")
cypher_text=""
for i in plain_text:
    index=chars.index(i)
    cypher_text+=key[index]
print(f"Original message:  {plain_text}")
print(f"Encrypted Message: {cypher_text}")
