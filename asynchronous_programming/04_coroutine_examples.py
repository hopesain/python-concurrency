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

