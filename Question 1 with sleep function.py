#NAME MALIK ABDUL HADI
#REG NO : 200901053
#COURSE: OPERATING SYSTEM LAB
#SUBMITTED TO : MADAM REEDA

#Question 1:

#Program to create 2 threads.
#1)To increment the value of shared variable.
#2)To decrement the value of shared variable.
#3)Show the output with sleep function.

#WITH SLEEP FUNCTION :

import threading
import time

sharedVariable = int(input("Please enter the value of shared variable: "))
print("Original value of shared variable is: ", sharedVariable)

def increment_variable():
    global sharedVariable
    for i in range(5):
        time.sleep(1)
        sharedVariable += 1
        print("Shared Variable after Increment =", sharedVariable)

def decrement_variable():
    global sharedVariable
    for i in range(5):
        time.sleep(1)
        sharedVariable -= 1
        print("Shared Variable after Decrement =", sharedVariable)

thread1 = threading.Thread(target=increment_variable)
thread2 = threading.Thread(target=decrement_variable)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("\nFinished Threading.")
print("\n")
print("So, the final value of the shared variable is =", sharedVariable)