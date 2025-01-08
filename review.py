# Review 1

def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list
"""
Answer: This method is working as expected. It will add value to the list passed in as paramater.
"""

# Review 2

def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."

"""
Answer: This method will treat {name} and {age} as string instead of reading value from parameter.
`correct_format_greeting` show the fix
"""
def correct_format_greeting(name, age):
    return f"Hello, my name is {name} and I am {age} years old."

# Review 3

class Counter:
    count = 0
    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count

"""
Answer: All it does is setting self.count to 1 when a new instance is created. There is no way to increment the counter
We should also implement method `increment` to increase the counter
"""
class Correct_Counter:
    count = 0
    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count
    
    def increment(self):
        self.count += 1

# Review 4

import threading
class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

def worker(counter):

    for _ in range(1000):

        counter.increment()

counter = SafeCounter()
threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

"""
Answer: This implementation start 10 threads, all of them are incrementing the same `SafeCounter` object.
As a result, counter.count will return 1000 * 10 = 10000 at the end of execution.
If we want each thread to have a different counter, we can keep the same definition on `SafeCounter` and `worker`, but passing new object whenever we start a new thread
"""
counters = []
threads = []

for _ in range(10):
    counter = SafeCounter()
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)
    counters.append(counter)

for t in threads:
    t.join()
print([counter.count for counter in counters]) # This print: [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000] 

# Review 5 
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1 # problem: "=+" this will always assign 1 to counts[item]
        else:
            counts[item] = 1
    return counts
"""
Answer: `counts[item] =+ 1` will always assign 1 to `counts[item]`
It should be `counts[item] += 1`
"""
def correct_count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1 # This will crement counts[item] by 1
        else:
            counts[item] = 1
    return counts
