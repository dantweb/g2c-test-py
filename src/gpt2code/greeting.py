def get_greeting(name: str) -> str:
    """Return a greeting message.
    
    Args:
        name: Name to include in greeting
        
    Returns:
        Formatted greeting string
    """
    return f"Hi, {name}"


def get_formal_greeting(name: str, title: str) -> str:
    """Return a formal greeting message.
    
    Args:
        name: Name to include in greeting
        title: Title of the person
        
    Returns:
        Formatted formal greeting string
    """
    return f"Dear {title} {name}"


def get_farewell(name: str) -> str:
    """Return a farewell message.
    
    Args:
        name: Name to include in farewell
        
    Returns:
        Formatted farewell string
    """
    return f"Goodbye, {name}"
