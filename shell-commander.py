import subprocess as subp
import json,os

filename="com.json"
insfname="install.txt"

def cheakfiles(allfiles):
    if isinstance(allfiles,list):
        for i in allfiles:
            if i not in os.listdir():
                initfile(i)
    else:
        if i not in os.listdir():
            initfile(i)

def initfile(filename):
    with open(filename,"w") as initf:
        pass

def packnames():
    mods=[]
    with open(insfname,"r") as instfile:
        inmods=instfile.readlines()
        for i in inmods:
            mods.append(i.strip('\n'))
    return mods

def comfileinit(filename):
    with open(filename,"r") as jfile:
        alldat=json.loads(jfile.read())
    return alldat

def runcommand(allcom):
    subp.run(allcom,text=True,capture_output=True)

class shell_com:
    def instpack(package,args):
        allcom=comfileinit(filename)
        if len(args)==0:
            allcoms=" ".join([allcom["packman"][0],allcom["install"][0],package])
        else:
            allcoms=" ".join([allcom["packman"][0],allcom["install"][0],args,package])
        print(allcoms)
    def remvpack(package,args):
        allcom=comfileinit(filename)
        if len(args)==0:
            allcoms=" ".join([allcom["packman"][0],allcom["remove"][0],package])
        else:
            allcoms=" ".join([allcom["packman"][0],allcom["remove"][0],args,package])
        print(allcoms)
    def downpack(package,args):
        allcom=comfileinit(filename)
        if len(args)==0:
            allcoms=" ".join([allcom["packman"][0],allcom["download"][0],package])
        else:
            allcoms=" ".join([allcom["packman"][0],allcom["download"][0],args,package])
        print(allcoms)


