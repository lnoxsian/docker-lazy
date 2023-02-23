import json,os,subprocess as subp

logfile='loggy.py'
comfile='com.json'
packfile='package.txt'

def fileread(filename,readtype):
    filechkinit(filename)
    with open(filename,'r') as rfile:
        if readtype.lower()=='s':
            alldata=rfile.read()
        elif readtype.lower()=='l':
            alldata=rfile.read().split('\n')
        elif readtype.lower()=='j':
            alldata=json.loads(rfile.read())
    return alldata

def filewrite(filename,writetype,alldata):
    if len(alldata)==0:
        print("no data to write")
        exit()
    if writetype.lower()=='w':
        with open(filename,'w') as wfile:
            if isinstance(list,alldata):
                wfile.writelines(alldata)
            else:
                wfile.write(alldata)
    else:
        with open(filename,'a') as afile:
            afile.write(alldata)

def filechkinit(filename):
    if filename in os.listdir() and os.path.isfile(filename):
        print(filename,"found")
    else:
        print(filename,"not found")
        if input(f"init {filename} y/n").lower()=='y':
            with open(filename,'w') as ifile:
                pass

def shellparser(packname,comtype,args=""):
    allcoms=fileread(comfile,'j')
    packman=allcoms[packman][0]
    if comtype.lower()=='i':
        if len(args)==0:
            command=[packman,allcoms["install"][0],packname]
        else:
            command=[packman,allcoms["install"][0],args,packname]
    elif comtyep.lower()=='r':
        if len(args)==0:
            command=[packman,allcoms["remove"][0],packname]
        else:
            command=[packman,allcoms["remove"][0],args,packname]
    elif comtyep.lower()=='m':
        if len(args)==0:
            command=[packman,allcoms["maintain"][0],packname]
        else:
            command=[packman,allcoms["maintain"][0],args,packname]
    elif comtyep.lower()=='d':
        if len(args)==0:
            command=[packman,allcoms["download"][0],packname]
        else:
            command=[packman,allcoms["download"][0],args,packname]
    return command

def sheldon(all_coms):
    if len(all_coms)==0:
        exit()
    else:
        shell_out=subp.run(all_coms,shell=True,capture_output=True,text=True,encoding='UTF-8')
        if shell_out.returncode==0:
            cout=shell_out.stdout
            print(f"{all_coms} exec done")
        else:
            cout=shell_out.stderr
            print(f"{all_coms} stopped with err:{shell_out.stderr}")
    return cout

def chkbin(packname):
    allout=subp.run(["which",packname],text=True,capture_output=True)
    if packname in allout.stdout and packname.index(allout.stdout):
        return True
    else:
        return False

def ifnotinstall(appname):
    if chkbin(appname):
        print(appname," found")
    else:
        fname='get-docker.sh'
        allcoms=[f"curl -fsSL https://get.docker.com -o {fname}",f"chmod +x {fname}",f"sh get-docker.sh","rm -rf {fname}"]
        for coms in allcoms:
            output=subp.run(coms.split(" "),shell=True,capture_output=True)
            if output.returncode==0:
                print("proc done ")
            else:
                print("proc not done pls cheak ;|")
