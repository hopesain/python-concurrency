"""
This is a Python module that demonstrates the use of the asyncio library for asynchronous programming.
asyncio is a library to write concurrent code using the async/await syntax. I have copied this statement from the official documentation.
The code snippen below is just a simple example of how to use asyncio to run asynchronous functions concurrently.
"""

import asyncio

async def main():
    print("Welcome to the asyncio world!")
    await asyncio.sleep(1)  # Delay for one second
    print("We just getting started...")
    await asyncio.sleep(2)  # Delay for two second
    print("The mighty, Hello World!")
    
asyncio.run(main()) # Run the main function using asyncio's event loop. A quick observation, this should be placed outside the function.
    