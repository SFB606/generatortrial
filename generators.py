#def f():
    #yield 1
    #yield 2
#print(f())
#for x in f():
    #print(x)
#import string
#def f():
    #for c in string.ascii_uppercase:
        #yield c
#for x in f():
    #print(x)
import itertools

def prime():
    yield 2
    prime_cache = [2]
    for n in itertools.count(3,2):
        is_prime = True

        for p in prime_cache:
            if p%n==0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(n)
            yield n
for x in prime():
    print(x)
    if x>=100:
        break
        
        
