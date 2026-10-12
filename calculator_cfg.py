import math
import sys

from lark import Lark, Transformer, v_args


#Abstract Syntax Tree
@v_args(inline=True)
class BuildAST(Transformer):

    def number(self, token):
        return ("number", float(token))

    def add(self, left, right):
        return ("add", left, right)

    def sub(self, left, right):
        return ("sub", left, right)

    def mul(self, left, right):
        return ("mul", left, right)

    def pow(self, left, right):
        return ("pow", left, right)

    def neg(self, child):
        return ("neg", child)

    def log(self, value, base):
        return ("log", value, base)


#Evaluate AST
def evaluate(ast):

    operation = ast[0]

    if operation == "number":
        return ast[1]

    if operation == "neg":
        return -evaluate(ast[1])

    left = evaluate(ast[1])
    right = evaluate(ast[2])

    if operation == "add":
        return left + right

    if operation == "sub":
        return left - right

    if operation == "mul":
        return left * right

    if operation == "pow":
        return left ** right

    if operation == "log":
        return math.log(left, right)

    raise ValueError("Unknown operation")


#Main
def main():

    if len(sys.argv) != 2:
        print('Usage: python calculator_cfg.py "1+2*3"')
        sys.exit(1)

    #Load grammar and create parser
    parser = Lark.open(
        "grammar.lark",
        rel_to=__file__,
        parser="lalr"
    )

    expression = sys.argv[1]

    parse_tree = parser.parse(expression)

    ast = BuildAST().transform(parse_tree)

    result = evaluate(ast)

    print(f"{result:.15g}")


if __name__ == "__main__":
    main()
