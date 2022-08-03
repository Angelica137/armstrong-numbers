def armstrong_number(n: int) -> bool:
    chars = str(n)
    r = sum([(int(char) ** len(chars)) for char in chars])
    if r != n:
        return False
    return True
