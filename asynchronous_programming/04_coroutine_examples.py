"""
Just a few real-world examples of coroutines use cases in Python.
# Example 1: Sending emails to multiple recipients concurrently.
You looking for Example 2? It will probably be added later. Lol...
"""

import asyncio
from datetime import datetime

def get_time():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3] 

def time_taken(initial_time, final_time):
    duration = (final_time - initial_time)
    return duration

async def send_email(recipient, delay):
    print(f"Sending email to {recipient} at {get_time()}...")
    await asyncio.sleep(delay)
    print(f"Email sent to {recipient} at {get_time()}.")


#USING create_task TO SEND EMAILS CONCURRENTLY.
# Under normal circumastances, sending the emails below could take around 6 seconds, but with asyncio.create_task, it will take around 2 seconds.    
async def modified_main():
    print(f"Starting the email system at {get_time()}...")
    initial_time = datetime.now()
    
    first_task = asyncio.create_task(send_email("john@gmail.com", 2))
    second_task = asyncio.create_task(send_email("doe@gmail.com", 2))
    third_task = asyncio.create_task(send_email("hope@gmail.com", 2))
    
    await first_task
    await second_task
    await third_task
    
    final_time = datetime.now()
    print(f"📨 Finished all emails at {get_time()}")
    print(f"⏱ Time taken: {time_taken(initial_time, final_time)} seconds")
    
asyncio.run(modified_main())

#You still don't believe me. Let's try the synchronous one.

async def send_email_sync():
    print("#################################### SYNCHRONOUS EMAIL SENDING ####################################")
    print(f"Starting the email system at {get_time()}...")
    initial_time = datetime.now()
    
    first_task = send_email("john@gmail.com", 2)
    second_task = send_email("doe@gmail.com", 2)
    third_task = send_email("hope@gmail.com", 2)
    
    await first_task
    await second_task
    await third_task
    
    final_time = datetime.now()
    print(f"📨 Finished all emails at {get_time()}")
    print(f"⏱ Time taken: {time_taken(initial_time, final_time)} seconds") # This will take around 6 seconds to complete, because it is synchronous.

asyncio.run(send_email_sync())

async def modern_main():
    print(f"Starting the modern email system at {get_time()}")
    initial_time = datetime.now()
    
    async with asyncio.TaskGroup() as tg:
        tg.create_task(send_email("john@gmail.com", 2))
        tg.create_task(send_email("doe@gmail.com", 2))
        tg.create_task(send_email("hope@gmail.com", 2))
        
    final_time = datetime.now()
    print(f"📨 Finished all emails at {get_time()}")
    print(f"⏱ Time taken: {time_taken(initial_time, final_time)} seconds") # This will take around 2 seconds to complete, because it is using TaskGroup.

asyncio.run(modern_main())

#YOU MUST BE WONDERING BY NOW THAT ASYNCIO.CREATE_TASK AND ASYNCIO.TASKGROUP ARE THE SAME THING. WHY HAVE THEM BOTH
"""
REAL WORLD ANOLOGY
create_task() is like manual gears in a car: more control, but you must know what you're doing.
TaskGroup() is like an automatic gearbox: safer, easier, but less flexible when things get complex.    
"""