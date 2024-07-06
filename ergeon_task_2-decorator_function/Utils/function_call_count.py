def count_calls(func):
    # Dictionary to store counts for each function
    counts = {}
    
    def wrapper(*args, **kwargs):
        # Check or initialize count 
        if func not in counts:
            counts[func] = 0

        counts[func] += 1
        # Print the count
        print(f"{func.__name__} has been called {counts[func]} times")

        return func(*args, **kwargs)
    
    return wrapper