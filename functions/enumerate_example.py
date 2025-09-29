# enumerate_example.py
# Examples showing usage of built-in enumerate()

def demo_enumerate():
    fruits = ["apple", "banana", "cherry"]
    print("Basic enumerate (index starts at 0):")
    for index, fruit in enumerate(fruits):
        print(index, fruit)

    print("\nStart index at 1:")
    for i, fruit in enumerate(fruits, start=1):
        print(i, fruit)

    print("\nMake an index->value dict with enumerate():")
    d = dict(enumerate(fruits))  # keys are indices
    print(d)

if __name__ == "__main__":
    demo_enumerate()
