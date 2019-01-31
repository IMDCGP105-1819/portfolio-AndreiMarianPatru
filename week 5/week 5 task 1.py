L3=[]
def remove_dups(L1, L2):
 for e in L1:
     if e not  in L2:
         L3.append(e)
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
