You're up!
I provided you with a code snippet to draw a Julia fractale. 
The code is very slow (especially in High Definition, feel free to try a lower resolution for your first steps).
Use your Cython magic to make it faster!
Your report should include a quick time execution measurement of the initial code (you can use a lower resolution, and stick to it until the end. Also, you might want to create functions yourself).
Then, introduce step by step a couple Cython tricks, measure the time execution performance and quickly explain what happened and what can be done next.
For example, start with a couple cdef inside the function body, time it.
Then introduce typed memoryviews (array), or change the function declaration.

This is fairly freeform - there is no exact answer, I just want to see a quick investigation and a couple Cython tricks that we saw (feel free to lookup additional tricks online too). Feel free to introduce additional functions too!

Have fun!

