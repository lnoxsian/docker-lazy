def instfromfile(instfile,subcom):
    allcoms=fh.readingfile(comfile,"json")
    fullread=fh.readingfile(instfile,"list")
    for command in fullread:
        if ":" in command:
            appname=command[:command.index(":")-1].strip('\n')
            args=command[command.index(":")+1:].strip('\n')
            print(shand.shelldonparse(appname,subcom,allcoms,args))
        else:
            appname=command.strip('\n')
            print(shand.shelldonparse(appname,subcom,allcoms))

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
            print(shand.shelldonparse(appname,subcom,allcoms,args))
        else:
            appname=command
            print(shand.shelldonparse(appname,subcom,allcoms))
