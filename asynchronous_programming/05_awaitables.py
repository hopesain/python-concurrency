### MOST OF THE INFO ABOUT THIS TOPIC IS FROM THE OFFICIAL PYTHON DOCUMENTATION ####
"""
We say that an object is an awaitable object if it can be used in an await expression. Many asyncio APIs are designed to accept awaitables.
There are three main types of awaitable objects: coroutines, Tasks, and Futures.    
"""

### COROUTINES ###
# Python coroutines are awaitables and therefore can be awaited from other coroutines

import asyncio

async def nested():
    return 50

async def coroutines_main():
    # nested() # This line creates a coroutine object but does not await it. It raises a RuntimeWarning.
    print(await nested())
    
asyncio.run(coroutines_main())


### TASKS ###
"""
Tasks are used to schedule coroutines concurrently.
When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon:
"""

async def task_main():
    # Schedule nested() to run soon concurrently
    # with "task_main()
    
    task = asyncio.create_task(nested())
    
    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task
    print("Task completed...")
    print(task.result())

asyncio.run(task_main())


#### FUTURES ###
"""
I did not bother to include this section because the documentation stated that I would not use it in most cases.
'Normally there is no need to create Future objects at the application level code.' Copied from the official documentation.
"""