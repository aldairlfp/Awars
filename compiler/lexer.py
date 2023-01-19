import compiler.ply.lex as lex

literals = ['+', '-', '*', '/',
            '(', ')', '=', ';', ',', '{', '}', '[', ']', '<', '>', '&', '|', '!']

reserved = {
    'func': 'FUNCTION',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'var': 'VAR',
    'return': 'RETURN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'print': 'PRINT',
    'simulator': 'SIMULATOR',
    'hard_mode': 'HARD_MODE',
    'units': 'UNITS',
    'unit': 'UNIT',
    'normal': 'NORMAL_UNIT',
    'archer_b': 'ARCHER_B_UNIT',
    'archer_c': 'ARCHER_C_UNIT',
    'swordman': 'SWORDMAN_UNIT',
    'spearman': 'SPEARMAN_UNIT',
    'hard': 'HARD_BEHAVIOUR',
    'random_strategy': 'RANDOM_STRATEGY',
    'greedy_strategy': 'GREEDY_STRATEGY',
    'runner_strategy': 'RUNNER_STRATEGY',
    'attacker_strategy': 'ATTACKER_STRATEGY',
    'normal_strategy': 'NORMAL_STRATEGY',
    'advanced_strategy': 'ADVANCED_STRATEGY',
    'hard_optimal_strategy': 'HARD_OPTIMAL_STRATEGY',
    'hard_fuzzy_strategy': 'HARD_FUZZY_STRATEGY',
}

tokens = [
    'PLUS',
    'MINUS',
    'STAR',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'ID',
    'ASSIGN',
    'SEMI',
    'COMMA',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'LT',
    'GT',
    'LTE',
    'GTE',
    'EQ',
    'NEQ',
    'AND',
    'OR',
    'NOT',
    'INC',
    'DEC',
    'COMMENT',
    'STRING',
    'newline',
] + list(reserved.values())


def aw_lexer():
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_STAR = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_ASSIGN = r'='
    t_SEMI = r';'
    t_COMMA = r','
    t_LBRACE = r'{'
    t_RBRACE = r'}'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LT = r'<'
    t_GT = r'>'
    t_LTE = r'<='
    t_GTE = r'>='
    t_EQ = r'=='
    t_NEQ = r'!='
    t_AND = r'&&'
    t_OR = r'\|\|'
    t_NOT = r'!'
    t_INC = r'\+\+'
    t_DEC = r'--'

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'ID')
        return t

    def t_NUMBER(t):
        r'\d+'
        t.value = float(t.value)
        return t

    def t_STRING(t):
        r'\"[^\"]*\"'
        return t

    def t_COMMENT(t):
        r'//.*'
        pass

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def find_column(input, token):
        """
        Compute the column.
        @param input: the input text string
        @param token: a token instance
        @return: the column number
        """
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    t_ignore = ' \t'

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def t_eof(t):
        return None

    return lex.lex(debug=True)
