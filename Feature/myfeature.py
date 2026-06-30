def greet(name="World"):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def main():
    print(greet())
    print(greet("Developer"))


if __name__ == "__main__":
    main()
