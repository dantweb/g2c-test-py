def get_greeting(name: str) -> str:
    """Generate greeting message.
    
    Args:
        name: Name to include in greeting
        
    Returns:
        Formatted greeting string
    """
    return f'Hi, {name}'


def main() -> None:
    """Main executable function."""
    print(get_greeting('PyCharm'))


if __name__ == '__main__':
    main()
