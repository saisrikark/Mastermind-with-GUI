#module to generate random pattern
#colours are red,blue,green and yellow

import random

def pattern_generator():
    comp_patt=[]
    l=['r','b','g','y']
    print("\nGenerating pattern")
    for i in range(18):
        print('.',end='',sep='')
    print("\nRandom pattern generated")
    for i in range(4):
        comp_patt.append(random.choice(l))
    f=open("C:/Users/Srikar/Desktop/withgraphics/RAND_GEN_CODES.txt","a")
    f.write(str(comp_patt)+'\n')
    f.close()
    return comp_patt
