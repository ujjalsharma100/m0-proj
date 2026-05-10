"""Small sample app entrypoint."""


def format_greeting(name: str) -> str:
    """Return a personalized line when name is set, otherwise quiet mode."""
    if name:
        return f"Nice to meet you, {name}!"
    return "Running in quiet mode."


def main() -> None:
    print("Hello from app.py")
    name = input("Your name (optional, press Enter to skip): ").strip()
    print(format_greeting(name))


if __name__ == "__main__":
    main()
