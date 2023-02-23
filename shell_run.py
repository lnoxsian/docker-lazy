import subprocess as subp

def shell_runner(all_commands):
    if len(all_commands)==0:
        break
    else:
        shell_out=subp.run(all_commads,shell=True,capture_output=True,Text=True,encoding='UTF-8')
        if shell_out.returncode==0:
            print("exec is done")
        else:
            print("exec is not done properly")
            print(shell_out.stderr)
            break
    return shell_out.output
        
