import compiler.cmp.visitor as visitor
from compiler.context import Scope
from compiler.aw_ast import *
from compiler.utils import BreakException, ContinueException, FloatStringException, ReturnException
from simulation.simulation import Simulator
import copy


class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ProgramNode [<stat>; ... <stat>;]'
        statements = '\n'.join(self.visit(child, tabs + 1)
                               for child in node.statements)
        return f'{ans}\n{statements}'

    @visitor.when(PrintNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__PrintNode <expr>'
        expr = self.visit(node.expression, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(VarDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__VarDeclarationNode: let {node.id} = <expr>'
        expr = self.visit(node.expression, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(FunctionDeclarationNode)
    def visit(self, node, tabs=0):
        params = ', '.join(node.params)
        ans = '\t' * tabs + \
            f'\\__FuncDeclarationNode: func {node.id}({params}) <statement_list>'
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'

    @visitor.when(BinaryNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__<expr> {node.__class__.__name__} <expr>'
        left = self.visit(node.left, tabs + 1)
        right = self.visit(node.right, tabs + 1)
        return f'{ans}\n{left}\n{right}'

    @visitor.when(AtomicNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ {node.__class__.__name__}: {node.lex}'

    @visitor.when(CallNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__CallNode: {node.lex}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.args)
        return f'{ans}\n{args}'

    @visitor.when(IfNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__IfNode: if <expr> <statement_list> else <statement_list>'
        condition = self.visit(node.condition, tabs + 1)
        then = '\n'.join(self.visit(child, tabs + 1) for child in node.then)
        if node.else_ is None:
            else_ = '\t' * (tabs + 1) + '\\__else: None'
        else:
            else_ans = '\t' * tabs + '\\__else: <statement_list>'
            else_ = '\n'.join(self.visit(child, tabs + 1)
                              for child in node.else_)
            else_ = f'{else_ans}\n{else_}'
        return f'{ans}\n{condition}\n{then}\n{else_}'

    @visitor.when(ReturnNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ReturnNode: return <expr>'
        expr = self.visit(node.expression, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(WhileNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__WhileNode: while <expr> <statement_list>'
        condition = self.visit(node.condition, tabs + 1)
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{condition}\n{body}'

    @visitor.when(ForNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + \
            f'\\__ForNode: for(start; condition; increment) <statement_list>'
        start = self.visit(node.start, tabs + 1)
        condition = self.visit(node.condition, tabs + 1)
        increment = self.visit(node.increment, tabs + 1)
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{start}\n{condition}\n{increment}\n{body}'

    @visitor.when(BreakNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__BreakNode'

    @visitor.when(ContinueNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ContinueNode'


class SemanticCheckerVisitor(object):
    def __init__(self):
        self.errors = []
        self.simulator = None
        self.units = []

    @visitor.on('node')
    def visit(self, node, scope):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        if scope is None:
            scope = Scope()
        for child in node.statements:
            try:
                self.visit(child, scope)
            except ContinueException:
                self.errors.append('Continue outside loop')
            except BreakException:
                self.errors.append('Break outside loop')
            except ReturnException:
                self.errors.append(f'Return outside function')
        return self.errors

    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):
        is_var_defined = scope.is_var_defined(node.id)
        if is_var_defined and not node.reassignament:
            self.errors.append(f'Variable {node.id} already declared')
        elif not is_var_defined and node.reassignament:
            self.errors.append(f'Variable {node.id} it is not declared')
        else:
            result = self.visit(node.expression, scope)
            scope.define_variable(node.id, result)

    @visitor.when(FunctionDeclarationNode)
    def visit(self, node, scope):
        if scope.is_func_defined(node.id, len(node.params)):
            self.errors.append(f'Function {node.id} already declared')
        else:
            scope.define_function(node.id, node.params)
            child_scope = scope.create_child_scope()
            for param in node.params:
                child_scope.define_variable(param, None)
            for statement in node.body:
                try:
                    self.visit(statement, child_scope)
                except ReturnException:
                    pass

    @visitor.when(PrintNode)
    def visit(self, node, scope):
        self.visit(node.expression, scope)

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        pass

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        if not scope.is_var_defined(node.lex):
            self.errors.append(f'Variable {node.lex} not declared')

    @visitor.when(CallNode)
    def visit(self, node, scope):
        if not scope.is_func_defined(node.lex, len(node.args)):
            self.errors.append(f'Function {node.lex} not declared')

    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)

    @visitor.when(IfNode)
    def visit(self, node, scope):
        self.visit(node.condition, scope)
        for child in node.then:
            self.visit(child, scope.create_child_scope())
        if node.else_ is not None:
            for stmt in node.else_:
                self.visit(stmt, scope.create_child_scope())

    @visitor.when(WhileNode)
    def visit(self, node, scope):
        self.visit(node.condition, scope)
        child_scope = scope.create_child_scope()
        for child in node.body:
            try:
                self.visit(child, child_scope)
            except ContinueException:
                pass
            except BreakException:
                pass

    @visitor.when(ForNode)
    def visit(self, node, scope):
        self.visit(node.start, scope)
        self.visit(node.condition, scope)
        self.visit(node.increment, scope)
        child_scope = scope.create_child_scope()
        for child in node.body:
            try:
                self.visit(child, child_scope)
            except ContinueException:
                pass
            except BreakException:
                pass

    @visitor.when(BreakNode)
    def visit(self, node, scope):
        raise BreakException()

    @visitor.when(ContinueNode)
    def visit(self, node, scope):
        raise ContinueException()

    @visitor.when(ReturnNode)
    def visit(self, node, scope):
        raise ReturnException(1)

    @visitor.when(SimulatorNode)
    def visit(self, node, scope):
        if self.simulator is None:
            try:
                self.simulator = Simulator(node.mode(), int(node.max_turns))
            except Exception as e:
                print(e)

    @visitor.when(UnitNode)
    def visit(self, node, scope):
        if self.simulator is None:
            self.errors.append(f'''Units {node.unit.__name__} can not be created in a simulation that it is not defined''')
        else:
            self.units = [] if self.units is None else self.units
            if self.simulator is not None:
                self.simulator.units(node.unit, int(node.number), node.team, node.behavior)
                for unit in self.simulator.unit():
                    unit.strategy(node.behavior, node.strategy(unit))


    @visitor.when(FieldNode)
    def visit(self, node, scope):
        if self.simulator is None:
            self.errors.append(f'''Field can not be created in a simulation that it is not defined''')
        else:
            self.simulator.board(int(node.height), int(node.width))

    @visitor.when(AllocateNode)
    def visit(self, node, scope):
        if self.simulator is None:
            self.errors.append(f'''The units can not be allocate in a simulation that it is not defined''')
        else:
            self.simulator.allocate_units(node.allocate, self.simulator.unit())

    @visitor.when(ExecuteSimulationNode)
    def visit(self, node, scope):
        if self.simulator is None:
            self.errors.append(f'''The simulation can not be executed because it is not defined''')
        if self.simulator.board_s() == None:
            self.errors.append(f'''The simulation can not be executed because the field are not defined''')
        if len(self.simulator.unit()) > 0:
            for unit in self.simulator.unit():
              if unit.pos_s() == None:
                self.errors.append(f'''The simulation can not be executed because the units are not allocate''')
                break
            
class EvaluatorVisitor(object):
    def __init__(self):
        self.errors = []
        self.functions = {}
        self.simulator = None
        self.units = None

    @visitor.on('node')
    def visit(self, node, scope):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        if scope is None:
            scope = Scope()
        try:
            for child in node.statements:
                self.visit(child, scope)
        except FloatStringException():
            pass
        return self.errors

    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):
        result = self.visit(node.expression, scope)
        scope.define_variable(node.id, result, node.reassignament)

    @visitor.when(FunctionDeclarationNode)
    def visit(self, node, scope):
        child_scope = scope.create_child_scope()
        child_scope.define_function(node.id, node.params)
        for param in node.params:
            child_scope.define_variable(param, None)
        self.functions[node.id] = (node, child_scope)

    @visitor.when(PrintNode)
    def visit(self, node, scope):
        print(self.visit(node.expression, scope))

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        return node.lex

    @visitor.when(ConstantStringNode)
    def visit(self, node, scope):
        return node.lex

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        return scope.get_variable(node.lex).value

    @visitor.when(CallNode)
    def visit(self, node, scope):
        func, func_scope = self.functions[node.lex]
        func_scope_c = copy.deepcopy(func_scope)
        for i, param in enumerate(func.params):
            arg = self.visit(node.args[i], scope)
            func_scope_c.redefine_call_arg(param, arg)
        for body in func.body:
            try:
                self.visit(body, func_scope_c)
            except ReturnException as e:
                return e.value

    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        if isinstance(left, str) and isinstance(right, float) or \
                isinstance(left, float) and isinstance(right, str):
            self.errors.append('Cannot operate between string and number')
            raise FloatStringException()
        else:
            return node.operate(left, right)

    @visitor.when(NotNode)
    def visit(self, node, scope):
        return not self.visit(node.expression, scope)

    @visitor.when(IfNode)
    def visit(self, node, scope):
        if self.visit(node.condition, scope):
            child_scope = scope.create_child_scope()
            for child in node.then:
                self.visit(child, child_scope)
        elif node.else_ is not None:
            for child in node.else_:
                self.visit(child, scope)

    @visitor.when(WhileNode)
    def visit(self, node, scope):
        child_scope = scope.create_child_scope()
        while self.visit(node.condition, scope):
            try:
                for child in node.body:
                    self.visit(child, child_scope)
            except ContinueException:
                continue
            except BreakException:
                break

    @visitor.when(ForNode)
    def visit(self, node, scope):
        child_scope = scope.create_child_scope()
        self.visit(node.start, child_scope)
        while self.visit(node.condition, child_scope):
            try:
                for child in node.body:
                    self.visit(child, child_scope)
            except ContinueException:
                continue
            except BreakException:
                break
            finally:
                self.visit(node.increment, child_scope)

    @visitor.when(ReturnNode)
    def visit(self, node, scope):
        value = self.visit(node.expression, scope)
        raise ReturnException(value)

    @visitor.when(BreakNode)
    def visit(self, node, scope):
        raise BreakException()

    @visitor.when(ContinueNode)
    def visit(self, node, scope):
        raise ContinueException()

    @visitor.when(SimulatorNode)
    def visit(self, node, scope):
        self.simulator = Simulator(node.mode(), node.max_turns)

    @visitor.when(UnitNode)
    def visit(self, node, scope):
        self.units = [] if self.units is None else self.units
        if self.simulator is not None:
            self.simulator.units(node.unit, int(node.number), node.team, node.behavior)
            for unit in self.simulator.unit():
                unit.strategy(node.behavior, node.strategy(unit))

    @visitor.when(FieldNode)
    def visit(self, node, scope):
        if self.simulator is not None:
            self.simulator.board(int(node.height), int(node.width))      

    @visitor.when(AllocateNode)
    def visit(self, node, scope):
        if self.simulator is not None:
            self.simulator.allocate_units(node.allocate, self.simulator.unit())

    @visitor.when(ExecuteSimulationNode)
    def visit(self, node, scope):
        if self.simulator is not None:
            self.simulator.execute()