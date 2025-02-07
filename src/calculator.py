from typing import Union
from decimal import Decimal

Number = Union[int, float, Decimal]

class CalculatorError(Exception):
    """计算器基础异常类。"""
    pass

class DivisionByZeroError(CalculatorError):
    """除数为零时的异常。"""
    pass

class InvalidInputError(CalculatorError):
    """输入无效时的异常。"""
    pass

def add(a: Number, b: Number) -> Number:
    """将两个数相加。

    Args:
        a: 第一个数值
        b: 第二个数值

    Returns:
        两个数的和

    Raises:
        InvalidInputError: 当输入不是数字时抛出

    Examples:
        >>> add(1, 2)
        3
        >>> add(-1, 1)
        0
    """
    try:
        return float(a) + float(b)
    except (TypeError, ValueError):
        raise InvalidInputError("输入必须是数字")

def subtract(a: Number, b: Number) -> Number:
    """将两个数相减。

    Args:
        a: 被减数
        b: 减数

    Returns:
        两个数的差

    Raises:
        InvalidInputError: 当输入不是数字时抛出

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(1, 1)
        0
    """
    try:
        return float(a) - float(b)
    except (TypeError, ValueError):
        raise InvalidInputError("输入必须是数字")

def multiply(a: Number, b: Number) -> Number:
    """将两个数相乘。

    Args:
        a: 第一个因数
        b: 第二个因数

    Returns:
        两个数的乘积

    Raises:
        InvalidInputError: 当输入不是数字时抛出

    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(-2, 3)
        -6
    """
    try:
        return float(a) * float(b)
    except (TypeError, ValueError):
        raise InvalidInputError("输入必须是数字")

def divide(a: Number, b: Number) -> float:
    """将两个数相除。

    Args:
        a: 被除数
        b: 除数

    Returns:
        两个数的商

    Raises:
        DivisionByZeroError: 当除数为0时抛出
        InvalidInputError: 当输入不是数字时抛出

    Examples:
        >>> divide(6, 2)
        3.0
        >>> divide(5, 2)
        2.5
    """
    try:
        a, b = float(a), float(b)
        if b == 0:
            raise DivisionByZeroError("除数不能为零")
        return a / b
    except (TypeError, ValueError):
        raise InvalidInputError("输入必须是数字")
