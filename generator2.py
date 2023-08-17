import itertools
import sys
sqr=(x**2 for x in itertools.count(1))

#for x in sqr:
    #print(x)

    #if x >1000:
        #sqr.close()
print(sys.getsizeof(sqr),"bytes")
