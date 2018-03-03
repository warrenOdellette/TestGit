
def myPrint(y):
    for ite in y:
        print(ite)
    return

n = 3 #number of proteins analyzed 
sec = 6
charLength=len('sp|Q60892|OLF8_MOUSE        ')
charLength2=len('PMYFFLANLSFVDICFTSTTVPKMLVNIQTQSKAITYADCISQMSVFLVFAELDNFLLA')

with open('aminoacidSeq.txt') as f:
    data=f.read().split('\n')

myPrint(data)
print("hello world")
    


