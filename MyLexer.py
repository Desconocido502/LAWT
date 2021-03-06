from ply_3_11.ply.lex import lex

# * Ejemplo tomado de la documentacion oficial de https://www.dabeaz.com/ply/ply.html


class MyLexer():

    # * List of token names.   This is always required
    tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
    )

    # * Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex(module=self, **kwargs)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    def getTokens(self, data):
        lts = []
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            lts.append(tok)
        return lts


def recorrerTokens(ltsTokens):
    for token in ltsTokens:
        print("Tipo de token: "+token.type, ", Lexema:"+ str(token.value),", Linea:"+str(token.lineno), ", Columna:"+str(token.lexpos))


data = "3 + 4 * (5 - 6)"
# * Build the lexer and try it out

m = MyLexer()
m.build()  # * Build the lexer
print("Expresion a evaluar: " + data+"\n")
#m.test(data)  
# *Test it
#print("\n----------\n")
recorrerTokens(m.getTokens(data))
