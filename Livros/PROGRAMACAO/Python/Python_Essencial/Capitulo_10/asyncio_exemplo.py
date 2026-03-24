import asyncio

async def hello():
    print("Olá,")
    await asyncio.sleep(1)
    print("Mundo!")
    

if __name__ == "__main__":
    asyncio.run(hello())