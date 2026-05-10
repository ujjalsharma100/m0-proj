"""Secondary sample entrypoint."""

from app import format_greeting


def main() -> None:
    print("Hello from app2.py")
    name = input("Your name (optional, press Enter to skip): ").strip()
    print(format_greeting(name))


if __name__ == "__main__":
    main()
