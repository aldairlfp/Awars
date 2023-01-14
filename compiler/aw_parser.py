import ply.yacc as yacc
from lexer import tokens
from aw_ast import (ProgramNode, PrintNode, StatementNode, VarDeclarationNode, FunctionDeclarationNode, PlusNode,
                          MinusNode, StarNode, DivNode, ConstantNumNode, IfNode, WhileNode)


def aw_parser():
    def p_program(p):
        'program : maybe_newline statement_list'
        p[0] = ProgramNode(p[2])

    def p_epsilon(p):
        'epsilon :'
        pass

    def p_maybe_newline(p):
        "maybe_newline : newline"
        p[0] = p[1]

    def p_maybe_epsilon(p):
        "maybe_newline : epsilon"
        pass

    def p_statement_list(p):
        'statement_list : statement newline maybe_newline statement_list'
        p[0] = [p[1], *p[4]]

    def p_statement_list_epsilon(p):
        'statement_list : epsilon'
        p[0] = []

    def p_statement(p):
        '''statement : assignment
                     | function
                     | expression
                     | if_statement
                     | while_statement
                     '''
        p[0] = p[1]

    def p_assignment(p):
        'assignment : NUMBERTYPE ID ASSIGN expression'
        p[0] = VarDeclarationNode(p[2], p[4])

    def p_function(p):
        'function : FUNCTION ID LPAREN params RPAREN LBRACE statement_list RBRACE'
        p[0] = FunctionDeclarationNode(p[2], p[4], p[7])

    def p_params(p):
        '''params : param COMMA params
                  | param'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1], *p[3]]

    def p_param(p):
        'param : NUMBERTYPE ID'
        p[0] = p[2]

    def p_if_statement(p):
        'if_statement : IF LPAREN expression RPAREN LBRACE maybe_newline statement_list RBRACE'
        p[0] = IfNode(p[3], p[7], [])

    def p_while_statement(p):
        'while_statement : WHILE LPAREN expression RPAREN LBRACE maybe_newline statement_list RBRACE'
        p[0] = WhileNode(p[3], p[7])

    def p_expression(p):
        '''expression : expression PLUS term
                      | expression MINUS term
                      | term'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            if p[2] == '+':
                p[0] = PlusNode(p[1], p[3])
            else:
                p[0] = MinusNode(p[1], p[3])

    def p_term(p):
        '''term : term STAR factor
                | term DIVIDE factor
                | factor'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            if p[2] == '*':
                p[0] = StarNode(p[1], p[3])
            else:
                p[0] = DivNode(p[1], p[3])

    def p_factor(p):
        '''factor : NUMBER
                  | LPAREN expression RPAREN'''
        if len(p) == 2:
            p[0] = ConstantNumNode(p[1])
        else:
            p[0] = p[2]

    def p_error(p):
        print("Syntax error in input!")

    return yacc.yacc()
