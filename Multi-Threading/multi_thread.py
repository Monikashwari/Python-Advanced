"""
This program compares three different ways of executing I/O-bound tasks in Python.

1. Without Multithreading (Sequential Execution)
   - Tasks run one after another.
   - The next task starts only after the previous one finishes.
   - Simple to understand, but slower for I/O operations.

2. Traditional Multithreading (threading module)
   - A separate thread is created manually for each task.
   - Threads are started and managed explicitly using start() and join() and we need to manage the threads manually.
   - Provides concurrency, but thread management becomes complex as tasks increase.

3. Thread Pool (ThreadPoolExecutor)
   - A fixed pool of worker threads is created and reused.
   - Tasks are automatically assigned to available threads.
   - More efficient, scalable, and easier to manage than creating threads manually.
   - Demonstrated using both map() and submit() methods.

Use this program to observe the behavioral and performance differences
between sequential execution, manual thread management, and thread pooling.
"""
import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url:str):
    print(f"Fetching data from {url}...")
    time.sleep(5) # Simulating a delay in fetching data
    print(f"Data fetched from {url}!")
    return "Data from " + url

urls = [
    "https://api.example.com/data1",
    "https://api.example.com/data2", 
    "https://api.example.com/data3",
    "https://api.example.com/data4",
    "https://api.example.com/data5"
]
def without_multi_threading():
    for url in urls:
        fetch_data(url)
def with_multi_threading_traditional(): # This is the traditional way of using multi-threading which is using the threading module. We will create a thread for each URL and start the thread to fetch the data. We will also join the threads to wait for them to complete before exiting the program.
    import threading
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_data, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        
def multi_threading_threadpool_map(): # This is the first way of using ThreadPoolExecutor which is using the map function. The map function will take the function and the iterable as arguments and will return an iterator that will yield the results of the function for each item in the iterable.
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        executor.map(fetch_data, urls)

def multi_threading_threadpool_submit(): # This is the second way of using ThreadPoolExecutor which is using the submit function. The submit function will take the function and the arguments as arguments and will return a Future object which will represent the result of the function. We can use the result() method of the Future object to get the result of the function.
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        futures = [executor.submit(fetch_data, url) for url in urls]
        for future in futures:
            future.result() # This will wait for the thread to complete and get the result
while True:
    print("select the method of fetching data.. ")
    print("1.Without Multi-threading")
    print("2.With Multi-threading (traditional way )")
    print("3.Multi-threading (using ThreadPoolExecutor 1st way)")
    print("4.multi-threading (using ThreadPoolExecutor 2nd way)")
    print("5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        without_multi_threading()
    elif choice == 2:
        with_multi_threading_traditional()
    elif choice == 3:
        multi_threading_threadpool_map()
    elif choice == 4:
        multi_threading_threadpool_submit()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


