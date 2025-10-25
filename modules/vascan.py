#!/usr/bin/env python3
#@paciente23256


import conf.conf as conf
import time
import os
os.path.abspath("/var/webvapt/reports/va/")

# VA Scanhttps://github.com/paciente23256/webvapt/edit/main/modules/vascan.py
def va_scan():


    # NMAP
    def nmap_v1():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NMAP: ", "white", attrs=["reverse"]) + conf.colored(" http web enumeration -p 80,443,8080       ", "yellow", attrs=["reverse"]))
        nmap_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nmap_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nmap_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nmap_host)
        nmap_output = conf.dir_output(nmap_output, "/var/webvapt/reports/va", nmap_host)
        conf.create_dir(nmap_output)       
        #ataque V5
        startTime = time.time()
        conf.os.system(f"dirsearch -u {nmap_host} --format plain -o {nmap_output}/dirsearch_nmap1.txt")
        conf.os.system(f"nmap -sV -p80,443,8080 --script http-enum  {nmap_host} -vv -oN  {nmap_output}/nmap_http-enum.txt")
        
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        print("\n")
        
        #print(conf.colored("                                                    ","blue", attrs=["reverse"],)) 


    def nmap_v2():
    
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NMAP: ", "white", attrs=["reverse"]) + conf.colored(" http common vuln   -p 80,443,8080         ", "yellow", attrs=["reverse"]))
        nmap_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nmap_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nmap_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nmap_host)
        nmap_output = conf.dir_output(nmap_output, "/var/webvapt/reports/va/", nmap_host)
        conf.create_dir(nmap_output)       
        #ataque V2
        startTime = time.time()
        conf.os.system(f"nmap -sV -p 80,443,8080 --script http-backup-finder,http-cors,http-headers,http-csrf,http-aspnet-debug,http-cross-domain-policy,http-phpself-xss,http-php-version,http-webdav-scan,http-waf-detect,http-xssed   {nmap_host} -vv -oN  {nmap_output}/nmap_http-common.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        
       


    def nmap_all():
    
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NMAP: ", "white", attrs=["reverse"]) + conf.colored(" http vulnerabilities   -p all             ", "yellow", attrs=["reverse"]))
        nmap_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nmap_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nmap_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nmap_host)
        nmap_output = conf.dir_output(nmap_output, "/var/webvapt/reports/va/", nmap_host)
        conf.create_dir(nmap_output)       
        #ataque V3
        startTime = time.time()
        conf.os.system(f"nmap -sV --script vuln,vulners,vulscan/vulscan,http-enum  {nmap_host} -Pn -vv -oN  {nmap_output}/nmap_vulners_enum_all.txt")
        conf.os.system(f"nmap -sV -p 80,443,8080 --script http-backup-finder,http-cors,http-headers,http-csrf,http-aspnet-debug,http-cross-domain-policy,http-phpself-xss,http-php-version,http-webdav-scan,http-waf-detect,http-xssed   {nmap_host} -Pn -vv -oN  {nmap_output}/nmap_http-common_all.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        
        




    # SSL.Test
    def ssl_sh():
    
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● SSLTEST :", "white", attrs=["reverse"]) + conf.colored(" Full SSL/TLS and cert Tests            ", "yellow", attrs=["reverse"]))  
        # Alvo
        sslsh_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        sslsh_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{sslsh_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, sslsh_host)
        sslsh_output = conf.dir_output(sslsh_output, "/var/webvapt/reports/va/", sslsh_host)
        conf.create_dir(sslsh_output)       
        #ataque V5
        startTime = time.time()
        conf.os.system(f"/var/webvapt/modules/testssl/testssl.sh --wide --sneaky --colorblind -U -9  --htmlfile {sslsh_output}/testssl.html {sslsh_host}")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        
        
        


    # WAPITI
        
    def wapiti_v1():
    
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" V1-XSS-A7-OWASP-2017                     ", "yellow", attrs=["reverse"]))
        # Alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # Report 
        wapiti_output = input(conf.colored(f"Pasta de Saida do relatório  - [default: /var/webvapt/reports/va/{wapiti_host}]: ","green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
                
        # parametrização da ferramenta
        startTime = time.time()
        conf.os.system(f"wapiti --flush-attack -u http://{wapiti_host} -m xss,permanentxss -v 2 -f txt -o {wapiti_output}/wapiti_v1.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
                
        
    #Vulnerabilidade 2 - Injection 
    def wapiti_v2(): 
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" V2-INJECTION-A1:2017                     ", "yellow", attrs=["reverse"]))
        # alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # pasta do relatorio
        wapiti_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{wapiti_host}]: ","green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
        # V2 ataque - parametrização da ferramenta
        startTime = time.time()
        conf.os.system(f"wapiti --flush-attack -u http://{wapiti_host} -m sql,blinsql,xxe,exec,crlf -v 2 -f txt -o {wapiti_output}/wapiti_v2.txt")
        print("\n")           
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        
    #Vulnerabilidade 3 
    def wapiti_v3():   
     
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" V3-Broken Authentication-A2:2017         ", "yellow", attrs=["reverse"]))     
        # Alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # pasta do relatorio
        wapiti_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{wapiti_host}]: ", "green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
        # V3 ataque - parametrização da ferramenta
        startTime = time.time()
        conf.os.system(f"wapiti --flush-attack -u http://{wapiti_host} -m brute_login_form --auth-type basic -a test%test -v 2 -f txt -o {wapiti_output}/wapiti_v3.txt")
        print("\n")         
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        
    #Vulnerabilidade 4
    def wapiti_v4():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" V4-Security Misconfiguration-A6:2017     ", "yellow", attrs=["reverse"]))     
        # Alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # pasta do relatorio
        wapiti_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{wapiti_host}]: ", "green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
        # V4 ataque - parametrização da ferramenta
        startTime = time.time()
        conf.os.system(f"wapiti --flush-attack -u http://{wapiti_host} -m wapp,methods,http_headers,htaccess,backup,brute_login_form,csrf,csp,ssrf -v 2 -f txt -o {wapiti_output}/wapiti_v4.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
                
           
    #Vulnerabilidade 5    
    def wapiti_v5():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" V5-Sensitive Data Exposure - A3:2017     ", "yellow", attrs=["reverse"]))     
        # Alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # Report 
        wapiti_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{wapiti_host}]: ", "green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
        # V3 ataque - parametrização da ferramenta
        startTime = time.time()
        conf.os.system(f"wapiti --flush-attack -u http://{wapiti_host} -m redirect,methods,htaccess,wapp,backup,shellshock,buster,ssrf -v 2 -f txt -o {wapiti_output}/wapiti_v5.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))

   
    #Vulnerabilidade 6    
    def wapiti_v6():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" V6- Malicious File Inclusion             ", "yellow", attrs=["reverse"]))  
        # Alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # pasta do relatorio
        wapiti_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{wapiti_host}]: ", "green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
        startTime = time.time()

        # V6 ataque - parametrização da ferramenta
        conf.os.system(f"wapiti --flush-attack -u http://{wapiti_host} -m exec,file,xxe,clrf,ssrf  -v 2 -f txt -o {wapiti_output}/wapiti_v6.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        
    #Vulnerabilidade 7    
    def wapiti_v7():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" V7-Cross Site Request Forgery            ", "yellow", attrs=["reverse"]))  
        # Alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # pasta do relatorio
        wapiti_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{wapiti_host}]: ", "green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
        startTime = time.time()
        # V7 ataque - parametrização da ferramenta
        conf.os.system(f"wapiti --flush-attack -u http://{wapiti_host} -m csrf,clrf,ssrf,redirect  -v 2 -f txt -o {wapiti_output}/wapiti_v7.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
    
    #Vulnerabilidade 8
    def wapiti_v8():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" V8 - Insecure Communications - A3:2017   ", "yellow", attrs=["reverse"]))  
        # Alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # Report 
        wapiti_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{wapiti_host}]: ", "green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
        startTime = time.time()
        # V8 ataque - parametrização da ferramenta
        conf.os.system(f"wapiti --flush-attack -u http://{wapiti_host} -m methods,http_headers,cookieflags,shellshock --verify-ssl 1 -v 2  -f txt -o {wapiti_output}/wapiti_v8.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
 
    def wapiti_all():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● WAPITI:", "white", attrs=["reverse"]) + conf.colored(" All Vulnerabilities                      ", "yellow", attrs=["reverse"]))  
        # Alvo
        wapiti_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        # Report 
        wapiti_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{wapiti_host}]: ", "green", attrs=["bold"],))
        conf.not_valid(va_scan, wapiti_host)
        wapiti_output = conf.dir_output(wapiti_output, "/var/webvapt/reports/va/", wapiti_host)
        conf.create_dir(wapiti_output)
        startTime = time.time()
        # parametrização da ferramenta

        conf.os.system(f"wapiti  --flush-attack  -u https://{wapiti_host} -m buster,backup,cookieflags,crlf,csp,exec,xxe,xss,file,htaccess,http_headers,methods,permanentxss,redirect,shellshock,ssrf,wapp,brute_login_form  --verify-ssl 1 --auth-type basic -a test%test  -v 2  -f html -o {wapiti_output}/wapiti_all")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))

        
 
    #Nikto V1
    def nikto_v1():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" V1-XSS-A7-OWASP-2017                     ", "yellow", attrs=["reverse"])) 
        # Alvo
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)
        startTime = time.time()
        #V1 - xss
        conf.os.system(f"nikto -T 4 -usecookies -evasion 7B -mutate-options -followredirects +h {nikto_host} -Display v -Format htm -o {nikto_output}/nikto_v1.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))

        
    #Nikto V2
    def nikto_v2():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" V2-INJECTION-A1:2017                     ", "yellow", attrs=["reverse"]))
        # alvo
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)
        startTime = time.time()
        #ataque V2 
        conf.os.system(f"nikto -T 4589c -evasion 7B -mutate-options -followredirects +h {nikto_host} -Display v -Format htm -o {nikto_output}/nikto_v2.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
 
  
    #Nikto V2
    def nikto_v3():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" V3-Broken Authentication-A2:2017         ", "yellow", attrs=["reverse"]))     
        # Alvo
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)    
        startTime = time.time()
        #V3 
        conf.os.system(f"nikto -usecookies -Plugin auth -T a -evasion 7B -mutate-options -followredirects +h {nikto_host} -Display v -Format htm  -o  {nikto_output}/nikto_v3.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
 
    #Nikto V4
    def nikto_v4():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" V4-Security Misconfiguration-A6:2017     ", "yellow", attrs=["reverse"]))     
        # Alvo
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)
        startTime = time.time()
        #V4
        conf.os.system(f"nikto -usecookies -T 123b -evasion 7B -mutate-options -followredirects +h {nikto_host} -Display v -Format htm  -o {nikto_output}/nikto_v4.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))

    
    #Nikto V5
    def nikto_v5():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" V5-Sensitive Data Exposure - A3:2017     ", "yellow", attrs=["reverse"]))     
        # Alvo  
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)       
        startTime = time.time()
        #ataque V5
        conf.os.system(f"nikto -usecookies -Plugin EXTRAS -evasion 7B -mutate-options -followredirects +h {nikto_host} -Display v -Format htm -o {nikto_output}/nikto_v5.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
 
     #Nikto V6
    def nikto_v6():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" V6- Malicious File Inclusion             ", "yellow", attrs=["reverse"]))  
        # Alvo
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)       
        startTime = time.time()
        #ataque V6
        conf.os.system(f"nikto -T 058ce -Plugin EXTRAS -evasion 7B -mutate-options -followredirects +h {nikto_host} -Display v -Format htm  -o  {nikto_output}/nikto_v6.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        
        
        
    #Nikto V7
    def nikto_v7():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" V7-Cross Site Request Forgery            ", "yellow", attrs=["reverse"]))  
        # Alvo
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)       
        startTime = time.time()
        #ataque V7
        conf.os.system(f"nikto -T 7 -evasion 7B -mutate-options -followredirects +h {nikto_host} -Display v -Format htm  -o  {nikto_output}/nikto_v7.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
  
  
      #Nikto V8
    def nikto_v8():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" V8 - Insecure Communications - A3:2017   ", "yellow", attrs=["reverse"]))  
        # Alvo 
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)       
        startTime = time.time()
        #ataque V8
        conf.os.system(f"nikto -usecookies -Plugin tests -evasion 7B -mutate-options -followredirects +h {nikto_host} -Display v -Format htm -o {nikto_output}/nikto_v8.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        
        
      #Nikto All
    def nikto_all():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● NIKTO :", "white", attrs=["reverse"]) + conf.colored(" All Vulnerabilities                      ", "yellow", attrs=["reverse"]))  
        #Alvo
        nikto_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        nikto_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{nikto_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, nikto_host)
        nikto_output = conf.dir_output(nikto_output, "/var/webvapt/reports/va/", nikto_host)
        conf.create_dir(nikto_output)       
        startTime = time.time()
        #ataque all
        conf.os.system(f"nikto -T x6 -evasion 7B -mutate-options -followredirects -no404 +h {nikto_host} -Display v -Format htm -o {nikto_output}/nikto_all.htm")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))




