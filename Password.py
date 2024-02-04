# The idea is to create a password generator in python 
import secrets
import string 
import random 

 #the password must contain lowercase, uppercase, numbers and sp characters

letters=string.ascii_letters # combination of UC and LC letters
digits=string.digits #Makes a string of digits

sp_chars=string.punctuation
selection_list= letters+digits+sp_chars
password_len=8

password=''

for i in range(password_len):
    password+=''.join(secrets.choice(selection_list))
    # adding constraints to the number of special characters used 
    if(any(char in sp_chars for char in password)and sum(char in digits for char in password)>=2):

        break
    print(password)   
