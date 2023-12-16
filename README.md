# WebVAPT - Web Application Security Audit
###  Web Security Blackbox Testing with VAPT

<center><img src="https://raw.githubusercontent.com/paciente23256/webvapt/main/images/logo.png">
</center>

<a target="_blank" href="https://en.wikipedia.org/wiki/Python_(programming_language)">
<img src="https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11&color=informational&logo=python"/>
</a>
<p></p>

## Manual Setup in Kali 

**step 1:** Download webvapt. 

    git clone https://github.com/paciente23256/webvapt.git
    cd webvapt
    
**step 2:** install python libraries

sudo pip3 install -r conf/requirements.txt

**step 3:** Install tools

sudo apt update && apt install wapiti uniscan nmap nikto commix git dirsearch python3-pip -y

**step 4**

sudo python3 webvapt.py

## Using setup sh

**step 1:** Give the file execute permissions

cd webvapt
sudo chmod +x setup.sh
sudo ./setup.sh

**step 2:** Run WebVAPT

just type webvapt

