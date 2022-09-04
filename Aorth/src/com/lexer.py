from sly import Lexer

class MyLexer(Lexer):
    tokens = {PRINT, STRING, NUMBER, PUSH, POP, ADD, SUB, MUL, DIV , DUPL, IF, DROP, SWAP, EQEQ, CLEAR, THEN , PASS, ELSE, FUN, START , END, FUNCNAME, CALL, FOR, ITEM, IN, STACK, PUSHSTR, POPSTR, DROPSTR, WHILE, TRUE, DUPLSTR, GETINPUT , NUM , STR, CLEARSTR, STHAN, GTHAN, SYSTEM} 
    ignore = ' \t'
    
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'
    
    literals = {">" "<", "(", ")"} 
    
    PRINT = r'print'
    PUSH = r'push'
    POP = r'pop'
    ADD = r'add'
    SUB = r'sub'
    MUL = r'mul'
    DUPL = r'dupl'
    DIV = r'div'
    IF = r"if"
    DROP = r'drop'
    SWAP = r'swap'
    EQEQ = r'=='
    THEN = r"then"
  
    PASS = r"pass"
    FUN= r"fun"
    ELSE = r"else"
    START = r"start"
    END = r"end"
    CALL = r"call"
    CLEAR = r"clear"
    FUNCNAME = r'\<.*?\>'
    
    FOR  = r"for"
    IN = r"in"
    STACK = r"stack"
    ITEM = r"item"

    PUSHSTR = r"strpush"
    POPSTR = r"strpop"
    DROPSTR = r"strdrop"
    
    DUPLSTR = r"strdupl"
    CLEARSTR = r"strclear"


    GETINPUT =  r"getinput"
    NUM = r"num"
    STR = r"str"
    STHAN = r"<"
    GTHAN = r">"
    
    WHILE = r"while"
    TRUE = r"True"
    SYSTEM = r"system"

    @_(r'\d+') 
    def NUMBER(self, t): 
        
        # convert it into a python integer 
        t.value = int(t.value) 
        return t  

    @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')
    def STRING(self, t):
        t.value = self.remove_quotes(t.value)
        return t

    # Notice Identifier comes after string because most words in a string would be matched with the identifier pattern
   

    def remove_quotes(self, text: str):
        if text.startswith('\"') or text.startswith('\''):
            return text[1:-1]
        return text