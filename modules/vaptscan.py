#!/usr/bin/env python3
#@paciente23256


import conf.conf as conf
import time
import os
os.path.abspath("reports/vapt/")

# VAPT Scan




# VA Scan
def vapt_scan():


    # NMAP
    def full_vapt():
        conf.clear()
        logo_ascii = """       
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  

        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● VAPT: ", "white", attrs=["reverse"]) + conf.colored(" Full Web VAPT                             ", "yellow", attrs=["reverse"]))
        #Target
        vapt_host = input(conf.colored("\n  Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        vapt_output = input(conf.colored(f"report path - [default: reports/vapt/{vapt_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(vapt_scan, vapt_host)
        vapt_output = conf.dir_output(vapt_output, "reports/vapt", vapt_host)
        conf.create_dir(vapt_output)
        #start time
        startTime = time.time()         
        
        #full tools 
       
        if len(vapt_host) == 0:
            conf.clear()

            print("opção inválida, tente novamente")
            conf.re_open()

            conf.vapt_host = None
           
           
        else:
            conf.os.system(f"dirsearch -u {vapt_host} --format plain -o  /mnt/c/Users/root/Desktop/webVAPT/reports/vapt/{vapt_host}/dirsearch.txt")
            conf.os.system(f"nmap -sV --script vuln {vapt_host} -vvv -oN  {vapt_output}/nmap_vulnerabilities.txt")
            conf.os.system(f"./modules/testssl/testssl.sh --wide --sneaky --colorblind -U -9 --htmlfile {vapt_output}/testssl.html {vapt_host}")
            conf.os.system(f"wapiti --flush-attack --flush-session --auth-method basic -a test%test -u http://{vapt_host} -m backup,brute_login_form,cookieflags,crlf,csp,csrf,drupal_enum,exec,file,htaccess,htp,http_headers,log4shell,methods,permanentxss,redirect,shellshock,sql,ssl,ssrf,takeover,timesql,wapp,wp_enum,xss,xxe,nikto  -v 2 -dr -f html -o {vapt_output}/wapiti")
            conf.os.system(f"uniscan -qwedsgj -u {vapt_host} | tee {vapt_output}/uniscan_full.txt")
            # nikto is present on wapiti module
            #conf.os.system(f"nikto -T x6 -evasion 7B -usecookies -mutate-options -followredirects -no404 +h {vapt_host} -Display v -Format html -o {vapt_output}/nikto_full.html")
            conf.os.system(f"sqlmap -u {vapt_host} --risk 3 -a --forms --crawl=2 --batch --tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,percentage,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes  | tee {vapt_host}/sqlmap.txt ")
            conf.os.system(f"commix -u http://{vapt_host} --level 2 --all -v 2 --batch --output-dir=/mnt/c/Users/root/Desktop/webVAPT/reports/vapt/{vapt_host}")
            conf.os.system(f"python3 modules/msf/msf.py -j 6 -t {vapt_host}  -f {vapt_output}")


            print(conf.colored("⚠️ ", "yellow", attrs=["bold"]) +  conf.colored(" Note, the scan may take < 1h.\n", "green", attrs=["bold"]))  
          
            print("\n")
            #end time
            print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))



 # MENU
 
    def menu_vapt_scan():
        conf.clear()
        conf.re_open()
    
    logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
    print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))
    print(conf.colored("                                                    ","blue", attrs=["reverse"],))
    print(conf.colored("\n ● Map: ", "white", attrs=["reverse"]) + conf.colored(" 8 Vulnerabilities from NIST & OWASP Top10  ", "yellow", attrs=["reverse"]))
       
       
    #MENU
    print("\n")
    print(conf.colored("\t ●", "white", attrs=["bold"]) +  conf.colored(" Run all VAPT tools:\n", "yellow", attrs=["bold"])) 
    print(conf.colored("\t[dirsearch][nmap][ssltest]\n\t[wapiti][uniscan]\n\t[commix][nikto]\n\t[sqlmap][msf]\n", "green", attrs=["bold"]))  
    print(conf.colored("\t A. ", "white", attrs=["bold"]) +  conf.colored(" massive attack\n", "yellow", attrs=["bold"]))       
    print(conf.colored("----------------------------------------------------","green", attrs=["bold"],))
    print(conf.colored("\tM. ", "white", attrs=["bold"]) +  conf.colored("Main Menu.\n", "yellow", attrs=["bold"]))                               
    print(conf.colored("                                                    ","blue", attrs=["reverse"],))
        
    conf.ans = input(
        conf.colored("\n Choose an option: ","white", attrs=["bold"])).upper()

    if conf.ans == "A":
        conf.call_def(full_vapt, 0)


    elif conf.ans == "M":
        conf.call_def(menu_vapt_scan, 0)
    else:
        conf.not_valid(vapt_scan, conf.ans, 0)
