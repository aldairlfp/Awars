class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements

class StatementNode(Node):
    pass

class ExpressionNode(Node):
    pass

class VarDeclarationNode(StatementNode):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression

class FunctionDeclarationNode(StatementNode):
    def __init__(self, id, params, body):
        self.id = id
        self.params = params
        self.body = body

class PrintNode(StatementNode):
    def __init__(self, expression):
        self.expression = expression

class AtomicNode(ExpressionNode):
    def __init__(self, lex):
        self.lex = lex

class BinaryNode(ExpressionNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right