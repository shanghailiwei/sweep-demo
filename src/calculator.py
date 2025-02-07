from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """将两个数相加。

    Args:
        a: 第一个数值
        b: 第二个数值

    Returns:
        两个数的和

    Examples:
        >>> add(1, 2)
        3
        >>> add(-1, 1)
        0
    """
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """将两个数相减。

    Args:
        a: 被减数
        b: 减数

    Returns:
        两个数的差

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(1, 1)
        0
    """
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """将两个数相乘。

    Args:
        a: 第一个因数
        b: 第二个因数

    Returns:
        两个数的乘积

    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(-2, 3)
        -6
    """
    return a * b

def divide(a: Number, b: Number) -> float:
    """将两个数相除。

    Args:
        a: 被除数
        b: 除数

    Returns:
        两个数的商

    Raises:
        ValueError: 当除数为0时抛出

    Examples:
        >>> divide(6, 2)
        3.0
        >>> divide(5, 2)
        2.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
