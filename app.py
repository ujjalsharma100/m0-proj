"""Small sample app entrypoint."""

def main() -> None:
    print("Hello from app.py")
    name = input("Your name (optional, press Enter to skip): ").strip()
    if name:
        print(f"Nice to meet you, {name}!")
    else:
        print("Running in quiet mode.")


if __name__ == "__main__":
    main()
