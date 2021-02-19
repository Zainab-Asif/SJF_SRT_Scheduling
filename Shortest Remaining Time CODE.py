import random
arr_list = [ [] , [] , [] , [] , [] ]
for i in range(5):
    for a in range(random.randint(3,8)):
        b = random.randint(1,15)
        arr_list[i].append(b)
        
pro1 = arr_list[0]
print("length =", len(pro1), "=>", "process 1:", pro1)
pro2 = arr_list[1]
print("length =", len(pro2), "=>", "process 2:", pro2)
pro3 = arr_list[2]
print("length =", len(pro3), "=>", "process 3:", pro3)
pro4 = arr_list[3]
print("length =", len(pro4), "=>", "process 4:", pro4)
pro5 = arr_list[4]
print("length =", len(pro5), "=>", "process 5:", pro5)
print("------------------------------------------")

print("process 1:", pro1, "\nthread executed:", pro1[0])
del pro1[0]
print("------------------------------------------")

print("process 1:", pro1, "\nprocess 2:", pro2)
if len(pro1) > len(pro2):
    print("thread executed:", pro2[0])
    del pro2[0]
else:
    print("thread executed:" ,pro1[0])
    del pro1[0]
print("------------------------------------------")

print("process 1:", pro1, "\nprocess 2:", pro2, "\nprocess 3:", pro3)
if len(pro1) <= len(pro2) and len(pro3):
    print("thread executed:", pro1[0])
    del pro1[0]
elif len(pro2) <= len(pro1) and len(pro3):
    print("thread executed:", pro2[0])
    del pro2[0]
elif len(pro3) <= len(pro1) and len(pro2):
    print("thread executed:", pro3[0])
    del pro3[0]
print("------------------------------------------")

print("process 1:", pro1, "\nprocess 2:", pro2, "\nprocess 3:", pro3, "\nprocess 4:", pro4)
if len(pro1) <= len(pro2) and len(pro3) and len(pro4):
    print("thread executed:", pro1[0])
    del pro1[0]
elif len(pro2) <= len(pro1) and len(pro3) and len(pro4):
    print("thread executed:", pro2[0])
    del pro2[0]
elif len(pro3) <= len(pro1) and len(pro2) and len(pro4):
    print("thread executed:", pro3[0])
    del pro3[0]
elif len(pro4) <= len(pro1) and len(pro2) and len(pro3):
    print("thread executed:", pro4[0])
    del pro4[0]
print("------------------------------------------")

print("process 1:", pro1, "\nprocess 2:", pro2, "\nprocess 3:", pro3, "\nprocess 4:", pro4, "\nprocess 5:", pro5)

while len(pro1)>0 or len(pro2)>0 or len(pro3)>0 or len(pro4)>0 or len(pro5)>0:
    
    len_list = [len(pro1), len(pro2), len(pro3), len(pro4), len(pro5)]
    #print("length of list:", len_list)
    
    m = min(i for i in len_list if i > 0)
    
    if len(pro1) > 0 and m == len(pro1):
        print("thread executed:", pro1[0])
        del pro1[0]
    elif len(pro2) > 0 and m == len(pro2):
        print("thread executed:", pro2[0])
        del pro2[0]
    elif len(pro3) > 0 and m == len(pro3):
        print("thread executed:", pro3[0])
        del pro3[0]
    elif len(pro4) > 0 and m == len(pro4):
        print("thread executed:", pro4[0])
        del pro4[0]
    elif len (pro5) > 0 and m == len(pro5):
        print("thread executed:", pro5[0])
        del pro5[0]
    print("------------------------------------------")
    print("process 1:", pro1, "\nprocess 2:", pro2, "\nprocess 3:", pro3, "\nprocess 4:", pro4, "\nprocess 5:", pro5)
print("\n--- ALL PROCESSES COMPLETED ---")
