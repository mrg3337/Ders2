import random

char_pool="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password= ""

pass_lenght= int(input("Please enter password lenght:"))

for i in range(pass_lenght):
    password= password+ random.choice(char_pool)

print("Your password is ready!!! :" + password)    
