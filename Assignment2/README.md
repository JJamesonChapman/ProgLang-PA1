# Lambda Calculus Interpreter in Python

## Authors

Jacob Jameson ID: 266882
Assisted by Tiffany Jameson
Original Code by Alex Kurz

## Installation

Requirements: `python` (`python3`) and `pip` (`pip3`).

Install with `source setup.sh`. Then `python interpreter_test.py` should pass all tests. You can run your own program in `test.lc` with `python interpreter.py test.lc`. You can run the interpreter from the command line with, for example, `python interpreter.py "(\x.x)a"`

## Description

This assignment modifies the starter Python interpreter for the untyped lambda calculus. The program uses Lark to parse lambda expressions, converts them into an abstract syntax tree (AST), performs beta reduction, and prints the resulting expression.

The goal of my modifications is to evaluate expressions to beta normal form when a normal form exists.

## Files

- `interpreter.py` — The starter interpreter with updated evaluation logic.
- `grammar.lark` — The original Lark grammar, kept unchanged.

## Running

python interpreter.py "[LAMBDA EQUATION HERE]"