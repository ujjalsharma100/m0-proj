"""Secondary sample entrypoint."""

from app import format_greeting


def read_optional_name() -> str:
    return input("Your name (optional, press Enter to skip): ").strip()


def normalize_user_input(name: str) -> str:
    """Title-case a non-empty name from optional user input."""
    return name.title() if name else ""


def print_intro() -> None:
    print("Hello from app2.py")


def main() -> None:
    print_intro()
    name = normalize_user_input(read_optional_name())
    print(format_greeting(name))


if __name__ == "__main__":
    main()
