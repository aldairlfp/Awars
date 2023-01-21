class Node:
    pass


class ProgramNode(Node):
    def __init__(self, simulator, units, statements):
        self.simulator = simulator
        self.units = units
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
        self.params = params if params[0] is not None else []
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


class ConstantStringNode(AtomicNode):
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
    def __init__(self, start, condition, increment, body):
        self.start = start
        self.condition = condition
        self.increment = increment
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


class EqualsNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue == rvalue


class LessThanNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue < rvalue


class LessThanEqualsNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue <= rvalue


class GreaterThanNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue > rvalue


class GreaterThanEqualsNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue >= rvalue


class AndNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue and rvalue


class OrNode(BinaryNode):
    def operate(self, lvalue, rvalue):
        return lvalue or rvalue

class NotNode(ExpressionNode):
    def __init__(self, expression):
        self.expression = expression

class SimulatorNode(Node):
    def __init__(self, mode, max_turns):
        self.mode = mode
        self.max_turns = max_turns

class SimulatorPropertyNode(Node):
    pass

class UnitNode(SimulatorPropertyNode):
    def __init__(self, unit, number, team, behavior, strategy):
        self.unit = unit
        self.number = number
        self.team = team
        self.behavior = behavior
        self.strategy = strategy

class FieldNode(SimulatorPropertyNode):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class AllocateNode(Node):
    def __init__(self, allocate):
        self.allocate = allocate

class ExecuteSimulationNode(Node):
    pass
