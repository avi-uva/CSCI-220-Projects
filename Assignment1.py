# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 1 - Propositional Logic and Truth Tables
# Avraham Uvaydov

# Acknowledgements:
# I worked with the class

import inspect
import pandas as pd
from itertools import product


def func_body(f):
    body = inspect.getsource(f)  # gets the code
    idx = body.index("return")  # get the part after the word return
    return '"' + body[7 + idx:].strip() + '"'


# https://stackoverflow.com/questions/29548744/creating-a-truth-table-for-any-expression-in-python
def truth_table(f):
    values = [list(x) + [f(*x)] for x in product([False, True], repeat=f.__code__.co_argcount)]
    return pd.DataFrame(values, columns=(list(f.__code__.co_varnames) + [f.__name__]))


def impl(p, q):
    return not p or q


def bi_impl(p, q):
    return impl(p, q) and impl(q, p)


def f0(p, q, r):
    return (p or q) and r


def f1(p):
    return p and not p


def f2(p):
    return p or not p


def f3(p, q):
    return not p and impl(p, q)


def f4(p, q):
    return impl(p, q) or impl(q, p)


def f5(p, q):
    return (p or q) or (not p and not q)


def f6(p, q):
    return (p or q) and (not p and not q)


def f7(p, q, r):
    return impl(p, q) and impl(q, r)


def f8(p, q, r):
    return impl((impl(p, q) and impl(q, r)), impl(p, r))


# DeMorgan's First Law: ~(p | q) ↔ (~p & ~q)
def f9(p, q):
    return bi_impl(not (p or q), (not p and not q))


# DeMorgan's Second Law: ~(p & q) ↔ (~p | ~q)'''
def f10(p, q):
    return bi_impl(not (p and q), (not p or not q))


def analyze_truth_table(f):
    tt = truth_table(f)
    tt_rows = tt.shape[0]
    tt_cols = tt.shape[1]
    tt_vars = tt_cols - 1
    tt_type = None
    last_col = tt.iloc[:, tt_vars]
    if last_col.all():
        tt_type = "Tautology"
    elif last_col.any():  # LIKE ELSE IF
        tt_type = "Contingency"
    else:
        tt_type = "Contradiction"
    print("Name:", f.__name__, func_body(f))
    print(tt)
    print("Rows:", tt_rows, "Cols:", tt_cols, "Vars:", tt_vars, "Type:", tt_type)
    print()


# will tell us how many variables, rows, columns, whether it is a tautology, contingency, or contradiction


def main():
    for f in [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]:
        analyze_truth_table(f)


if __name__ == "__main__":  # use colons for if and def functions
    main()
