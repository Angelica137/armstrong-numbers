def armstrong_number(n: int) -> bool:
    chars = str(n)
    return n == sum([(int(char) ** len(chars)) for char in chars])
