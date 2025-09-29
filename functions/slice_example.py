# slice_example.py
# Examples using slice objects and slicing syntax

def demo_slice():
    s = "abcdefghijklmnopqrstuvwxyz"
    print("Slice s[2:10:2] ->", s[2:10:2])

    sl = slice(2, 10, 2)
    print("Using slice object:", s[sl])

    print("Reverse string using slice steps:", s[::-1])  # reversed

    nums = list(range(10))
    sl2 = slice(1, 8, 3)
    print("nums:", nums)
    print("nums[1:8:3] ->", nums[sl2])

    # slice.indices useful when you need safe start/stop adjusted to length
    example = "hello"
    print("slice(-4, 100).indices(len(example)) ->", slice(-4, 100).indices(len(example)))

if __name__ == "__main__":
    demo_slice()
