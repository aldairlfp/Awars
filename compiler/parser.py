import ply.yacc as yacc
from lexer import tokens
from compiler.ast import (ProgramNode, PrintNode, StatementNode, VarDeclarationNode, FunctionDeclarationNode, PlusNode,
    MinusNode, StarNode, DivNode, ConstantNumNode)


def aw_parser():
    def p_program(p):
        'program : function'
        p[0] = p[1]

    def p_epsilon(p):
        'epsilon :'
        pass

    def p_statement_list(p):
        '''statement_list : statement SEMI statement_list
                           | statement'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_statement(p):
        '''statement : assignment
                     | function
                     | expression'''
        p[0] = p[1]

    def p_statement_epsilon(p):
        'statement : epsilon'
        p[0] = []

    def p_semi(p):
        'semi : SEMI'
        pass

    def p_newline(p):
        'newline : NEWLINE'
        pass

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
            p[0] = [p[1]] + p[3]

    def p_param(p):
        'param : NUMBER ID'
        p[0] = p[1]

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
