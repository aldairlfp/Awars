import ply.lex as lex

literals = ['+', '-', '*', '/', '(', ')', '=', ';', ',', '{', '}', '[', ']', '<', '>', '&', '|', '!']

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'number': 'NUMBERTYPE',
    'string': 'STRING',
    'return': 'RETURN',
    'void': 'VOID',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'soldier': 'SOLDIER',
    'field': 'FIELD',
    'enemy': 'ENEMY',
    'obstacle': 'OBSTACLE',
    'default': 'DEFAULT',
    'print': 'PRINT',
}

tokens = [
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'NUMBER',
             'ID',
             'FUNCTION',
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
             'COMMENT',
             'STRING_LITERAL',
             'CHAR_LITERAL',
         ] + list(reserved.values())


def aw_lexer():
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
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
    t_STRING_LITERAL = r'\".*\"'
    t_CHAR_LITERAL = r'\'.\''

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'ID')
        return t

    def t_FUNCTION(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*\('
        t.type = reserved.get(t.value, 'FUNCTION')
        return t

    def t_NUMBER(t):
        r'\d+'
        t.value = float(t.value)
        return t

    def t_COMMENT(t):
        r'//.*'
        pass

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

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

    return lex.lex()
