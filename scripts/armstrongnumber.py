def armstrong_number(n: int) -> bool:
    chars = str(n)
    calc = []
    for char in chars:
        calc.append(int(char) ** len(chars))
    result = sum(calc)
    if result != n:
        return False
    return True


print(armstrong_number(153))
