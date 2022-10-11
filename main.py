import subprocess
#import admin

subprocess.run('powershell -Command "Start-Process cmd -Verb RunAs"')
#NETSH WLAN SET HOSTEDNETWORK MODE=ALLOW SSID=”YOUR WIFI CONNECTION NAME” KEY=”YOUR WIFI CONNECTION PASSWORD”
A=subprocess.run("netsh wlan show profiles", shell=True, capture_output=True)
#subprocess.run("NETSH WLAN SET HOSTEDNETWORK MODE=ALLOW SSID=”ssid name” KEY=”password", shell=True)
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

subprocess.run("NETSH WLAN SET HOSTEDNETWORK MODE=ALLOW SSID=”ssid name” KEY=”password")
