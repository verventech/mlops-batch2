import asyncio

# 1. Define an async function using 'async def'
async def fetch_data(delay, name):
    print(f"Starting {name}...")
    # Simulate a non-blocking wait using await asyncio.sleep()
    await asyncio.sleep(delay)
    print(f"Finished {name}!")
    return f"Data from {name}"

# 2. Define a main function to run our async tasks
async def main():
    # Run two tasks concurrently using asyncio.gather
    results = await asyncio.gather(
        fetch_data(2, "Task A"),
        fetch_data(1, "Task B")
    )
    print("All tasks completed:", results)

# 3. Entry point to run the async program
if __name__ == "__main__":
    asyncio.run(main())