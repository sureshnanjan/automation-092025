# format_example.py
# Examples for built-in format(value, format_spec) and str.format()

def demo_format():
    x = 123.456789

    print("Built-in format(value, format_spec):")
    print("Two decimals:", format(x, ".2f"))         # '123.46'
    print("Percentage:", format(0.75, ".0%"))         # '75%'

    print("\nHex formatting and width:")
    print("255 in hex (width 4, zero padded):", format(255, "04x"))  # '00ff'

    print("\nstr.format() examples:")
    name = "Shreya"
    print("Hello, {}!".format(name))
    print("Align left   |{:<10}|".format("hi"))
    print("Named fields: {n} scored {s:.1f}".format(n=name, s=95.234))

    print("\nF-strings (Python 3.6+):")
    print(f"{name} has {x:.1f} points")

if __name__ == "__main__":
    demo_format()
