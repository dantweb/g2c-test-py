from .greeting import get_greeting, get_formal_greeting, get_farewell


def main() -> None:
    """Main executable function."""
    print(get_greeting('PyCharm'))


if __name__ == '__main__':
    main()