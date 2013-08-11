import os

# List everything in 

dirname="."
dirList=os.listdir(dirname)
for filename in dirList:
    print( filename )

files = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]
dirs  = [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, f))]

print( files )
print( dirs )


import glob
l=glob.glob('*.py')
print(l)

(filepath, filename) = os.path.split("c:\\music\\ap\\mad.mp3")
print( "|{}| |{}|".format(filepath, filename) )


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

print( listdir_fullpath(os.getcwd()) )


for dirname, dirnames, filenames in os.walk('C:\\'):
    for subdirname in dirnames:
        print( os.path.join(dirname, subdirname) )
    for filename in filenames:
        print( os.path.join(dirname, filename) )
