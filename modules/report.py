#!/usr/bin/env python3
# @paciente23256

import conf.conf as conf
import glob


def reports():

       
    def va_report():
    
        conf.clear()
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n📰 List VA Reports:\n","white", attrs=["bold"],))      
       # search all files inside a specific folder
       # *.* means file name with any extension
       	dir_path = r'reports/va/**/*.*'
       	for file in glob.glob(dir_path, recursive=True):
    
            #print(file)
       
            print(conf.colored(f"⚠️  {file}","green", attrs=["bold"],))         
         
    def pt_report():  

        conf.clear()
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n📰 List PT Reports:\n","white", attrs=["bold"],))      
       # search all files inside a specific folder
       # *.* means file name with any extension
       	dir_path = r'reports/pt/**/*.*'
       	for file in glob.glob(dir_path, recursive=True):
    
            #print(file)
       
            print(conf.colored(f"⚠️  {file}","green", attrs=["bold"],))         
 

    def vapt_report():  

        conf.clear()
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))     
        print(conf.colored("\n📰 List VAPT Reports:\n","white", attrs=["bold"],))      
       # search all files inside a specific folder
       # *.* means file name with any extension
       	dir_path = r'reports/vapt/**/*.*'
       	for file in glob.glob(dir_path, recursive=True):
    
            #print(file)
       
            print(conf.colored(f"⚠️  {file}","green", attrs=["bold"],))      

    # MENU
 
    def menu_reports():
        conf.clear()
        conf.re_open()

    logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
    print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))

    #print(conf.colored("                                                    ","blue", attrs=["reverse"],))
    print(conf.colored("\n   REPORTS   ", "white", attrs=["reverse"]) + conf.colored("                                        ", "yellow", attrs=["reverse"]))
       
    #MENU
    print(conf.colored("\n ● VA ", "white", attrs=["bold"]))
    print(conf.colored("1. ", "white", attrs=["bold"]) +  conf.colored("get VA scan reports\n", "yellow", attrs=["bold"]))
    print(conf.colored("\n ● PT ", "white", attrs=["bold"]))
    print(conf.colored("2. ", "white", attrs=["bold"]) +  conf.colored("get PT scan reports\n", "yellow", attrs=["bold"]))
    print(conf.colored("\n ● VAPT ", "white", attrs=["bold"]))
    print(conf.colored("3. ", "white", attrs=["bold"]) +  conf.colored("get VAPT scan reports\n", "yellow", attrs=["bold"]))
    print(conf.colored("----------------------------------------------------","green", attrs=["bold"],))
    print(conf.colored("\tM. ", "white", attrs=["bold"]) +  conf.colored("Main Menu.\n", "yellow", attrs=["bold"]))                               
    print(conf.colored("                                                    ","blue", attrs=["reverse"],))
        
    conf.ans = input(
        conf.colored("\nChoose an option: ","white", attrs=["bold"])).upper()

    if conf.ans == "1":
        conf.call_def(va_report, 0)
    elif conf.ans == "2":
        conf.call_def(pt_report, 0)
    elif conf.ans == "3":
        conf.call_def(vapt_report, 0) 
    elif conf.ans == "M":
        conf.call_def(menu_reports, 0)
    else:
        conf.not_valid(reports, conf.ans, 0)

