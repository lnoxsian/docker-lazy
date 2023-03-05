#this is a small python project for running docker and using it
#for running the depends for docker and maintaining it for fun ;)
import json,os,subprocess as subp
from datetime import datetime 

logfile='loggy.txt'
comfile='com.json'
packfile='package.txt'

class fh:
    def readingfile(filename,readtype):
        fh.cheakfileinit(filename)
        with open(filename,'r') as readfile:
            if readtype=='str':
                alldata=readfile.read()
            elif readtype=='list':
                alldata=readfile.readlines()
            elif readtype=='json':
                alldata=json.loads(readfile.read())
        return alldata
    
    def writingfile(filename,alldata,writetype="str"):
        fh.cheakfileinit(filename)
        if len(alldata)==0:
            print("no data found to written exiting")
            exit()
        if writetype=='str':
            with open(filename,'w') as writefile:
                if isinstance(alldata,list):
                    writefile.writelines(alldata)
                else:
                    writefile.write(alldata)
        else:
            with open(filename,'a') as appendfile:
                appendfile.write(alldata)

    def cheakfileinit(filename):
        if filename in os.listdir() and os.path.isfile(filename):
            print(f"{filename}:is found ")
        else:
            print(f"{filename}:is not found")
            if input(f"want to init {filename} y/n >> ").lower()=='y':
                with open(filename,'w') as initfile:
                    pass
class shand():
    def shelldonparse(packname,comtype,allcoms,args=""):
        packman=allcoms["pack"][0]
        if len(args)==0:
            dacomm=[packman,allcoms[comtype][0],packname]
        else:
            dacomm=" ".join([packman,allcoms[comtype][0],args,packname]).split(" ")
        return dacomm
    
    def shelldon(fullcoms):
        if len(fullcoms)==0:
            exit()
        else:
            if isinstance(fullcoms,list):
                shellout=subp.run(fullcoms,capture_output=True,text=True,encoding='UTF-8')
            else:
                shellout=subp.run(fullcoms.split(" "),capture_output=True,text=True,encoding='UTF-8')
            if shellout.returncode==0:
                print(f"the proc is done")
                return shellout.stdout
            else:
                print(f"the proc is not done")
                return ""
    
    def chkifinstalled(appname):
        installcoms=[f"curl -fsSL https://get.docker.com -o {fname}",f"chmod +x {fname}",f"sh get-docker.sh","rm -rf {fname}"]
        fname=f"get-{appname}.sh"
        command=f"which {appname}"
        if appname in shand.shelldon(command):
            print(f"{appname} is found")
        else:
            if input(f"Need to install {appname}:y/n>> ").lower()=='y':
                for coms in installcoms:
                    shand.shelldon(coms)

    def instfromfile(instfile,subcom):
        allcoms=fh.readingfile(comfile,"json")
        fullread=fh.readingfile(instfile,"list")
        for command in fullread:
            if ":" in command:
                appname=command[:command.index(":")-1].strip('\n')
                args=command[command.index(":")+1:].strip('\n')
                fullout=shelldon(shand.shelldonparse(appname,subcom,allcoms,args))
            else:
                appname=command.strip('\n')
                fullout=shelldon(shand.shelldonparse(appname,subcom,allcoms))

    def instfromuser(subcom):
        appsep=','
        argsep=':'
        allcoms=fh.readingfile(comfile,"json")
        print(f"Enter in the apps to install with sep by {appsep} with {argsep}")
        allapps=input("Enter>>").split(appsep)
        for command in allapps:
            if ":" in command:
                appname=command[:command.index(argsep)-1]
                args=command[command.index(argsep)+1:]
                shelldon(shand.shelldonparse(appname,subcom,allcoms,args))
            else:
                appname=command
                shelldon(shand.shelldonparse(appname,subcom,allcoms))
    
    def logtofile(logfile,alldata):
        today=datetime.today().isoformat()
        nfilename=logfile[:logfile.index('.')]+'-'+today+logfile[logfile.index('.'):]
        fh.writingfile(nfilename,alldata,'and')
