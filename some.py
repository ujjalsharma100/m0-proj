"""Read names from some.txt and print them."""

from pathlib import Path


def main() -> None:
    path = Path(__file__).resolve().parent / "some.txt"
    text = path.read_text(encoding="utf-8")
    members = [line.strip() for line in text.splitlines() if line.strip()]
    for member in members:
        print(member)


if __name__ == "__main__":
    main()
