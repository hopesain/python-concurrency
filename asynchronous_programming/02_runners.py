"""
This section is about runners from the asyncio library.
A runner is a function that runs an asynchronous function and returns the result.
In simple terms, it is something that starts and manages the event loop for your asynchronous code.
An event loop is the engine that drives async code — a runner is what gets the engine started, manages its life cycle, and stops it safely.

"""

import asyncio

async def main():
    print("start")
    await asyncio.sleep(2) # Sleep for 2 seconds.
    print("end")

asyncio.run(main()) # This is the runner that starts the event loop and runs the main function.


### RUNNERS CONTEXT MANAGERS ###
"""
It is a manual way to manage the event loop's lifecycle using a context manager (With statement).
You can use it to run multiple tasks without having to create a new event loop each time.    
"""

async def first_task():
    await asyncio.sleep(1)
    print("First task completed!")
    
    
async def second_task():
    await asyncio.sleep(2)
    print("Second task completed!")
    

with asyncio.Runner() as runner: 
    runner.run(first_task())  # This will run the first_task coroutine within the event loop managed by the Runner context manager.
    runner.run(second_task())  # This will run the second_task coroutine within the same event loop.