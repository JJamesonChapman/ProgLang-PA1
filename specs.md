# Calculator Implementation Specification

## 1. Overview

This project implements a calculator using Python
and the Lark parsing library.

The calculator supports:

- Addition
- Subtraction
- Multiplication
- Exponentiation
- Unary negation
- Logarithms with an explicit base
- Parentheses

The implementation generates an Abstract Syntax Tree
(AST) and then recursively evaluates it.

## 2. Context-Free Grammar

The grammar is defined in grammar.lark.

The original grammar was ambiguous because it did
not specify operator precedence or associativity.

Our implementation uses separate grammar rules
to enforce the intended order of operations.

Exponentiation is right-associative.

Addition, subtraction, and multiplication are
left-associative.

Parentheses override the normal precedence rules.

## 3. Abstract Syntax Tree

The BuildAST class extends Lark's Transformer class.

It converts the parser's output into tuples representing
operations and their operands.

For example:

1+2

Becomes:

("add", ("number", 1), ("number", 2))

Each AST node represents either a number,
a unary operation, or a binary operation.

## 4. Evaluation

The evaluate(ast) function recursively processes
the Abstract Syntax Tree.

For a number node, it returns the stored value.

For unary negation, it recursively evaluates
the operand and negates the result.

For binary operations, it recursively evaluates
the left and right operands before applying
the appropriate mathematical operation.

## 5. Main Program

The main() function performs the following operations:

1. Reads the expression from the command line.
2. Loads grammar.lark.
3. Generates a Lark parser.
4. Parses the input expression.
5. Converts the parse tree into an AST.
6. Recursively evaluates the AST.
7. Prints the result.

## 6. Testing

The implementation was tested using expressions
covering arithmetic, parentheses, exponentiation,
negation, and logarithms.

The test cases verify operator precedence
and associativity.
