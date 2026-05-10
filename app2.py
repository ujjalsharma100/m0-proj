"""Secondary sample entrypoint."""

from app import format_greeting


def read_optional_name() -> str:
    return input("Your name (optional, press Enter to skip): ").strip()


def print_intro() -> None:
    print("Hello from app2.py")


def main() -> None:
    print_intro()
    name = read_optional_name()
    print(format_greeting(name))


if __name__ == "__main__":
    main()
