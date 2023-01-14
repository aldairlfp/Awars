import cmp.visitor as visitor
from context import Scope
from aw_ast import (ProgramNode, PrintNode, VarDeclarationNode, FunctionDeclarationNode, BinaryNode, AtomicNode,
                          CallNode, IfNode, ReturnNode, WhileNode, VariableNode, ConstantNumNode)


class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ProgramNode [<stat>; ... <stat>;]'
        statements = '\n'.join(self.visit(child, tabs + 1) for child in node.statements)
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
        ans = '\t' * tabs + f'\\__FuncDeclarationNode: func {node.id}({params}) <statement_list>'
        body = self.visit(node.body, tabs + 1)
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
            else_ = '\n'.join(self.visit(child, tabs + 1) for child in node.else_)
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


class SemanticCheckerVisitor(object):
    def __init__(self):
        self.errors = []

    @visitor.on('node')
    def visit(self, node, scope):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        if scope is None:
            scope = Scope()
        for child in node.statements:
            self.visit(child, scope)
        return self.errors

    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):
        if scope.is_var_defined(node.id):
            self.errors.append(f'Variable {node.id} already declared')
        else:
            self.visit(node.expression, scope)
            scope.define_variable(node.id)

    @visitor.when(FunctionDeclarationNode)
    def visit(self, node, scope):
        if scope.is_func_defined(node.id):
            self.errors.append(f'Function {node.id} already declared')
        else:
            self.visit(node.body, scope)
            scope.define_function(node.id, node.params)

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
        if not scope.is_func_defined(node.lex):
            self.errors.append(f'Function {node.lex} not declared')
        else:
            for arg in node.args:
                self.visit(arg, scope)

    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        self.visit(node.right, scope)

    @visitor.when(IfNode)
    def visit(self, node, scope):
        self.visit(node.condition, scope)
        child_scope = scope.create_child_scope()
        for child in node.then:
            self.visit(child, child_scope)
        if node.else_ is not None:
            for child in node.else_:
                self.visit(child, scope)

    @visitor.when(WhileNode)
    def visit(self, node, scope):
        self.visit(node.condition, scope)
        child_scope = scope.create_child_scope()
        for child in node.body:
            self.visit(child, child_scope)

class EvaluatorVisitor(object):
    def __init__(self):
        self.errors = []
        self.functions = {}

    @visitor.on('node')
    def visit(self, node, scope):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        if scope is None:
            scope = Scope()
        for child in node.statements:
            self.visit(child, scope)
        return self.errors

    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):
        result = self.visit(node.expression, scope)
        scope.define_variable(node.id, result, node.reassignament)

    @visitor.when(FunctionDeclarationNode)
    def visit(self, node, scope):
        scope.define_function(node.id, node.params)
        self.functions[node.id] = node

    @visitor.when(PrintNode)
    def visit(self, node, scope):
        print(self.visit(node.expression, scope))

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        return node.lex

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        return scope.get_variable(node.lex).value

    @visitor.when(CallNode)
    def visit(self, node, scope):
        func = self.functions[node.lex]
        child_scope = scope.create_child_scope()
        for param, arg in zip(func.params, node.args):
            child_scope.define_variable(param, self.visit(arg, scope))
        for child in func.body:
            self.visit(child, child_scope)

    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        left = self.visit(node.left, scope)
        right = self.visit(node.right, scope)
        return node.operate(left, right)

    @visitor.when(IfNode)
    def visit(self, node, scope):
        if self.visit(node.condition, scope) == 0:
            child_scope = scope.create_child_scope()
            for child in node.then:
                self.visit(child, child_scope)
        elif node.else_ is not None:
            for child in node.else_:
                self.visit(child, scope)

    @visitor.when(WhileNode)
    def visit(self, node, scope):
        while self.visit(node.condition, scope) == 0:
            child_scope = scope.create_child_scope()
            for child in node.body:
                self.visit(child, child_scope)

    @visitor.when(ReturnNode)
    def visit(self, node, scope):
        return self.visit(node.expression, scope)
