import random
import string

all_characters = string.ascii_letters + string.digits + string.punctuation

length_of_password = int(input("Please enter the length of password: "))
account_of_password = str(input("Please enter the name of the service you are using: "))

password = ''.join(random.choices(all_characters,k=length_of_password))

new_password = 'your password for', account_of_password, 'is', password

log_password = open("password_manager.txt", "a+")

log_password.seek(0)

data = log_password.read(100)

if len(data) > 0:
    log_password.write("\n")

log_password.write(str(new_password))

log_password.close