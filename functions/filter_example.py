# filter_example.py
# Examples showing built-in filter()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def demo_filter():
    nums = range(1, 21)
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("Evens:", evens)

    primes = list(filter(is_prime, nums))
    print("Primes:", primes)

    values = ["", "hello", None, "world", 0, 5]
    truthy = list(filter(None, values))  # removes falsy values: '', None, 0
    print("Truthy values (filter(None,...)):", truthy)

if __name__ == "__main__":
    demo_filter()
