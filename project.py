from collections import Counter
from scipy.sparse import *
from numpy import *


def cr_way(n):
    w = []
    for i in range(n):
        way = str('/home/andrew/'+str(i)+'.txt')
        w.append(way)
    print w
    file_op(w)
    return w
        #file_op(way)

def file_op(w):
    for i in w:
        #print i
        f = open(i, 'r')
        list1 = []
   
        for line in f:
            a = line.replace(',','').split()
        for i in a:
            list1.append(i.rstrip().lstrip())
        #print list1
        count_list = [list1[:i].count(list1[i]) for i in range(len(list1))]
        count_list.reverse()
        list2.append(count_list)
    print list2
    print (csr_matrix(list2))
    
    
    

if __name__ == "__main__":
    list2 = []
    cr_way(2)
   