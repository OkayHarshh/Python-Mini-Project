import random
import string

passLen = int(input("Enter your password length: "))
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(passLen):
    password += random.choice(charValues)


print("Your Password is : ", password )


#OR by List Comprehension

res ="" .join([random.choice(charValues) for i in range(passLen)])
print("Your Password is : ",res )
