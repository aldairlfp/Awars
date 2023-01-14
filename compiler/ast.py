class Node:
    pass


class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements


class StatementNode(Node):
    def __init__(self, lineno) -> None:
        self.lineno = lineno


class ExpressionNode(Node):
    pass


class VarDeclarationNode(StatementNode):
    def __init__(self, id, expression, lineno):
        self.id = id
        self.expression = expression
        super().__init__(lineno)


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


class ConstantNumNode(AtomicNode):
    pass


class VariableNode(AtomicNode):
    pass


class IfNode(StatementNode):
    def __init__(self, condition, then, else_, lineno):
        self.condition = condition
        self.then = then
        self.else_ = else_
        super().__init__(lineno)


class WhileNode(StatementNode):
    def __init__(self, condition, body, lineno):
        self.condition = condition
        self.body = body
        super().__init__(lineno)


class ForNode(StatementNode):
    def __init__(self, id, start, end, body, lineno):
        self.id = id
        self.start = start
        self.end = end
        self.body = body
        super().__init__(lineno)


class ReturnNode(StatementNode):
    def __init__(self, expression, lineno):
        self.expression = expression
        super().__init__(lineno)


class BreakNode(StatementNode):
    pass


class ContinueNode(StatementNode):
    pass


class CallNode(AtomicNode):
    def __init__(self, id, args):
        AtomicNode.__init__(self, id)
        self.args = args


class PlusNode(BinaryNode):
    pass


class MinusNode(BinaryNode):
    pass


class StarNode(BinaryNode):
    pass


class DivNode(BinaryNode):
    pass
