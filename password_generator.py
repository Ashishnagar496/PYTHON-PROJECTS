import random 
import string
import os 
def password_generator(length):
    alphabet=string.ascii_letters + string.digits + string.punctuation + string.octdigits + string.hexdigits
    password="".join(random.choice(alphabet) for i in range(length))
    return password 


try:
    platform = input("Enter the name for the password you want to save: ")
    directory = input("enter the directory path : ")
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, f"{platform}.txt")

    x = int(input("Enter the length of the password needed: "))
    password = password_generator(x)
    print(f"{password}")
    print("'harder than steel'")
    with open(filename, "w") as file:
        file.write(f"{password}")
    print(f"File saved at {directory}\\")
except ValueError:
    print("enter a valid input")



