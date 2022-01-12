import os
import time
a=input("how many times you want Dr.Strange bargain >> ")
a=int(a)
for i in range(a):
    if i<a*0.6:
        print("Dormammu I've Come To Bargain")
    elif i<a*0.8:
        print("Dormammu I've Come ")
    else:
        print("Dormammu")
    time.sleep(0.8)

print("\nDormammu:What do you want!")
os.system("pause")
