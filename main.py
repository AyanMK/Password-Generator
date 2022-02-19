import string
import random
from pip import main

if __name__ == "__main__":
    s1 = string.ascii_lowercase     #(a to z)
    s2 = string.ascii_uppercase     #(A to Z)
    s3 = string.digits              #(0 to 9)
    s4 = string.punctuation         #(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    
    password_length = int(input("Enter password length: \n"))
    
    str = []
    str.extend(list(s1))
    str.extend(list(s2))
    str.extend(list(s3))
    str.extend(list(s4))
    
    #print(str)
    random.shuffle(str)             #shuffling 'str' string list
    #print(str)
    
    print("Your password ----->\n")
    
    print("".join(str[0:password_length]))
    print("".join(random.sample(str,password_length)))
    
    print("\n")