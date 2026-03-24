import asyncio

async def worker(n):
    print(f"Tarefa: {n} iniciada.")
    await asyncio.sleep(n)
    print(f"Tarefa {n} finalizada.")

async def main():
    tasks = [asyncio.create_task(worker(n)) for n in range(1, 4)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())