import time
import asyncio


def fetch_data():
    print("fetch data enter")
    time.sleep(3)
    print("fetch  end")



async def main():
    task1=asyncio.create_task(asyncio.to_thread(fetch_data))
    task2=asyncio.create_task(asyncio.to_thread(fetch_data))
    result1=await task1
    result2=await task2
    print("both task must end")
    print("complete work")




 
asyncio.run(main())