#UNISCAN


    def uniscan_v1():
    
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● UNISCAN :", "white", attrs=["reverse"]) + conf.colored(" Brute files and Directories            ", "yellow", attrs=["reverse"]))  
        # Alvo 
        uniscan_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        uniscan_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{uniscan_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, uniscan_host)
        uniscan_output = conf.dir_output(uniscan_output, "/var/webvapt/reports/va/", uniscan_host)
        conf.create_dir(uniscan_output)       
        startTime = time.time()
        #ataque 1
        conf.os.system(f"uniscan -geqw -u {uniscan_host} | tee {uniscan_output}/uniscan_dir_files.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))




    def uniscan_v2():
    
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● UNISCAN :", "white", attrs=["reverse"]) + conf.colored(" XSS, SQLi, BSQLi & Other Checks.       ", "yellow", attrs=["reverse"]))  
        # Alvo 
        uniscan_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        uniscan_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{uniscan_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, uniscan_host)
        uniscan_output = conf.dir_output(uniscan_output, "/var/webvapt/reports/va/", uniscan_host)
        conf.create_dir(uniscan_output)       
        startTime = time.time()
        #ataque 2
        conf.os.system(f"uniscan -d -u {uniscan_host} | tee {uniscan_output}/uniscan_xss_sqlli.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))
        

    def uniscan_v3():
    
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● UNISCAN :", "white", attrs=["reverse"]) + conf.colored(" LFI, RFI and RCE Checks                ", "yellow", attrs=["reverse"]))  
        # Alvo 
        uniscan_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        uniscan_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{uniscan_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, uniscan_host)
        uniscan_output = conf.dir_output(uniscan_output, "/var/webvapt/reports/va/", uniscan_host)
        conf.create_dir(uniscan_output)       
        startTime = time.time()
        #ataque 3
        conf.os.system(f"uniscan -s -u {uniscan_host} | tee {uniscan_output}/uniscan_lfi_rfi_rce.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))


    def uniscan_all():
    
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● UNISCAN :", "white", attrs=["reverse"]) + conf.colored(" Full scan                              ", "yellow", attrs=["reverse"]))  
        # Alvo  
        uniscan_host = input(conf.colored("\n Insert Target (127.0.0.1/www.url.com): ", "green", attrs=["bold"]))
        uniscan_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{uniscan_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, uniscan_host)
        uniscan_output = conf.dir_output(uniscan_output, "/var/webvapt/reports/va/", uniscan_host)
        conf.create_dir(uniscan_output)       
        startTime = time.time()
        #ataque all
        conf.os.system(f"uniscan -qwedsgj -u {uniscan_host} | tee {uniscan_output}/uniscan_all.txt")
        print("\n")
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))




    def full_va_scan():
        conf.clear()
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))    
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n ● VA   :", "white", attrs=["reverse"]) + conf.colored(" Full VA Web Scanning - All Tools          ", "yellow", attrs=["reverse"]))  
        # Alvo
        full_host = input(conf.colored("\n Insert Target (172.0.0.1/www.url.com) ", "green", attrs=["bold"]))
        full_output = input(conf.colored(f"report path - [default: /var/webvapt/reports/va/{full_host}]: ", "green", attrs=["bold"], ))
        conf.not_valid(va_scan, full_host)
        full_output = conf.dir_output(full_output, "/var/webvapt/reports/va/", full_host)    
        full_ip = conf.socket.gethostbyname(full_host)
        conf.create_dir(full_output)
        #start time
        startTime = time.time()       
    
        #full tools 
         

        if len(full_host) == 0:
            conf.clear()

            print("Invalid option")
            conf.re_open()

            conf.full_host = None
           
        else:
           
            conf.os.system(f"dirsearch -u {full_host} --auth-type=digest --auth=test:test --format plain -o /var/webvapt/reports/va/{full_host}/dirsearch.txt")
            conf.os.system(f"nmap -sV --script vuln {full_host} -vvv -oN  {full_output}/nmap_full_vulnerabilities.txt")
            conf.os.system(f"nmap -sV -p 80,443,8080 --script http-cors,http-headers,http-csrf,http-aspnet-debug,http-cross-domain-policy,http-phpself-xss,http-php-version,http-webdav-scan,http-waf-detect,http-xssed {full_host} -vv -oN  {full_output}/nmap_full_http-common.txt" )
            conf.os.system(f"wapiti  --flush-attack --auth-method basic -a test%test -u http://{full_host} -m backup,brute_login_form,cookieflags,crlf,csp,csrf,drupal_enum,exec,file,htaccess,htp,http_headers,log4shell,methods,permanentxss,redirect,shellshock,sql,ssl,ssrf,takeover,timesql,wapp,wp_enum,xss,xxe,nikto  -v 2  -f html -o {full_output}/wapiti_full_http")
            #nikto its present wapiti module
            conf.os.system(f"./modules/testssl/testssl.sh --wide --sneaky --colorblind -U -9 --htmlfile {full_output}/ssltest_full.html {full_host}")
            conf.os.system(f"uniscan -bqwedsjg -u {full_host} | tee {full_output}/uniscan_full.txt")

            
        print("\n")
        #end time
        print(conf.colored("\n Tempo usado: ", "white", attrs=["reverse"]) + conf.colored(f" {time.time() - startTime}          Segundos ", "yellow", attrs=["reverse"]))




