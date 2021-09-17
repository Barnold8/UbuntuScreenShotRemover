import os
import pwd

def dirGetter():

    dirARR = [os.getcwd(),os.getcwd().split("/")]
    return dirARR

def dirGenerator(splitted):

    string = ""

    for parts in splitted:
        
        if parts != "/home":
            string += '/' + parts

    return string

def getUser():

    return pwd.getpwuid( os.getuid() )[ 0 ]

def gotoPictures():
    
    dirs = dirGetter()
    i = len(dirs[1]) -1
    while(dirs[1][i] != "home"):

        dirs[1] = dirs[1][:-1]
        i -= 1

    dirs = dirGenerator(dirs[1])
    os.chdir("{}/{}/Pictures".format(dirs,getUser()))

def delFiles(include):

    for elems in os.listdir():

        if include in elems:
            os.system('rm "{}"'.format(str(elems)))
    
def main():

    gotoPictures()
    delFiles("Screenshot")

main()
