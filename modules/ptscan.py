#!/usr/bin/env python3
#@paciente23256


import conf.conf as conf
import time
import os
os.path.abspath("/var/webvapt/reports/pt/")

# PT Scan
def pt_scan():

    # Metasploit
       

    def msf_v1():
        conf.clear()
        logo_ascii = """       
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  

        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● MSF : ", "white", attrs=["reverse"]) + conf.colored(" Web Pentest with Metasploit               ", "yellow", attrs=["reverse"]))
        #Alvo
        msf_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"])) 
        msf_output = input(conf.colored(f"Report path  - [default: /var/webvapt/reports/pt/{msf_host}]: ","green", attrs=["bold"],))
        conf.not_valid(pt_scan, msf_host)
        msf_output = conf.dir_output(msf_output, "/var/webvapt/reports/pt/", msf_host)
        conf.create_dir(msf_output)
        # metasploit
        conf.os.system(f"python3 /var/webvapt/modules/msf/msf.py -j 5 -t {msf_host} -f {msf_output}")
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))         


    def sqlmap_auto():
        conf.clear()
        logo_ascii = """       
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  

        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● SQLMAP : ", "white", attrs=["reverse"]) + conf.colored(" Web Pentest with Sqlmap                ", "yellow", attrs=["reverse"]))
        #Alvo  
        sqlmap_host = input(conf.colored("\nInsert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"])) 
        sqlmap_output = input(conf.colored(f"report path  - [default: /var/webvapt/reports/pt/{sqlmap_host}]: ","green", attrs=["bold"],))
        conf.not_valid(pt_scan, sqlmap_host)
        sqlmap_output = conf.dir_output(sqlmap_output, "/var/webvapt/reports/pt/", sqlmap_host)
        conf.create_dir(sqlmap_output)
        # SQLMAP
        conf.os.system(f"sqlmap -u{sqlmap_host} --level 3 --risk 3 -a --forms --crawl=5 --batch --tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,percentage,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes  | tee {sqlmap_output}/sqlmap.txt ")
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))         

        

    def commix_v1():
        conf.clear()
        logo_ascii = """       
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  

        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● COMMINX : ", "white", attrs=["reverse"]) + conf.colored(" Web Pentest with Comminx              ", "yellow", attrs=["reverse"]))
        #Alvo  
        commix_host = input(conf.colored("\n nsert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"])) 
        commix_output = input(conf.colored(f"report path  - [default: /var/webvapt/reports/pt/{commix_host}]: ","green", attrs=["bold"],))
        conf.not_valid(pt_scan, commix_host)
        commix_output = conf.dir_output(commix_output, "/var/webvapt/reports/pt/", commix_host)
        conf.create_dir(commix_output)
        # commix
        #conf.os.system(f"commix -u http://{commix_host} --level 3 --all -v 2 --batch --output-dir={commix_output}")
        # it was not possible to force this path, change according to your reality
        conf.os.system(f"commix -u http://{commix_host} --level 3 --all -v 2 --batch --output-dir=/var/webvapt/reports/pt/{commix_host}")
        
        
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))         


        

    def full_pt():
        conf.clear()
        logo_ascii = """       
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  

        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● ALL : ", "white", attrs=["reverse"]) + conf.colored(" Full Web Pentest                         ", "yellow", attrs=["reverse"]))
        #Alvo    
        full_host = input(conf.colored("\nInsert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"])) 
        full_output = input(conf.colored(f"report path  - [default: /var/webvapt/reports/pt/{full_host}: ","green", attrs=["bold"],))
        conf.not_valid(pt_scan, full_host)
        full_output = conf.dir_output(full_output, "/var/webvapt/reports/pt/", full_host)
        conf.create_dir(full_output)
        #start time
        startTime = time.time() 
        
        if len(full_host) == 0:
            conf.clear()

            print("opção inválida, tente novamente")
            conf.re_open()

            conf.full_host = None

   
        #full pt tools 
        
        else:
            conf.os.system(f"python3 /var/webvapt/modules/msf/msf.py -j 5 -t {full_host}  -f {full_output}")
            conf.os.system(f"sqlmap -u {full_host} --level 3 --risk 3 -a --forms --crawl=5  --batch --tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,percentage,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes  | tee {full_output}/full_sqlmap.txt ")
            # It was not possible to force this path, change according to your reality
            conf.os.system(f"commix -u http://{full_host} --level 3 --all -v 2 --batch --output-dir=/var/webvat/reports/pt/{full_host}")
      
        print("\n")
        #end time
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))



    # MENU
 
    def menu_pt_scan():
        conf.clear()
        conf.re_open()
    
    logo_ascii = """      

           ___ __       _   ______ 
     (   /(_  / _) (  //_| /__)/   
     |/|/ /__/(_)  |_/(  |/   (    
     
 Web Security Blackbox Testing with VAPT
     
     
    """
    print(conf.colored(f"{logo_ascii}", "blue"))
    print(conf.colored("                                                    ","blue", attrs=["reverse"],))
    print(conf.colored("\n ● Map: ", "white", attrs=["reverse"]) + conf.colored(" 8 Vulnerabilities from NIST & OWASP Top10  ", "yellow", attrs=["reverse"]))
       
       
    #MENU
    print(conf.colored("\n ● METASPLOIT", "white", attrs=["bold"]))
    print(conf.colored(" 1. ", "white", attrs=["bold"]) +  conf.colored("Run All Tests with [metasploit]", "yellow", attrs=["bold"]))
    print(conf.colored("\n ● SQLMAP", "white", attrs=["bold"]))
    print(conf.colored(" 2. ", "white", attrs=["bold"]) +  conf.colored("Run All Tests with [sqlmap]", "yellow", attrs=["bold"]))
    print(conf.colored("\n ● Commix ", "white", attrs=["bold"]))
    print(conf.colored(" 3 ", "white", attrs=["bold"]) +  conf.colored("Run All Tests with [commix]\n", "yellow", attrs=["bold"]))
    print(conf.colored("\t ● ALL \n", "white", attrs=["reverse"]))
    print(conf.colored("\tA. ", "white", attrs=["bold"]) +  conf.colored("Run all tools", "yellow", attrs=["bold"]))  
    print(conf.colored("----------------------------------------------------","green", attrs=["bold"],))
    print(conf.colored("\t M. ", "white", attrs=["bold"]) +  conf.colored("Main Menu.\n", "yellow", attrs=["bold"]))                               
    print(conf.colored("                                                    ","blue", attrs=["reverse"],))
        
    conf.ans = input(
        conf.colored("\n Choose an option: ","white", attrs=["bold"])).upper()

    if conf.ans == "1":
        conf.call_def(msf_v1, 0)
    elif conf.ans == "2":
        conf.call_def(sqlmap_auto, 0)
    elif conf.ans == "3":
        conf.call_def(commix_v1, 0)
    elif conf.ans == "A":
        conf.call_def(full_pt, 0)
 
    elif conf.ans == "M":
        conf.call_def(menu_pt_scan, 0)
    else:
        conf.not_valid(pt_scan, conf.ans, 0)

 
        

