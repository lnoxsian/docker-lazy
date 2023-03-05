
class fh:
    def __init__(self,filename):
        self.filename=filename

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
    
    def writingfile(filename,writetype,alldata):
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
