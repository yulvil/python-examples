
# INTEGERS

i = 3
n = 1234**1234 # Infinite precision
n = 0xff    # 255
n = 0b1110  # 14
n = 0o14    # 12       14 does not work
hex(255) # 0xff
bin(255) # 0b11111111

# STRINGS

s1 = 'abc'
s2 = "def"
print(s1 + s2)

print( "x"*5 ) # xxxxx

print( 'ABC' "def" + "123" + str(456) )  # ABCdef123456

print( "ABC" + "DEF" + " xyz "*5 )   # ABCDEF xyz  xyz  xyz  xyz  xyz
print( "ABC" "DEF" " xyz "*5 )       # ABCDEF xyz ABCDEF xyz ABCDEF xyz ABCDEF xyz ABCDEF xyz

arr = "1,2,3,4,55".split(",")
print(arr)  # ['1', '2', '3', '4', '55']

#print("fatal error", file=sys.stderr)

print("MyMessage: ", end="")

print( (7/3)**5 ) # 2^5=32

print (5.0/2)   # 3.5

print( -1/2 ) # floor(0.5)=-1

print( sum([1,2,3]) )  # 6

print( str(bin(27)) )

# VARIABLES
x=y=z=2    # no type (int,float,string)
print( x*y*z ) # 8
x=4.3
y="abc"  # Type can change during execution
y = 8 if x==6 else 9

x,y = "ab cd".split()  # Multiple assignments
print(x) # ab
print(y) # cd

# STRINGS

x='abc'
y="def"
print( x, y )

x="multiline\
multiline2"

print(x);

x="""multiline
multiline2"""

print(x);

print ("ABC" + "DEF" + " xyz "*5)    # ABCDEF xyz  xyz  xyz  xyz  xyz
print ("ABC" "DEF" " xyz "*5)        # ABCDEF xyz ABCDEF xyz ABCDEF xyz ABCDEF xyz ABCDEF xyz

print ("%s %s %s %s" % ("Spam", "eggs", "and", "spam"))

x = "1,2,3,4,55".split(",")
print(x)

x,y = "ab cd".split()
print(x)
print(y)

#print( "len=" + len("abc123") );


# LISTS

arr = ['spam', 'eggs', 100, 1234]
print(arr,arr[1])
print(len(arr))
arr = ['spam', 'eggs', ['a',654,'b',987], 1234]
print(arr)
print(len(arr))
#a,b,*c = [1,2,3,4,5,6,7,8,9]   Python3000 only

# DICTIONARIES

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(d['voltage'])
d['key5'] = 'value5'  # dictionaries are mutable
print(d)
for myk,myv in d.items(): print(myk,myv) # items() returns a copy
for myk,myv in d.iteritems(): print(myk,myv) # iteritems() returns an iterator over the dictionary's items

mydict = {'key1': 4000, 'key2': 6000}
kk = mydict.keys()  # New array
print( kk )
kk = mydict.viewkeys()  #
print( kk )

mydict = {i : chr(64+i) for i in range(1,6)}  # Dictionary comprehension v2.7+
print( mydict )  # {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}

from collections import OrderedDict
d = OrderedDict([('first', 1), ('second', 2), ('third', 3)])
print(d.items()) # [('first', 1), ('second', 2), ('third', 3)]


# FUNCTIONS

def myFunc1(x):
  return len(x);

pF = myFunc1;
print(pF("printMe"))
pF = len;
print(pF("printMe"))

myargs = [10,20]
print(range(*myargs))

f = lambda x: x*x*x
print(f(3))

def make_incrementor(step):
  return lambda x: x + step

adder1 = make_incrementor(1)
adder2 = make_incrementor(2)

print(adder1(50))
print(adder1(55))

print(adder2(50))
print(adder2(55))

# =============================
print("FUNCTIONAL PROGRAMMING")

def cube(x): return x*x*x
print(map(cube, range(1, 11)))
print([cube(n) for n in range(1, 11)]) # Same as previous line

def add(x,y,z,v,w): return x+y+z+v+w
r = range(1,11)
print(map(add,r,r,r,r,r))

def add(n,m): return n+m
print(reduce(add, range(1, 11)))

# List Comprehensions

print( [3*x for x in [1,2,3]] )
print( [3*x for x in range(1,11) if x>5] )
print( [(x**2,x**3,x**4,x**5) for x in [1,2,3]] )
print( [(x,y,z) for x in [1,2,3] for y in [10,20,30] for z in [100,200,300] ])

print( zip([1,2,3,4],[10,20,30,40]) )  # [(1, 10), (2, 20), (3, 30), (4, 40)]
print( zip([1,2,3],['a','b','c'],['A','B','C'],[10,20,30,40]) ) # [(1, 'a', 'A', 10), (2, 'b', 'B', 20), (3, 'c', 'C', 30)]


print( [a - b for (a,b) in zip((1,2,3), (1,2,3))] )  # will return [0, 0, 0]

# Generators
from itertools import count
S = (2*x for x in count() if x**2 > 3)
print( S.next() )

# SETS
s1 = set([3,3,3,2,2,1,1])
s2 = set([3,3,4,4,4])
print( s1 )      # set([1, 2, 3])
print( s1 - s2)  # set([1, 2])
print( s1 & s2)  # set([3])
print( s1 | s2)  # set([1, 2, 3, 4])
print( s1 ^ s2)  # set([1, 2, 4])

# Printing
for x in range(1, 11):
    print (repr(x).rjust(2), repr(x*x).rjust(3),)
    print (repr(x*x*x).rjust(4))

for x in range(1,11):
    print ('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print( '12'.zfill(5) + '    123'.center(1))

print ('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print ('PI approx {0:.3f}.'.format(3.141592654))

# GENERATORS

def rett():
    for index in range(1,11):
        yield index

for ii in rett():
    print (ii)

print( sum(i*i for i in range(10)) ) # 285

# Fixed-length
import struct
print( struct.unpack("4s2s4s", "ABCDNYWXYZ") )   # ('ABCD', 'NY', 'WXYZ')

print( [(x,y) for x in range(1,4) for y in range(x,4)] )  # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]



import itertools
l = [s for s in itertools.combinations('ABCD', 2)]
print(l)
l = [s for s in itertools.combinations('ABCD', 3)]
print(l)
l = [s for s in itertools.product(range(1,4),range(1,4))]
print(l)


#from itertools import groupby
#l = [1,6,4,3,8,6,3,2,6,7,9,3,2,4,6,8,7,7,6,4]

   #print(l2)

#from collections import defaultdict

# 5 unique elements
#print random.sample(xrange(100,201),5)
