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

### LET'S CREATE A REAL LIFE EXAMPLE WHERE THIS IS USEFUL, THE USER CLICKS "PAY" ON OUR E-COMMERCE APP CALLED ILARA ###
### 1. We first send a payment request, ###
### 2. Wait for confirmation from a payment gateway whether paychangu, mobipay or others ### 
### 3. Return the confirmation message to the user ### 

# Sending a payment request
