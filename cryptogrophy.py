
import string 
def encrypt(message): 
    #set encryption key
    alphabet = string.ascii_lowercase
    key ="qwertyuixpasdcghjklzofvbnm"
    #encrypt the message 
    encrypted = ""
    for character in message.lower():
        index = alphabet.find(character)
        encrypted = encrypted + key[index]





    return encrypted 



message = "Storm the walls at Dawn!"
print(encrypt(message))