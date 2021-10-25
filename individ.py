#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check(s):
    result = 0
    f = 0
    for a in s:
        if "(" in a:
            result += 1
        elif ")" in a:
            result -= 1
        if "[" in a:
            result += 1
        elif "]" in a:
            result -= 1

        else:
            return "Правильное расположение скобок"
    if result < 0:
        return "Неправильное расположение скобок"

    if result > 0:
        return "Неправильное расположение скобок"
    return "Правильное расположение скобок"


if __name__ == '__main__':
    s = input()
    print(check(s))
