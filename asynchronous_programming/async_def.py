import asyncio

async def fetch_data():
    print("Fetching data...")


async def fetch_order(order_id):
    print (f"Fetching order {order_id}...")
    await asyncio.sleep(2)
    print("Payment verified and order fetched successfully!")
    return {"order_id": order_id, "status": "paid"}
    
async def main():
    result = await fetch_order(123)
    print(f"[RESULT] Status response: {result}")
    
    
asyncio.run(main())

### LET'S CREATE A REAL LIFE EXAMPLE WHERE THIS IS USEFUL, LET'S SAY WE ORDER SOMETHING ON AMAZON ###
### 1. We first check if the object is available, ###
### 2. The user enters payment details ### 
### 3. You verify if the payment is successful ### 
### 4. You confirm the order. ###