import random

lower="abcdefghijklmnnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="123456789"
symbols="{}[]\/*&$#@"
use_all=lower+upper+numbers+symbols
length=8
password="".join(random.sample(use_all,length))
print("The system generated password is:",password)
