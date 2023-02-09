def get_comparison_result(ver_a: list, ver_b: list) -> int:
    """Осущестляет сравнение версий."""
    if ver_a == ver_b:
        return 0
    if ver_a > ver_b:
        return 1
    return -1


def main() -> None:
    """Главная функция, точка входа."""
    ver_a = input("Enter version A: ").split('.')
    ver_b = input("Enter version B: ").split('.')
    print(get_comparison_result(ver_a, ver_b))


if __name__ == "__main__":
    main()


def test() -> None:
    """Тесты."""
    assert 1 == get_comparison_result("1.0.1", "1.0.0")
    assert 0 == get_comparison_result("1.0.0", "1.0.0")
    assert 1 == get_comparison_result("1.10.1", "1.1.0")
    assert -1 == get_comparison_result("1.0.1", "1.1.0")
    assert -1 == get_comparison_result("1.0.1", "2.0.0")

# test()
