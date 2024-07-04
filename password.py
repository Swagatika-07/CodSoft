import random

lowercase_letter="abcdefghijklmnopqrstuvwxyz"
uppercase_letter=lowercase_letter.upper()
numerics="0123456789"
symbols= "(){|}[]~!@#$%^&*_-`:;/.,?><'"


all =''+lowercase_letter+uppercase_letter+numerics+symbols

length=int(input("Enter the length of the password: "))

for x in range(1):
    password="".join(random.sample(all,length))
    print(f"Password is {password}")