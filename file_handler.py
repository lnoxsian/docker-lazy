import json,os

class File_handler():

    def fileread(filename,ftype):
        with open(filename,"r") as readf:
            if fout.lower()=="s":
                alldat=readf.read()
            elif fout.lower()=="l":
                alldat=(readf.read()).split("\n")
            elif fout.lower()=="j":
                alldat=json.loads(readf.read())
        return alldat

    def filewrite(filename,ftype,alldata):
        if len(alldata)==0:
            print("alldata seems to be empty")
            break
        if ftype.lower()=="w"
            with open(filename,"w") as writef:
                if isinstance(list,alldata)
                    writef.writelines(alldata)
                else:
                    writef.write(alldata)
        else:
            with open(filename,"a") as writef:
                writef.write(alldata)

    def fcheak_init(filename):
        if filename in os.listdir() and os.path.isfile(filename):
            print(filename,"is found here")
        else:
            print(filename,"is not found need to init")
            if input("y/n")=="y":
                with open(filename,"w") as f:
                    pass

