import compiler.ply.yacc as yacc
from compiler.lexer import tokens
from compiler.aw_ast import *
from simulation.Units.unit_generator import *
from simulation.modes.modes import Normal_mode, Hard_mode
from algoritms.strategies.strategies import *
from simulation.Units.units_allocator import random_allocator

units_generator = {
    'normal': normal_unit,
    'archer_b': archer_b_unit,
    'archer_c': archer_c_unit,
    'swordman': swordman_unit,
    'spearman': spearman_unit,
}

modes_generator = {
    'normal_mode': Normal_mode,
    'hard_mode': Hard_mode,
}

strategies_generator = {
    'hard_fuzzy_strategy': Hard_fuzzy_strategy,
    'hard_optimal_strategy': Hard_optimal_strategy,
    'random_strategy': Random_strategy,
    'greedy_strategy': Greedy_strategy,
    'runner_strategy': Runner_strategy,
    'attacker_strategy': Attacker_strategy,
    'normal_strategy': Normal_strategy,
    'advanced_strategy': Advanced_strategy,
}

allocate_generator = {
    'random_allocate': random_allocator,
}


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
        '''simulation_statement : simulator_property SIM_PROPERTY SIMULATOR
                                | simulator_statement
                                | allocate_statement
                                | SIMULATOR'''
        if p[1] == 'simulator':
            p[0] = ExecuteSimulationNode()
        else:
            p[0] = p[1]

    def p_simulator_statement(p):
        'simulator_statement : SIMULATOR LPAREN simulator_mode COMMA NUMBER RPAREN'
        p[0] = SimulatorNode(modes_generator[p[3]], p[5])

    def p_simulator_mode(p):
        '''simulator_mode : HARD_MODE
                          | NORMAL_MODE'''
        p[0] = p[1]

    def p_simulator_property(p):
        '''simulator_property : unit_property
                              | field_property'''
        p[0] = p[1]

    def p_unit_property(p):
        'unit_property : UNIT LPAREN type_unit COMMA NUMBER COMMA STRING COMMA behavior COMMA strategy RPAREN'
        p[0] = UnitNode(p[3], p[5], p[7][1:-1], p[9], p[11])

    def p_type_unit(p):
        '''type_unit : NORMAL_UNIT
                     | ARCHER_B_UNIT
                     | ARCHER_C_UNIT
                     | SWORDMAN_UNIT
                     | SPEARMAN_UNIT'''
        p[0] = units_generator[p[1]]

    def p_behavior(p):
        'behavior : HARD_BEHAVIOUR'
        p[0] = p[1]

    def p_strategy(p):
        '''strategy : RANDOM_STRATEGY
                    | GREEDY_STRATEGY
                    | RUNNER_STRATEGY
                    | ATTACKER_STRATEGY
                    | NORMAL_STRATEGY
                    | ADVANCED_STRATEGY
                    | HARD_OPTIMAL_STRATEGY
                    | HARD_FUZZY_STRATEGY
                    | RANDOM_ALLOCATE'''
        p[0] = strategies_generator[p[1]]

    def p_field_property(p):
        'field_property : FIELD LPAREN NUMBER COMMA NUMBER RPAREN'
        p[0] = FieldNode(p[3], p[5])

    def p_allocate_statement(p):
        'allocate_statement : RANDOM_ALLOCATE'
        p[0] = AllocateNode(allocate_generator[p[1]])

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
        'if_statement : IF LPAREN condition RPAREN LBRACE newline_or_empty all_statements_list RBRACE else_statement'
        p[0] = IfNode(p[3], p[7], p[9])

    def p_else_statement(p):
        'else_statement : ELSE LBRACE newline_or_empty all_statements_list RBRACE'
        p[0] = p[4]

    def p_else_statement_epsilon(p):
        'else_statement : epsilon'
        pass

    def p_while_statement(p):
        'while_statement : WHILE LPAREN condition RPAREN LBRACE newline_or_empty all_statements_list RBRACE'
        p[0] = WhileNode(p[3], p[7])

    def p_for_statement(p):
        'for_statement : FOR LPAREN assignment SEMI condition SEMI reassignment RPAREN LBRACE newline_or_empty all_statements_list RBRACE'
        p[0] = ForNode(p[3], p[5], p[7], p[11])

    def p_condition(p):
        '''condition : condition_c AND condition_c
                     | condition_c OR condition_c
                     | condition_c
                     | NOT condition_c
                       '''
        if len(p) == 3:
            p[0] = NotNode(p[2])
        elif len(p) == 4:
            if p[2] == '&&':
                p[0] = AndNode(p[1], p[3])
            else:
                p[0] = OrNode(p[1], p[3])
        else:
            p[0] = p[1]

    def p_condition_c(p):
        '''condition_c : expression EQ expression
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
