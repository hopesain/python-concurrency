# python-concurrency
Concurrency in programming refers to the ability of a program to handle multiple tasks at the same time
It is mainly used in CPU or I/O Bound Tasks.
You must be wondering what are the so called "CPU Bound Tasks" or "I/O Bound Task".
Well roll up your sleeves.

## I/O Bound Tasks vs CPU Bound Tasks
Well here is my general understanding but I hope it is related.
A task may take long time (not necessaliry long but take some x amoung of time) to be completed due to two main reasons:
  1. It is waiting for something else (like external confirmation) first to complete before it gives you the result (I/O Bound Task).
  2. The task itself is too complex such that it needs much time to process it before it gives you the results (CPU Bound Task).
Still not clear, let me explain with examples below...

## I/O-Bound-Tasks  
