### RUNNING TASKS CONCURRENTLY USING asyncio.gather(*aws, return_exceptions=False) ###
"""
Run awaitable objects in the aws sequence concurrently.

If any awaitable in aws(awaitables) is a coroutine, it is automatically scheduled as a Task.

If all awaitables are completed successfully, the result is an aggregate list of returned values. The order of result values corresponds to the order of awaitables in aws.

If return_exceptions is False (default), the first raised exception is immediately propagated to the task that awaits on gather(). Other awaitables in the aws sequence won’t be cancelled and will continue to run.

If return_exceptions is True, exceptions are treated the same as successful results, and aggregated in the result list.

If gather() is cancelled, all submitted awaitables (that have not completed yet) are also cancelled.

If any Task or Future from the aws sequence is cancelled, it is treated as if it raised CancelledError – the gather() call is not cancelled in this case. This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled.    
"""

import asyncio
from datetime import datetime

## Just tryna work...


def get_time(): 
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

def time_taken(initial_time, final_time):
    duration = final_time - initial_time
    return duration

# TO BETTER UNDERSTAND THE CONCEPT, LET'S SIMULATE A SITUATION WHERE YOU ARE THE CHEF COOKING MULTIPLE DISHES IN THE KITCHEN.
"""
You are preparing three dishes.
Each dish has multiple steps (e.g., prep, cook, plate).
Each step takes 1 second.
Instead of cooking them one after another, we’ll use asyncio.gather() to switch between tasks as each step waits.
"""

async def cook_dish(dish_name, steps):
    print(f"Starting to prepare {dish_name} at {get_time()}")
    for i in range(1, steps + 1): #Kindly visit the mastering loops section to understand the range function and loops in general.
        print(f"{dish_name} - Step {i} started at {get_time()} - Step {i}/{steps}")
        await asyncio.sleep(1)
    print(f"{dish_name} is ready at {get_time()}")
    return f"{dish_name} is completed!"

async def main():
    print(f"Kitchen opens up and start to cook at {get_time()}")
    initial_time = datetime.now()
    
    results = await asyncio.gather(
        cook_dish("Nsima", 4),
        cook_dish("Soya pieces", 3),
        cook_dish("Mabilinganya", 2),
    ) # Notice that we have not specified the return_exceptions parameter, so it defaults to False.
    
    print(f"[{get_time()}] 🧾 All dishes done!")
    print("🍽️ Summary:")
    for r in results:
        print(" -", r)
    
    final_time = datetime.now()
    duration = time_taken(initial_time, final_time)
    print(f"Time taken: {duration} seconds")    
        
asyncio.run(main())