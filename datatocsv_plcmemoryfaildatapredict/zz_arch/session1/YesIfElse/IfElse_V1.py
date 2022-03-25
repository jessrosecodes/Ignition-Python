import random
import numpy as numpy



for i in range(0, 20):    #generates iterations 0 to 20
    if i == 0:
      rannum = 0
      sum = 0
      checksum = 0
      fltrannum = float("{0:.4f}".format(rannum))
      fltsum = float("{0:.4f}".format(sum))
      fltchecksum = float("{0:.4f}".format(checksum))
    elif i > 0:
      rng = random.Random()           
      number = rng.randrange(1, 10000)
      rannum = (number / 1000)
      sum += rannum
      checksum +=  sum
      fltrannum = float("{0:.4f}".format(rannum))
      fltsum = float("{0:.4f}".format(sum))
      fltchecksum = float("{0:.4f}".format(checksum))
    print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
print ("i:", i,"RN:", fltrannum, "A:", fltsum, "B:", fltchecksum)