########
# MENU   
# WEB VA SCAN TOOLS
#######
 
    def menu_va_scan():
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
       
       
   # NMAP
    print(conf.colored("\n ● Nmap", "white", attrs=["bold"]))
    print(conf.colored(" 1. ", "white", attrs=["bold"]) +  conf.colored("HTTP - Enumeration", "yellow", attrs=["bold"]))
    print(conf.colored(" 2. ", "white", attrs=["bold"]) +  conf.colored("HTTP Server - Vulnerabilities", "yellow", attrs=["bold"]))

    print(conf.colored("\t V. ", "white", attrs=["bold"]) +  conf.colored(" FULL NMAP ", "white", attrs=["reverse"]))
 
    print(conf.colored(" ● TestSSL ", "white", attrs=["bold"]))
    print(conf.colored(" 3. ", "white", attrs=["bold"]) +  conf.colored("SSL Vulnerabilities", "yellow", attrs=["bold"]))
 
    # NUCLEI
    #print(conf.colored(" ● Nuclei", "white", attrs=["bold"]))
    #print(conf.colored(" 30. ", "white", attrs=["bold"]) +  conf.colored("Detetar Vulnerabilidades Comuns.\n", "yellow", attrs=["bold"]))
    
    # WAPITI
    print(conf.colored(" ● Wapiti", "white", attrs=["bold"]))
    print(conf.colored(" 4. ", "white", attrs=["bold"]) +  conf.colored(" V1 - XSS - OWASP A7:2017.", "yellow", attrs=["bold"]))
    print(conf.colored(" 5. ", "white", attrs=["bold"]) +  conf.colored(" V2 - Injection - OWASP A1:2017", "yellow", attrs=["bold"]))
    print(conf.colored(" 6. ", "white", attrs=["bold"]) +  conf.colored(" V3 - Broken Authentication - OWASP A2:2017", "yellow", attrs=["bold"]))
    print(conf.colored(" 7. ", "white", attrs=["bold"]) +  conf.colored(" V4 - Security Misconfiguration - OWASP A6:2017", "yellow", attrs=["bold"]))
    print(conf.colored(" 8. ", "white", attrs=["bold"]) +  conf.colored(" V5 - Sensitive Data Exposure - OWASP A3:2017","yellow", attrs=["bold"]))
    print(conf.colored(" 9. ", "white", attrs=["bold"]) +  conf.colored(" V6 - Malicious File Inclusion.", "yellow", attrs=["bold"]))
    print(conf.colored(" 10. ", "white", attrs=["bold"]) +  conf.colored("V7 - Cross Site Request Forgery (CSRF) .", "yellow", attrs=["bold"])) 
    print(conf.colored(" 11. ", "white", attrs=["bold"]) +  conf.colored("V8 - Insecure Communications - OWASP A3:2017.", "yellow", attrs=["bold"]))
    print(conf.colored("\t A. ", "white", attrs=["bold"]) +  conf.colored(" FULL WAPITI ", "white", attrs=["reverse"]))
    
    # NIKTO
    print(conf.colored(" ● Nikto", "white", attrs=["bold"]))
    print(conf.colored(" 12. ", "white", attrs=["bold"]) +  conf.colored("V1 - XSS - OWASP A7:2017.", "yellow", attrs=["bold"]))
    print(conf.colored(" 13. ", "white", attrs=["bold"]) +  conf.colored("V2 - Injection OWASP A1:2017", "yellow", attrs=["bold"]))
    print(conf.colored(" 14. ", "white", attrs=["bold"]) +  conf.colored("V3 - Broken Authentication - OWASP A2:2017", "yellow", attrs=["bold"]))  
    print(conf.colored(" 15. ", "white", attrs=["bold"]) +  conf.colored("V4 - Security Misconfiguration - OWASP A6:2017", "yellow", attrs=["bold"])) 
    print(conf.colored(" 16. ", "white", attrs=["bold"]) +  conf.colored("V5 - Sensitive Data Exposure - OWASP A3:2017","yellow", attrs=["bold"]))
    print(conf.colored(" 17. ", "white", attrs=["bold"]) +  conf.colored("V6 - Malicious File Inclusion.", "yellow", attrs=["bold"]))
    print(conf.colored(" 18. ", "white", attrs=["bold"]) +  conf.colored("V7 - Cross Site Request Forgery (CSRF) .", "yellow", attrs=["bold"])) 
    print(conf.colored(" 19. ", "white", attrs=["bold"]) +  conf.colored("V8 - Insecure Communications - OWASP A3:2017.", "yellow", attrs=["bold"]))
        
    print(conf.colored("\t P. ", "white", attrs=["bold"]) +  conf.colored(" FULL NIKTO ", "white", attrs=["reverse"]))
    

    
    # UNISCAN
    
    print(conf.colored(" ● Uniscan", "white", attrs=["bold"]))
    print(conf.colored(" 20. ", "white", attrs=["bold"]) +  conf.colored("Brute Filenames, Directories, Robotex,Sitemap.", "yellow", attrs=["bold"]))
    print(conf.colored(" 21. ", "white", attrs=["bold"]) +  conf.colored("Checks for XSS, SQLi, BSQLi & Other Checks.", "yellow", attrs=["bold"]))
    print(conf.colored(" 22. ", "white", attrs=["bold"]) +  conf.colored("Checks for LFI, RFI and RCE.", "yellow", attrs=["bold"]))
    print(conf.colored("\t T. ", "white", attrs=["bold"]) +  conf.colored(" FULL UNISCAN ", "white", attrs=["reverse"]))
    

        
                                          
    # ALL
    #print(conf.colored("  ● ALL ", "white", attrs=["reverse"]))
    print(conf.colored("\n W. ", "white", attrs=["bold"]) +  conf.colored(" FULL : NMAP WAPITI NIKTO UNSICAN SSL \n", "white", attrs=["reverse"]))
    print(conf.colored(" ⚠️ ", "yellow", attrs=["bold"]) +  conf.colored(" Note, some of the full scans may take < 30m.\n", "green", attrs=["bold"]))  

    print(conf.colored("----------------------------------------------------","green", attrs=["bold"],))
    print(conf.colored("\t M. ", "white", attrs=["bold"]) +  conf.colored("Main Menu.\n", "yellow", attrs=["bold"]))  

    print(conf.colored("                                                  ","blue", attrs=["reverse"],))

