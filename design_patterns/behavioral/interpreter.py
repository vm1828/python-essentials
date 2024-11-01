from abc import ABC, abstractmethod


class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self):
        ...


class NonTerminalExpression(AbstractExpression):

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        print("Non-terminal expression being interpreted...")
        # the expression could be either non-terminal or terminal,
        # which enables non-terminal expression class to continuously interpret multiple expressions,
        # until it reaches a terminal expression
        self._expression.interpret()


class TerminalExpression(AbstractExpression):

    def interpret(self):
        print("Terminal expression being interpreted...")


ast = NonTerminalExpression(NonTerminalExpression(TerminalExpression()))
ast.interpret()
