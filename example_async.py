import asyncio

# Async functions are marked with 'async' and called with 'await'
async def hello(task):
    print(f"Hello {task}")

async def main():
    tasks = range(10)

    print(f"Asyncio")
 
    # Process tasks in parallel
    results = await asyncio.gather(*[hello(t) for t in tasks])

if __name__ == '__main__':
    # Running async functions needs the asyncio.run wrapper at the top level
    asyncio.run(main())
