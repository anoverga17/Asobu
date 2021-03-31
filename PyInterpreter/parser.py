# -----------------------------------------------------------------------------
# Built from calc.py starter code provided in the sly documentation
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, '../..')

from sly import Lexer, Parser
from abs_syn_tree import *

class CalcLexer(Lexer):
    tokens = { ID, NUMBER, PLUS, TIMES, MINUS, DIVIDE, LAMBDA,
               LPAREN, RPAREN, LBRACK, RBRACK, FEED}
    ignore = ' \t'

    # Tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['lambda'] = LAMBDA
    NUMBER = r'\d+'

    # Special symbols
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACK = r'\{'
    RBRACK = r'\}'
    FEED = r'\<\<'


    # Ignored pattern
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print(f"Illegal character {t.value}")
        self.index += 1

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('left', FEED),
        ('right', UMINUS)
        )

    @_('expr')
    def statement(self, p):
        print(p.expr.eval({}))

    @_('LAMBDA LPAREN ID RPAREN LBRACK expr RBRACK')
    def expr(self, p):
        return Lambda(p.ID, p.expr)

    @_('expr FEED expr')
    def expr(self, p):
        return Apply(p.expr0, p.expr1)

    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr')
    def expr(self, p):
        return Builtin(p[1], [p.expr0, p.expr1])

    @_('MINUS NUMBER %prec UMINUS')
    def expr(self, p):
        return Literal(Value(-1*float(p.NUMBER)))

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return Literal(Value(float(p.NUMBER)))

    @_('ID')
    def expr(self, p):
        return Id(p.ID)
