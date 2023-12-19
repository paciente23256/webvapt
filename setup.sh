#!/usr/bin/env bash

DEPENDENCIES="wapiti uniscan nmap nikto commix git dirsearch python3 python3-pip"

if [ "$(grep -Ei 'debian|buntu|mint' /etc/*release)" ]; then
        sudo rm -rf /var/webvapt
	sudo rm -rf /usr/local/bin/webvapt
	sudo rm -rf /usr/share/nmap/scripts/vulscan
        sudo apt-get install $DEPENDENCIES -y
	sudo git  clone https://github.com/paciente23256/webvapt.git /var/webvapt
        sudo git clone https://github.com/drwetter/testssl.sh.git /var/webvapt/modules/testssl
	sudo git clone https://github.com/scipag/vulscan /usr/share/nmap/scripts/vulscan
	sudo chmod +x /var/webvapt/modules/testssl/testssl.sh
        sudo pip3 install -r /var/webvapt/conf/requirements.txt 
	sudo ln -s /var/webvapt/webvapt.py /usr/local/bin/webvapt 
	sudo chmod +x /usr/local/bin/webvapt
	echo ""
	echo "+-----------------------+"
	echo "     [ Setup OK ]"
 	echo "+-----------------------+"
	
elif [ "$(grep -Ei 'redhat|centos' /etc/*release)" ]; then 
    os_version=$(cut -d ':' -f5 < /etc/system-release-cpe)
    if [ "$os_version" == 8 ]; then
        sudo dnf install https://extras.getpagespeed.com/release-el8-latest.rpm -y
        sudo rm -rf /var/webvapt
	sudo rm -rf /usr/local/bin/webvapt/
	sudo rm -rf /usr/share/nmap/scripts/vulscan
        sudo dnf install $DEPENDENCIES -y
	sudo git  clone https://github.com/paciente23256/webvapt.git /var/webvapt
        sudo git clone https://github.com/drwetter/testssl.sh.git /var/webvapt/modules/testssl
	sudo git clone https://github.com/scipag/vulscan /usr/share/nmap/scripts/vulscan
	sudo chmod +x /var/webvapt/modules/testssl/testssl.sh
        sudo pip3 install -r /var/webvapt/conf/requirements.txt 
	sudo ln -s /var/webvapt/webvapt.py /usr/local/bin/webvapt 
	sudo chmod +x /usr/local/bin/webvapt
    elif [ "$os_version" == 7 ]; then
        sudo rpm -Uvh http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-20.el7.art.noarch.rpm
        sudo rpm  -Uvh http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-21.art.noarch.rpm
        sudo rpm -Uvh  http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-21.art.noarch.rpm
        sudo rm -rf /var/webvapt
	sudo rm -rf /usr/local/bin/webvapt/
	sudo rm -rf /usr/share/nmap/scripts/vulscan
        sudo yum install $DEPENDENCIES -y
	sudo git  clone https://github.com/paciente23256/webvapt.git /var/webvapt
        sudo git clone https://github.com/drwetter/testssl.sh.git /var/webvapt/modules/testssl
	sudo git clone https://github.com/scipag/vulscan /usr/share/nmap/scripts/vulscan
	sudo chmod +x /var/webvapt/modules/testssl/testssl.sh
        sudo pip3 install -r /var/webvapt/conf/requirements.txt 
	sudo ln -s /var/webvapt/webvapt.py /usr/local/bin/webvapt 
	sudo chmod +x /usr/local/bin/webvapt
    fi  
fi
