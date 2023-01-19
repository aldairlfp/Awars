import ply.yacc as yacc
from lexer import tokens
from aw_ast import *


def aw_parser():
    def p_program(p):
        '''program : newline_or_empty all_statements_list'''
        p[0] = ProgramNode([], [], p[2])

    def p_epsilon(p):
        'epsilon :'
        pass

    def p_newline_or_empty(p):
        "newline_or_empty : newline newline_or_empty"
        p[0] = p[1]

    def p_newline_or_empty_epsilon(p):
        "newline_or_empty : epsilon"
        pass

    def p_all_statements_list(p):
        '''all_statements_list : statement newline newline_or_empty all_statements_list
                            |    simulation_statement newline newline_or_empty all_statements_list
                                '''
        p[0] = [p[1], *p[4]]

    def p_all_statements_list_epsilon(p):
        'all_statements_list : epsilon'
        p[0] = []

    def p_statement_list(p):
        'statement_list : statement newline newline_or_empty statement_list'
        p[0] = [p[1], *p[4]]

    def p_statement_list_epsilon(p):
        'statement_list : epsilon'
        p[0] = []

    def p_simulation_statement_list(p):
        'simulation_statement_list : simulation_statement newline newline_or_empty simulation_statement_list'
        p[0] = [p[1], *p[4]]

    def p_simulation_statement_list_epsilon(p):
        'simulation_statement_list : epsilon'
        p[0] = []

    def p_simulation_statement(p):
        '''simulation_statement : simulator_statement
                                | unit_statement'''
        p[0] = p[1]

    def p_simulator_statement(p):
        'simulator_statement : SIMULATOR LPAREN simulator_mode COMMA NUMBER RPAREN'
        p[0] = SimulatorNode(p[3], p[5])

    def p_simulator_mode(p):
        'simulator_mode : HARD_MODE'
        p[0] = p[1]

    def p_unit_statement(p):
        'unit_statement : type_unit LPAREN NUMBER COMMA STRING COMMA behavior RPAREN'
        p[0] = p[1], p[3], p[5], p[7]

    def p_type_unit(p):
        '''type_unit : NORMAL_UNIT
                     | ARCHER_B_UNIT'''
        p[0] = p[1]

    def p_behavior(p):
        'behavior : HARD_BEHAVIOUR'
        p[0] = p[1]

    def p_statement(p):
        '''statement : assignment
                     | reassignment
                     | print_statement
                     | function_statement
                     | expression
                     | if_statement
                     | while_statement
                     | for_statement
                     | break_statement
                     | continue_statement
                     | return_statement
                     '''
        p[0] = p[1]

    def p_assignment(p):
        'assignment : VAR ID ASSIGN expression'
        p[0] = VarDeclarationNode(p[2], p[4])

    def p_reassignment(p):
        '''reassignment : ID ASSIGN expression
                       | ID INC
                       | ID DEC
                       '''
        if p[2] == '=':
            p[0] = VarDeclarationNode(p[1], p[3], True)
        elif p[2] == '++':
            p[0] = VarDeclarationNode(p[1], PlusNode(
                VariableNode(p[1]), ConstantNumNode(1)), True)
        elif p[2] == '--':
            p[0] = VarDeclarationNode(p[1], MinusNode(
                VariableNode(p[1]), ConstantNumNode(1)), True)

    def p_print_statement(p):
        'print_statement : PRINT LPAREN expression RPAREN'
        p[0] = PrintNode(p[3])

    def p_function_statement(p):
        'function_statement : FUNCTION ID LPAREN params RPAREN LBRACE newline newline_or_empty statement_list RBRACE'
        p[0] = FunctionDeclarationNode(p[2], p[4], p[9])

    def p_params(p):
        '''params : param COMMA params
                  | param
                  | epsilon'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1], *p[3]]

    def p_param(p):
        'param : ID'
        p[0] = p[1]

    def p_if_statement(p):
        'if_statement : IF LPAREN condition RPAREN LBRACE newline_or_empty statement_list RBRACE else_statement'
        p[0] = IfNode(p[3], p[7], p[9])

    def p_else_statement(p):
        'else_statement : ELSE LBRACE newline_or_empty statement_list RBRACE'
        p[0] = p[4]

    def p_else_statement_epsilon(p):
        'else_statement : epsilon'
        pass

    def p_while_statement(p):
        'while_statement : WHILE LPAREN condition RPAREN LBRACE newline_or_empty statement_list RBRACE'
        p[0] = WhileNode(p[3], p[7])

    def p_for_statement(p):
        'for_statement : FOR LPAREN assignment SEMI condition SEMI reassignment RPAREN LBRACE newline_or_empty statement_list RBRACE'
        p[0] = ForNode(p[3], p[5], p[7], p[11])

    def p_condition(p):
        '''condition : expression EQ expression
                     | expression NEQ expression
                     | expression LT expression
                     | expression GT expression
                     | expression LTE expression
                     | expression GTE expression
                     '''
        if p[2] == '==':
            p[0] = EqualsNode(p[1], p[3])
        elif p[2] == '!=':
            p[0] = NotEqualsNode(p[1], p[3])
        elif p[2] == '<':
            p[0] = LessThanNode(p[1], p[3])
        elif p[2] == '>':
            p[0] = GreaterThanNode(p[1], p[3])
        elif p[2] == '<=':
            p[0] = LessThanEqualsNode(p[1], p[3])
        elif p[2] == '>=':
            p[0] = GreaterThanEqualsNode(p[1], p[3])

    def p_break_statement(p):
        'break_statement : BREAK'
        p[0] = BreakNode()

    def p_continue_statement(p):
        'continue_statement : CONTINUE'
        p[0] = ContinueNode()

    def p_return_statement(p):
        'return_statement : RETURN expression'
        p[0] = ReturnNode(p[2])

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
                  | STRING
                  | LPAREN expression RPAREN
                  | ID LPAREN args RPAREN
                  | ID LPAREN RPAREN
                  | ID'''
        if len(p) == 2:
            if isinstance(p[1], float):
                p[0] = ConstantNumNode(p[1])
            elif isinstance(p[1], str) and p[1][0] == '"' and p[1][-1] == '"':
                p[0] = ConstantStringNode(p[1][1:-1])
            else:
                p[0] = VariableNode(p[1])
        elif p[2] == '(':
            if len(p) == 5:
                p[0] = CallNode(p[1], p[3])
            else:
                p[0] = CallNode(p[1], [])
        else:
            p[0] = p[2]

    def p_args(p):
        '''args : arg COMMA args
                | arg'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1], *p[3]]

    def p_arg(p):
        'arg : expression'
        p[0] = p[1]

    def p_error(p):
        print("Syntax error in input!")

    return yacc.yacc()
