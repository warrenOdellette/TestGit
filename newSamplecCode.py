
# coding: utf-8

# # WARNING RUN ONCE ONLY

# In[109]:


def myPrint(y):
    for ite in y:
        print(ite)
    return

n = 3 #number of proteins analyzed 
sec = 6
charLength=len('sp|Q60892|OLF8_MOUSE        ')
charLength2=len('PMYFFLANLSFVDICFTSTTVPKMLVNIQTQSKAITYADCISQMSVFLVFAELDNFLLA')

with open('sample.txt') as f:
    data=f.read().split('\n')

myPrint(data)
    


# In[110]:


dataSorted=[]
for ite in range(0,n+1):
    dataSorted.append(data[ite])
myPrint(dataSorted)


# In[111]:


dataReduced = data[n+2:]
myPrint(dataReduced)


# In[112]:


for ite in range(0,len(dataReduced)):
    dataReduced[ite]=dataReduced[ite][charLength:] #remove the first 28 characters to all
myPrint(dataReduced)


# In[113]:


for ite in range(0,n+1):
    for ite2 in range(0,sec-1):
        dataSorted[ite]=dataSorted[ite]+dataReduced[ite+ite2*(5)]
myPrint(dataSorted)    


# Transmembrane Comparison Sequence (14 number input)

# In[114]:


#dataSorted.append('')
#for ite in range(0,charLength):
#    dataSorted[n+1]=dataSorted[n+1]+' '
#dataSorted[n+1]

    


# In[115]:


#for ite in range(0,charLength2*(sec-1)):
#    dataSorted[n+1]=dataSorted[n+1]+str(ite)


# In[116]:


#myPrint(dataSorted)

