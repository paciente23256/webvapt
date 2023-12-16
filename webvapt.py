#!/usr/bin/env python3
# @paciente23256


"""
              ___ __       _   ______ 
        (   /(_  / _) (  //_| /__)/   
        |/|/ /__/(_)  |_/(  |/   (    
     
    Web Security Blackbox Testing with VAPT 
    
 Author: @paciente23256
    
"""


import conf.conf as conf


def main():
    while conf.ans:
        
        logo_ascii = """      
                ___ __       _   ______ 
          (   /(_  / _) (  //_| /__)/   
          |/|/ /__/(_)  |_/(  |/   (    
     
      Web Security Blackbox Testing with VAPT
    """  
        print(conf.colored(f"{logo_ascii}", "blue", attrs=["bold"]))
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))
        print(conf.colored("\n ● Author: ", "white", attrs=["bold"]) + conf.colored("@paciente23256", "green", attrs=["bold"]))
        print(conf.colored(" ● Version: ", "white", attrs=["bold"]) + conf.colored(f"{conf.version}\n", "green", attrs=["bold"]))
        conf.ver_check()
        print(conf.colored("----------------------------------------------------","green", attrs=["bold"],))
        print(conf.colored("\n ● MAIN \n", "white", attrs=["bold"]))
        print(conf.colored("\t V ", "white", attrs=["reverse"]) +  conf.colored(" Vulnerability Assessement", "yellow", attrs=["bold"]))
        print(conf.colored("\t A ", "white", attrs=["reverse"]) +  conf.colored(" Penetration Test", "yellow", attrs=["bold"]))
        print(conf.colored("\t P ", "white", attrs=["reverse"]) +  conf.colored(" Auto full VATP", "yellow", attrs=["bold"]))
        print(conf.colored("\t T ", "white", attrs=["reverse"]) +  conf.colored(" Report\n", "yellow", attrs=["bold"]))  
        print(conf.colored("----------------------------------------------------","green", attrs=["bold"],))
        print(conf.colored("\tS. ", "white", attrs=["bold"]) +  conf.colored("Exit.\n", "yellow", attrs=["bold"]))                               
        print(conf.colored("                                                    ","blue", attrs=["reverse"],))

        conf.ans = input(conf.colored("\n Choose an option: ", "green", attrs=["bold"])).upper()
             

        if conf.ans == "V":
            conf.call_def(conf.va_scan)
        elif conf.ans == "A":
            conf.call_def(conf.pt_scan)
        elif conf.ans == "P":
            conf.call_def(conf.vapt_scan)
        elif conf.ans == "T":
            conf.call_def(conf.reports)
        elif conf.ans == "S":
            conf.call_def(conf.exit)
        else:
            conf.not_valid(main, conf.ans, 0)
try:
    main()
except KeyboardInterrupt:
    print("\n \n Keyboard Interrupt. ")
    conf.sys.exit()
