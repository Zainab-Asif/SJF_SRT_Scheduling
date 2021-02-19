import random
import numpy
from numpy.random import randint
new_list = []
list_len = []
unsort_list = []
for pro in range (5):
    process = []
    ran_len = random.randint(2,9)
    list_len.append(ran_len)
    for j in range (ran_len):
        ran_num = random.randint(0,20)
        process.append(ran_num)
    new_list.append(process)
for i in new_list:
    print("process:", i)
    unsort_list.append(len(i))
sort_list = numpy.sort(unsort_list)
print("---------------------------------------------")
print("unsorted length list:", unsort_list)
print("---------------------------------------------")
print("sorted length list:", sort_list)
print("---------------------------------------------")
for j in sort_list:
    for SJF in new_list:
        if (j==len(SJF)):
            new_list.remove(SJF)
            print("process after SJF:", SJF)
            break
print("\n--- ALL PROCESSES COMPLETED ---")
