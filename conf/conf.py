#!/usr/bin/env python3
# @paciente23256

import os
import socket
import sys
import glob
import requests
from art import *
from termcolor import colored
import time



from modules.vascan import va_scan
from modules.ptscan import pt_scan
from modules.vaptscan import vapt_scan
from modules.report import reports
from modules.exit import exit



ans = True
version = "1.1"
home = os.path.expanduser("~")


def re_open():
    installed = True if os.path.exists("/usr/local/bin/webvapt") else False

    if installed:
        os.system("sudo webvapt")
        sys.exit()

    else:
        os.system("sudo python3 webvapt.py")
        sys.exit(())


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def not_valid(func, var, num=1):
    num = True
    if num == True:
        if len(var) <= 5:
            clear()

            print(colored("\nInvalid option, try again.\n", "red", attrs=["reverse"]))
            func()
    else:
        clear()

        print(colored("\nInvalid option, try again.\n", "red", attrs=["reverse"]))
        func()


def dir_output(var, path, url):
    if len(var) == 0:
        var = path + "/" + url
        return var


def call_def(func, num=1):
    if num == True:
        clear()
        ans = True
        while ans:
            func()
    else:
        clear()
        func()


def ver_check():
    ver_url = "https://raw.githubusercontent.com/paciente23256/webvapt/main/conf/version.txt"
    try:
        ver_rqst = requests.get(ver_url)
        ver_sc = ver_rqst.status_code
        if ver_sc == 200:
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()

            if version == github_ver:
                print(colored("  WebVAPT version is update.\n", "yellow", attrs=["reverse"],))
            else:
                print(colored(f"  The WebVAPT version is not update, there is a new version: {format(github_ver)} \n", "yellow", attrs=["reverse"],))
        else:
            print("[ License status: {} ".format(ver_sc) + "]" + "\n")
    except Exception as e:
        print("\n" + "[-] Exception : " + str(e))
