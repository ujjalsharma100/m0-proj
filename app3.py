"""Third sample app entrypoint (same shape as app.py)."""


def format_greeting(name: str) -> str:
    """Return a personalized line when name is set, otherwise quiet mode."""
    if name:
        return f"Nice to meet you, {name}!"
    return "Running in quiet mode."


def normalize_display_name(raw: str) -> str:
    """Strip and title-case a non-empty name; empty input stays empty."""
    stripped = raw.strip()
    return stripped.title() if stripped else ""


def main() -> None:
    print("Hello from app3.py")
    name = input("Your name (optional, press Enter to skip): ")
    print(format_greeting(normalize_display_name(name)))


if __name__ == "__main__":
    main()
