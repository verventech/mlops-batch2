import time

def fetch_data():
    time.sleep(3) # Blocks everything for 3 seconds
    return "Data received"

def main():
    print("Fetching 1...")
    fetch_data()
    print("Fetching 2...")
    fetch_data()

main()