"""
A coroutine is a special function that can pause itself and let other tasks run, then resume where it left off.
In Python, any function defined with *async def* is a coroutine function, and when you call it, it returns a coroutine object, not the result.   
"""

import asyncio
from datetime import datetime


# Current time
def get_time(): 
    return datetime.now().strftime("%H:%M:%S.%f")[:-3] # This function returns the current time in HH:MM:SS.mmm format.

def time_taken(initial_time, final_time):
    duration = final_time - initial_time
    return duration

##### Let's first try to create a normal function.
def normal_function():
    return "Done"
result = normal_function()
print(result) # Output: Done

##### Now let's create a coroutine function.
async def coroutine_function():
    return "Done"
result = coroutine_function()
print(result)  # Output: <coroutine object coroutine_function at 0x...>, because to run a coroutine, you need to use a run method. This raises a RuntimeWarning.


# Creating the first coroutine function as guided by the official documentation.
async def say_after(duration, message): #The coroutine function takes two parameters: duration and message.
    await asyncio.sleep(duration)  # This line pauses the coroutine for the specified duration.
    print(message) # After the sleep, it prints the message.
    
async def main():
    print(f"Started at {get_time()}")
    initial_time = datetime.now()  # This line captures the current time before running the coroutines.
    await say_after(1, "Hello")  # This line calls the say_after coroutine with a 1-second delay and the message "Hello".
    await say_after(2, "World")  # This line calls the say_after coroutine with a 2-second delay and the message "World".
    print(f"Finished at {get_time()}")  # This line prints "Finished" after both say_after calls
    final_time = datetime.now()  # This line captures the current time after running the coroutines.
    duration = time_taken(initial_time, final_time)
    print(f"Time taken: {duration} seconds") # This line calculates and prints the time taken to run the coroutines.

asyncio.run(main())  # This line runs the main coroutine, which in turn runs the say_after coroutines sequentially.


# Running multiple coroutines concurrently using asyncio.create_task.
# Let’s modify the above example and run two say_after coroutines concurrently:

async def modified_main():
    task1 = asyncio.create_task(say_after(1, "Hello"))  # Create a task for the first coroutine
    task2 = asyncio.create_task(say_after(2, "World"))  # Create a task for the second coroutine
    
    
    # Wait until both tasks are completed (should take around 2 seconds.)
    print(f"Started modified_main at {get_time()}")
    initial_time = datetime.now()
    await task1
    await task2
    
    print(f"Finished modified_main at {get_time()}")
    final_time = datetime.now()
    duration = time_taken(initial_time, final_time)
    print(f"Time taken for modified_main: {duration} seconds") #Notice that using asyncio.create_task is one second faster.


asyncio.run(modified_main())  # This line runs the modified_main coroutine, which runs both say_after coroutines concurrently.


# The asyncio.TaskGroup class provides a more modern alternative to create_task() added in version 3.11. 
# Using this API, the last example becomes:
async def modern_main():
    print(f"Started modern_main at {get_time()}")
    initial_time = datetime.now()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, "Hello"))
        tg.create_task(say_after(2, "World"))
    print(f"Finished modern_main at {get_time()}")
    final_time = datetime.now()
    duration = time_taken(initial_time, final_time)
    print(f"Time taken for modern_main: {duration} seconds") #The duration is also one second faster to complete the tasks.

asyncio.run(modern_main())  # This line runs the modern_main coroutine, which runs both say_after coroutines concurrently.