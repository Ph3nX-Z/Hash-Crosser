import hashlib
import binascii
import time

final_hash=""

a="""
 ▄  █ ██      ▄▄▄▄▄    ▄  █     ▄█▄    █▄▄▄▄ ████▄    ▄▄▄▄▄    ▄▄▄▄▄   ▄███▄   █▄▄▄▄ 
█   █ █ █    █     ▀▄ █   █     █▀ ▀▄  █  ▄▀ █   █   █     ▀▄ █     ▀▄ █▀   ▀  █  ▄▀ 
██▀▀█ █▄▄█ ▄  ▀▀▀▀▄   ██▀▀█     █   ▀  █▀▀▌  █   █ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄   ██▄▄    █▀▀▌  
█   █ █  █  ▀▄▄▄▄▀    █   █     █▄  ▄▀ █  █  ▀████  ▀▄▄▄▄▀   ▀▄▄▄▄▀    █▄   ▄▀ █  █  
   █     █               █      ▀███▀    █                             ▀███▀     █   
  ▀     █               ▀               ▀                                       ▀    
       ▀                                       
By Ph3nX-Z : https://github.com/Ph3nX-Z/

"""
print(a)

word=input("Your Password To hash >>")
print("\n")
salt="db"
salted=hashlib.sha3_512(salt.encode())
salted=salted.hexdigest()

md5=hashlib.md5(word.encode())
md52=md5.hexdigest()
print("[+] MD5  Hash : {}".format(md52))

sha1=hashlib.sha1(word.encode())
sha12=sha1.hexdigest()
print("[+] SHA1 Hash : {}".format(sha12))

ntlm=hashlib.new('md4', word.encode('utf-16le')).digest()
ntlm2=binascii.hexlify(ntlm).decode("utf8")
print("[+] NTLM Hash : {}".format(ntlm2))

print("\n")

for letter in salted[8:16]:
    md52+=letter
for letters in salted[16:20]:
    ntlm2+=letters
for letter2 in salted[0:4]:
    ntlm2+=letter2


index=0
for index in range(0,40,1):
    to_add=ntlm2[index]+sha12[index]+md52[index]
    final_hash+=to_add

final_hash=final_hash[::-1]
final_hash_marked="<--$Ph3nX-Z$"+final_hash+"-->"
print("[+] CROS Hash : "+final_hash_marked)
f=open("hash.txt",'a')
data="password : "+word+"\n"+"CROS Hash : "+final_hash_marked+"\n"+" NTLM Hash : "+ntlm2+"\n"+" MD5  Hash : "+md52+"\n"+" SHA1 Hash : "+sha12+"\n"+'\n'
f.write(data)
f.close()
time.sleep(3)
print("[+] Hashs Successfully Written in hash.txt")
print("\n"+"[+] Ended")
time.sleep(2)