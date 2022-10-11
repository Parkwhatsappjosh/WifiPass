
import subprocess
import algorithms

A=subprocess.run("netsh wlan show profiles", shell=True, capture_output=True)

result = A.stdout.decode()
f = open("result.txt","w")
f.write(result)
f.close()

g=open("result.txt", "r")
L = g.readlines()
wifiraw = list()
for i in L:
    if 'All User Profile' in i:
        wifiraw.append(i)
wifi = list()
for i in wifiraw:
    A = i.split(':')
    wifi.append(A[1].strip())
        
print(wifi)

subprocess.run('NETSH WLAN SET HOSTEDNETWORK MODE=ALLOW SSID=”JioFi3_187726" KEY=”br7xpjfbev"',shell=True)
process = subprocess.run("Netsh wlan connect ssid=JioFi3_187726 name=JioFi3_187726", shell=True, capture_output=True)
print(process.stdout.decode())
print(algorithms.passgen())

print("New commit")

