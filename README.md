# Two-threads-to-decrement-and-increment-the-value-of-shared-variable-.

# EXPLANATION OF THE CODE:

This will create two threads and start them. The threads will run concurrently, and the main program will wait for both threads to finish before continuing and printing "Both threads have finished" and the final value of the shared variable.

The increment_variable and decrement_variable functions each increment and decrement the shared variable, respectively, in a loop 5 times. The time.sleep(1) function is used to pause the execution of each thread for 1 second between each iteration of the loop. This is done to allow the other thread to run and make changes to the shared variable.

To show the output without the sleep function, you can simply remove the time.sleep(1) line from both functions. This will cause the threads to run as fast as possible, without any pauses.


# OUTPUT WITH SLEEP FUNCTION:

![image](https://user-images.githubusercontent.com/92660593/212484244-d8954c9b-d09b-4ca1-8ed8-75899f003c59.png)

# OUTPUT WITHOUT SLEEP FUNCTION:

![image](https://user-images.githubusercontent.com/92660593/212484331-29f85703-256b-48bd-9e60-a6789ccd982e.png)
