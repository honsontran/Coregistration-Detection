import os
#REPLACE PATH WITH YOURS :D
l = os.listdir(os.getcwd())
count = 5
for file_num in l[::1]:
    if (count %5 == 0):
        count = 1
    else:
        os.unlink(file_num)
        count = count + 1 