def filter_even_numbers_fn(numbers):
    if not all(isinstance(n,int) for n in numbers):
        raise  ValueError("This should be an integer")
    return [n for n in numbers if n%2==0]