import string as s
from secrets import SystemRandom as SR

sr = SR()
random_string = ''.join(sr.choices( s.ascii_letters + s.digits + s.punctuation,k=64))

print(random_string)