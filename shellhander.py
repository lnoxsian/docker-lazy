import os,subprocess as subp,json

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
                return shellout.stderr
    
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

