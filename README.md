# Use-legacy-Blynk-local-server-everywhere-with-plenty-of-energy
A lot of energy with accessibility everywhere using either ngrok, bypassing my IP address (not secure), hivemq...

In this tutorial, I used a Raspberry Pi.
You can also use Windows, Mac, Ubuntu...

Download the Blynk server using this command: "wget http://osoyoo.com/driver/blynk/blynk-server.jar"
Run this command in the directory of the downloaded file: "java -jar ./blynk-server.jar -dataFolder ./Blynk &"
The java server will start in one or two minutes, then you will see following result:
pi@raspberrypi:~/Documents/Blynk_legacy $ java -jar ./blynk-server.jar -dataFolder ./Blynk &
[1] 658
pi@raspberrypi:~/Documents/Blynk_legacy $
Blynk Server 0.41.13-SNAPSHOT successfully started.
All server output is stored in folder '/home/pi/Documents/Blynk_legacy/logs' file.
Now your local Blynk server has been successfully installed and running in your Raspberry Pi. In above picture, we can see our local server IP is 192.168.xx.xx, pleas write down your server IP address for later use.
You can visit the admin page of Blynk Server url:

https://your_RaspberryPi_ip_address:9443/admin
don't forget "https://"
Now, the local Blynk server is running. We go to our old Blynk v1.0 application, create a new account with email and password, and in the three dots, we choose "custom," enter our IP address, and port 9443. Launch the application and add buttons, sliders, etc.


If we want to access our materials from anywhere, we must use a local Blynk server with ngrok, hivemq, IP address, DNS server...
With ngrok, download ngrok using this command after creating an account: 
"curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com bookworm main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok"
After run this command: "ngrok config add-authtoken 2SaGhs9Mr9ZxE8wDZEWVWn0lkzM_5yY6v7nkC1HdWrhZ3cUFE"

After launching ngrok, go to this file and add the following:
"sudo nano .config/ngrok/ngrok.yml" and add this line so that the local blynk server uses the ngrok gateway::
"
version: "2"
authtoken: 2lTGCOPytKzwgMcJkQZEn4Rpaoa_7mXVpbyvDdXFwpkKYKeWG
tunnels:
web:
proto: http
addr: 80
ssh:
proto: tcp
addr: 22
blynk:
proto: tcp
addr: 9443
"
ctl+x, y enter

start "ngrok start blynk" change in blynk app your 2.tcp.ngrok.io and port, connect
in your code, juste ip raspberry pi with port 8080  "blynk = BlynkLib.Blynk(BLYNK_AUTH,server="192.168.2.101",port=8080"
after your raspberry pi accissible anywhere
===================================used ip address================================
go to my router "192.168.2.1", port dcp and tape for port intern 9443 and externe 12345 example. and ip address for my raspberry pi. save
go to my application blynk. user and passe.and tape my address:"74.14.134.254" port "12345" connect


