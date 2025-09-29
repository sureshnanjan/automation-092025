# zip_example.py
# Examples showing usage of built-in zip()

def demo_zip():
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 78]

    print("Pairing names and scores with zip():")
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

    print("\nConvert zip to list of tuples:")
    pairs = list(zip(names, scores))
    print(pairs)

    print("\nIf lengths differ, zip stops at the shortest:")
    ages = [25, 30]  # shorter
    print(list(zip(names, ages)))  # Charlie is dropped

    print("\nUnzip (transpose) a zipped list:")
    names2, scores2 = zip(*pairs)
    print("names2:", names2)
    print("scores2:", scores2)

if __name__ == "__main__":
    demo_zip()
