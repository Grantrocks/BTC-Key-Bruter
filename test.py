import hashlib
with open("pwdatabase.txt") as f:
    pwstr=f.read()
    pwstr=pwstr.split("\n")
print("Loaded passwords")
print("Please specify what encyrption method to use:")
method=input("1: SHA256\n2: SHA1\n>")
read=0
tpw=input("Password hash: ")
for a in pwstr:
    pw=a.split(" sep ")
    if method=="1":
        phash=hashlib.sha256(pw[1].encode()).hexdigest()
    elif method=="2":
        phash=hashlib.sha1(pw[1].encode()).hexdigest()
    if tpw==phash:
        print(f"FOUND IT! Your password is: {pw[1]}\nIndex in the database: {pw[0]}")
        break
print("If your password is above it was in the database")