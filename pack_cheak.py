import subprocess as subp
def chkbin(appname):
    allout=subp.run(["which",appname],capture_output=True,text=True)
    if appname in allout.stdout and allout.stdout.index(appname)>1:
        return True
    else:
        return False
def ifnotinstall(appname):
    if chkbin(appname):
        print(appname," found")
    else:
        fname='get-docker.sh'
        #allcoms=[f"curl -fsSL https://get.docker.com -o {fname}",f"chmod +x {fname}",f"sh get-docker.sh","rm -rf {fname}"]
        allcoms=[f"curl -fsSL https://get.docker.com -o {fname}",f"chmod +x {fname}"]
        for coms in allcoms:
            subp.run(coms.split(" "))
ifnotinstall("docker")
