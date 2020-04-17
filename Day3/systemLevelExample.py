import subprocess, re

process = subprocess.Popen("ipconfig", stdout = subprocess.PIPE, stderr = subprocess.PIPE)
out = process.communicate()

a=out[0]
b=a.decode("utf-8").replace("\r\n", "###")
c=b.split('###')

for i in c:
    if(type(i) is str):
        if i != "":
            print("printing value of i ", i)
            ip=re.findall(r'[0-9]+(?:\.[0-9]+){3}', i)
print(ip)