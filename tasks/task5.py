def get_initial_data() -> tuple[list[str], list[str]]:
    """Получение исходных данных. Удаление лишних нулей в версиях."""
    ver_a = input("Enter version A: ").lstrip("0").split(".")
    ver_b = input("Enter version B: ").lstrip("0").split(".")
    return ver_a, ver_b


def validate_initial_data(ver_a, ver_b) -> None:
    """Валидация входных данных."""
    try:
        list(map(int, ver_a))
        list(map(int, ver_b))
    except ValueError as error:
        print(error, "Enter versions in the format '0.0.0...'", sep="\n")
        main()


def get_comparison_result(ver_a: list[str], ver_b: list[str]) -> int:
    """Сравнение двух версий."""
    if ver_a == ver_b:
        return 0

    while not len(ver_a) == len(ver_b):
        if len(ver_a) < len(ver_b):
            ver_a.append("0")
            continue
        ver_b.append("0")

    for i in range(len(ver_a)):
        if len(ver_a[i]) == len(ver_b[i]):
            continue
        while not len(ver_a[i]) == len(ver_b[i]):
            if len(ver_a[i]) < len(ver_b[i]):
                ver_a[i] += "0"
                continue
            ver_b[i] += "0"

    if ver_a > ver_b:
        return 1
    return -1


def main():
    """Главная функция, точка входа."""
    ver_a, ver_b = get_initial_data()
    validate_initial_data(ver_a, ver_b)
    print(get_comparison_result(ver_a, ver_b))


if __name__ == "__main__":
    main()


def test() -> None:
    """Тесты."""
    assert 1 == get_comparison_result(["1", "0", "1"], ["1", "0", "0"])
    assert 1 == get_comparison_result(["1", "0", "1"], ["1", "000", "0"])
    assert 0 == get_comparison_result(["1", "0", "0"], ["1", "0", "0"])
    assert 1 == get_comparison_result(["1", "10", "1"], ["1", "1", "0"])
    assert -1 == get_comparison_result(["1", "0", "1"], ["1", "1", "0"])
    assert -1 == get_comparison_result(["1", "0", "1"], ["2", "0", "0"])
    assert 1 == get_comparison_result(["1", "0", "1"], ["1", "0", "01"])
    assert -1 == get_comparison_result(["1", "0", "1", "9"], ["2", "0", "0"])


# test()
