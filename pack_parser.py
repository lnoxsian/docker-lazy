
def prime_commander(packname,allcoms,swt,args=""):
    packman=allcoms["pack"][0]
    if swt=="i":
        if len(args)==0:
            command=[packman,allcoms["install"][0],packname]
        else:
            command=[packman,allcoms["install"][0],args,packname]
    if swt=="r":
        if len(args)==0:
            command=[packman,allcoms["remove"][0],packname]
        else:
            command=[packman,allcoms["remove"][0],args,packname]
    if swt=="m":
        if len(args)==0:
            command=[packman,allcoms["maintain"][1],packname]
        else:
            command=[packman,allcoms["maintain"][1],args,packname]
    if swt=="d":
        if len(args)==0:
            command=[packman,allcoms["download"][0],packname]
        else:
            command=[packman,allcoms["download"][0],args,packname]
    return command

