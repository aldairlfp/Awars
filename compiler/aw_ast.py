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
    def __init__(self, id, expression, reassignament=False):
        self.id = id
        self.expression = expression
        self.reassignament = reassignament


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

    def operate(self, lvalue, rvalue):
        raise NotImplementedError()


class ConstantNumNode(AtomicNode):
    pass


class VariableNode(AtomicNode):
    pass


class IfNode(StatementNode):
    def __init__(self, condition, then, else_):
        self.condition = condition
        self.then = then
        self.else_ = else_


class WhileNode(StatementNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class ForNode(StatementNode):
    def __init__(self, id, start, end, body):
        self.id = id
        self.start = start
        self.end = end
        self.body = body


class ReturnNode(StatementNode):
    def __init__(self, expression):
        self.expression = expression


class BreakNode(StatementNode):
    pass


class ContinueNode(StatementNode):
    pass


class CallNode(AtomicNode):
    def __init__(self, id, args):
        AtomicNode.__init__(self, id)
        self.args = args


class PlusNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue + rvalue

class MinusNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue - rvalue

class StarNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue * rvalue

class DivNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue / rvalue