# MENU
    conf.ans = input(conf.colored("\n Choose an option: ","white", attrs=["bold"])).upper()

    if conf.ans == "1":
        conf.call_def(nmap_v1, 0)                           
    elif conf.ans == "2":
        conf.call_def(nmap_v2, 0)                           
                        
    elif conf.ans == "V":
        conf.call_def(nmap_all, 0)                           
    elif conf.ans == "3":
        conf.call_def(ssl_sh, 0)   
        
    elif conf.ans == "4":
        conf.call_def(wapiti_v1, 0)
        
    elif conf.ans == "5":
        conf.call_def(wapiti_v2, 0)
        
    elif conf.ans == "6":
        conf.call_def(wapiti_v3, 0)

    elif conf.ans == "7":
        conf.call_def(wapiti_v4, 0)
    elif conf.ans == "8":
        conf.call_def(wapiti_v5, 0)
    elif conf.ans == "9":
        conf.call_def(wapiti_v6, 0)
    elif conf.ans == "10":
        conf.call_def(wapiti_v7, 0)
    elif conf.ans == "11":
        conf.call_def(wapiti_v8, 0)
    elif conf.ans == "A":
        conf.call_def(wapiti_all, 0)              
    elif conf.ans == "12":   
        conf.call_def(nikto_v1, 0)              
    elif conf.ans == "13":
        conf.call_def(nikto_v2, 0)              
    elif conf.ans == "14":
        conf.call_def(nikto_v3, 0)              
    elif conf.ans == "15":
        conf.call_def(nikto_v4, 0)   
    elif conf.ans == "16":
        conf.call_def(nikto_v5, 0)              
    elif conf.ans == "17":
        conf.call_def(nikto_v6, 0)              
    elif conf.ans == "18":
        conf.call_def(nikto_v7, 0)              
    elif conf.ans == "19":
        conf.call_def(nikto_v8, 0) 
    elif conf.ans == "P":
        conf.call_def(nikto_all, 0) 
    elif conf.ans == "20":
        conf.call_def(uniscan_v1, 0) 
    elif conf.ans == "21":
        conf.call_def(uniscan_v2, 0) 
    elif conf.ans == "22":
        conf.call_def(uniscan_v3, 0) 
    elif conf.ans == "T":
        conf.call_def(uniscan_all, 0) 
   # elif conf.ans == "23":
   #     conf.call_def(ssl_sh, 0) 


    elif conf.ans == "W":
        conf.call_def(full_va_scan, 0)

    elif conf.ans == "M":
        conf.call_def(menu_va_scan, 0)
    else:
        conf.not_valid(va_scan, conf.ans, 0)

        #conf.not_valid(va_scan, 0)
        #conf.ans = None
        

