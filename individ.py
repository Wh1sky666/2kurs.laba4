#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check(S, start=0, current=0):

    if start == len(S):
        return current == 0

    if current < 0:
        return False

    if S[start] == "(" or S[start] == "[":
        return check(S, start + 1, current + 1)

    elif S[start] == ")" or S[start] == "]":
        return check(S, start + 1, current - 1)


if __name__ == '__main__':

    S = ["(", ")", "(", ")", "[", "["]
    print(check(S))

