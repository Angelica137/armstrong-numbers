def armstrong_number(n: int) -> bool:
    n = str(n)
    calc = []
    place = len(n)
    for char in n:
        calc.append(int(char) ** place)
        place -= 1
    result = sum(calc)
    if result != n:
        return False
    return True
