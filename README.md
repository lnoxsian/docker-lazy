# docker-lazy
This is a smallish python program used for automating and
maintaing docker instance as such it is build with additional 
functions such as shellinteraction with logging and other functions
## why make docker lazy
Since im **lazy** and need to run my apps in docker by automatically
installing it and managing it so i made this program as such you
can import it to a module and run it as such ok
* to import it

```bash
git clone https://github.com/lnoxsian/docker-lazy.git
```
* To run in a program just move the **'docker_lazy.py'** to the 
project folder and exec it as such your choice also the com.json 
and the installing file

```python
import docker_lazy # or from docker_lazy import fh,shand
```
# all modules
1. There is one for file handling -- class fh
    * All the functions here are used for makeing and handing 
    with files and this includes logging loading of files and also for
    getting returns for all the types of data
    **contains**
    * _readingfile()_ -- This is used for reading files 
    of types str,json and return list or str
    * _writingfile()_ -- This is used for writing files 
    of types str,list for logging and other uses
    * _cheakfileinit()_ -- This is for initing the missing files for 
    not encounting errors as such
2. There is one for shell process -- class shand
    * The modules in the class is used for installing docker or 
    even getting shell commands and next is the use of regex
    to maintain the apps running in docker for fun
    * _shelldonparse()_ -- This is for parsing the commands properly
    to be executed by shelldon()
    * _shelldon()_ -- This is for running the commands using subprocess
    module
    * _chkifinstalled()_ -- This is for cheaking if docker is installed 
    if not installing it okay
    * _instfromfile()_ -- This opens **package.txt** and makes the program
    to install it in docker with the args
    * _instfromuser()_ -- This is for userinput for installing the docke
    apps 
    * _logtofile()_ --This is for logging all the output from shelldon 
    either an error or even exec 0 output
# wanrning 
**Pls do take this with a grain of salt**
This is still alpha software and i will not be responsible for
bricked or broken docker installs also **not full complete**
if there is any issues you can contact me a i can help if i can ;)
# who am i ? and why make this 
As stated im lazy and need something to do in life so i made this 
small module and also the name sounded cool thats all
to contact me 
```
    __                      _           
   / /___  ____  _  _______(_)___ _____ 
  / / __ \/ __ \| |/_/ ___/ / __ `/ __ \
 / / / / / /_/ />  <(__  ) / /_/ / / / /
/_/_/ /_/\____/_/|_/____/_/\__,_/_/ /_/ 
email : lnox122224@gmail.com
githublocal: https://github.com/lnoxsian
-- happy to help ;)
```
