max_passwords_generated=100000000000000000000000000000000
max_length=5
min_length=1 #reccommended is 8 long as its standard now
wait_time=0.0001
rest=1
from multiprocessing import Process
passwords=[]
import itertools
import time
chars="ABCDEFGHIJLKMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`! @#$%^&*()_-+={[}]|:;"+'"'+"'"+"<,>.?/"
charslist=[]
for a in chars:
    charslist.append(a)
def iter_all_strings(a):
    for size in itertools.count(a):
        for s in itertools.product(charslist, repeat=size):
            yield "".join(s)
def do_brute(maxp,minl,maxl):
    print(maxp)
generated=0
for a in range(min_length,max_length):
    passwords_generated=0
    for s in iter_all_strings(a):
        passwords.append(f"{passwords_generated+1} sep {s}")
        if s=="/"*a or max_passwords_generated<=generated:
            print(f"{passwords_generated} paswords with a length of {a}")
            break
        generated+=1
        if generated%1500000==0:
            print(f"Generated {passwords_generated} passwords")
            time.sleep(rest)
        passwords_generated+=1
        time.sleep(wait_time)
    time.sleep(5)
    if max_passwords_generated<=generated:
        break
with open("pwdatabase.txt","w") as f:
    f.write("\n".join(passwords))
print("Complete")
