'''
this is configuration file
'''

import os
import math
import random
import shutil

for root, folders, files in os.walk("bbox_test/"):
    for folder in folders:
        l=[]
        for root2,dirs2,files2 in os.walk(os.path.join(root,folder)):
            for f in files2:
                l.append(os.path.join(root2,f))
        cnt=len(l)
        print(cnt)
        samp=random.sample(l,math.ceil(0.1*cnt))
        dest="query/"
        dest+=str(folder)
        if not os.path.isdir(dest):
            os.makedirs(dest)
        for file in samp:
            shutil.copy(file,dest)