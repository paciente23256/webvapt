# WebVAPT - Web Application Security Audit
###  Web Security Blackbox Testing with VAPT

<center><img src="https://raw.githubusercontent.com/paciente23256/webvapt/main/images/logo.png">
</center>

<a target="_blank" href="https://en.wikipedia.org/wiki/Python_(programming_language)">
<img src="https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11&color=informational&logo=python"/>
</a>
<p></p>

### WebVAPT it´s a framework that automates and parameterizes well-known VAPT tools by modeling the attack, for Web applications, through the mapping of eight vulnerabilities obtained from NIST and OWASP.

     
## Manual Setup in Kali 

**step 1:** Download and Setup webvapt. 

    sudo git clone https://github.com/paciente23256/webvapt.git /var/webvapt
    sudo git clone https://github.com/drwetter/testssl.sh.git /var/webvapt/modules/testssl
    sudo chmod +x /var/webvapt/modules/testssl/testssl.sh
    sudo git clone https://github.com/scipag/vulscan /usr/share/nmap/scripts/vulscan
        
**step 2:** Install tools

    sudo apt-get update && apt-get install wapiti uniscan nmap nikto commix git dirsearch python3 python3-pip -y
    
   
**step 3:**  Install python libraries.

    sudo pip3 install -r /var/webvapt/conf/requirements.txt

**step 4:** Create a symbolic-link
    
    sudo ln -s /var/webvat/webvapt.py /usr/local/bin/webvapt
    sudo chmod +x /usr/local/bin/webvapt
    
**step 5:** Run WebVAPT
    just type:
    
    sudo webvapt
    

## Using setup.sh

**step 1:** Download and execute setup

     sudo wget -O - https://raw.githubusercontent.com/paciente23256/webvapt/main/setup.sh | bash
     
**step 2:** Run WebVAPT
     just type

    sudo webvapt


## WebVAPT Screenshots
**[screenshots]**
<center><img src="https://raw.githubusercontent.com/paciente23256/webvapt/main/images/webvapt_screenshot.png">
</center>


