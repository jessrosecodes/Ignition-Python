import random
import numpy as numpy

############################ Inputs ################################
test = 1001
n = 255
rannum = 0
sum = 0
checksum = 0
calcs = 20
rannumrangestart = 1
rannumrangeend = 10000
rannumdiv = 100000
############################ Inputs ################################
########################### EQNS    ################################
# list2 = []   #list allows us to append, unlike array
pretty2 = []
list1 = []
########################### EQNS    ################################
########################### SYNTAX  ################################
fltrannum = float("{0:.4f}".format(rannum))
fltsum = float("{0:.4f}".format(sum))
fltchecksum = float("{0:.4f}".format(checksum))
#print ("i: 0","RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)

for k in range(1,test):
   
    for i in range(1, calcs):    #generates iterations 0 to 20              #indented inside the forloop is INSIDE forloop
      rng = random.Random()           
      number = rng.randrange(rannumrangestart, rannumrangeend)
      rannum = (number / rannumdiv)
      sum += rannum
      checksum += sum
      fltrannum = float("{0:.4f}".format(rannum))
      fltsum = float("{0:.4f}".format(sum))
      fltchecksum = float("{0:.4f}".format(checksum))
      #print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)

    # print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)    
    #my_checksum[k] = fltchecksum
    # ans2 = bignum % rannumdiv

    ans1 = fltsum % rannumdiv
    ans2 = fltchecksum % rannumdiv
    fltans2 = float("{0:.4f}".format(ans2))
    # list1 = []                        use if using two lists
    # list1.append(ans1)
    list1.append(fltans2)
    # list2.append(list1)

# print("ANS2: ",my_checksum)

for item in list1:
    print(item)

from collections import Counter
d = Counter(list1)
new_list = list([item for item in d if d[item]>1])
print(new_list)

# print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)