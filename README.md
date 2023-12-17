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
    sudo mkdir /var/webvapt
    mv -r webvapt/* /var/webvapt
    git clone https://github.com/drwetter/testssl.sh.git /var/webvapt/modules/testssl
	git clone https://github.com/scipag/vulscan /usr/share/nmap/scripts/vulscan
        
**step 2:** install python libraries.

    sudo pip3 install -r /var/webvapt/conf/requirements.txt

**step 3:** Install Tools

    sudo apt update && apt install wapiti uniscan nmap nikto commix git dirsearch python3-pip -y

**step 4** Create a symbolic-link
    
    sudo ln -s /var/webvat/webvapt.py /usr/local/bin/webvapt
    sudo chmod +x /usr/local/bin/webvapt
    
**step 5** Run WebVAPT
    just type:
    
    webvapt
    

## Using setup.sh

**step 1:** Give the file execute permissions

    wget https://raw.githubusercontent.com/paciente23256/webvapt/main/setup.sh
    chmod +x setup.sh
    ./setup.sh
    
**step 2:** Run WebVAPT

    webvapt


## WebVAPT Screenshots
**[screenshots]**
<center><img src="https://raw.githubusercontent.com/paciente23256/webvapt/main/images/webvapt_screenshot.png">
</center>


