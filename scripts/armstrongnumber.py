def armstrong_number(n: int) -> bool:
    num_str = str(n)
    calc = []
    place = len(num_str)
    for char in num_str:
        calc.append(int(char) ** place)
        print(calc)
        place -= 1
    result = sum(calc)
    print(type(result))
    print(type(n))
    if result != n:
        return False
    return True


print(armstrong_number(9))
print(armstrong_number(10))
