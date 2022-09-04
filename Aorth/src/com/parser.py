
from lexer import MyLexer
from sly import Parser


class MyParser(Parser):

   
    tokens = MyLexer.tokens

    @_('')
    def statement(self, p):
        pass
    
    @_("PASS")
    def statement(self, p):
        return ("pass", )
    #CONDITIONS
    @_("NUMBER EQEQ NUMBER")
    def condintion(self, p):
        
        return ("coneqeq", p.NUMBER0, p.NUMBER1,)
    
    @_('NUMBER GTHAN NUMBER')
    def condintion(self, p):
        return ("condition_gd", p.NUMBER0, p.NUMBER1)
    
    @_('NUMBER STHAN NUMBER')
    def condintion(self, p):
        return ("condition_sd", p.NUMBER0, p.NUMBER1)


    @_("POP EQEQ NUMBER") 
    def condintion(self, p):
        return ("condition_pop_eqeq_num", p.POP, p.NUMBER)

    @_("NUMBER EQEQ POP")
    def condintion(self, p):
        return ("condition_num_eq_pop", p.NUMBER, p.POP) 
    @_('POP GTHAN NUMBER')
    def condintion(self, p):
        return ("condition_pop_gd_num", p.POP, p.NUMBER)
    @_('NUMBER GTHAN POP')
    def condintion(self, p):
        return ("condition_num_gd_pop", p.NUMBER, p.POP)
    @_('NUMBER STHAN POP')
    def condintion(self, p):
        return ("condition_num_sd_pop", p.NUMBER, p.POP)
    @_('POP STHAN NUMBER')
    def condintion(self, p):
        return ("condition_pop_sd_num", p.POP, p.NUMBER)
    @_("STRING EQEQ STRING")
    def condintion(self, p):
        return ("con_str_eq_str", p.STRING0, p.STRING1)
    
    
    @_("POPSTR EQEQ STRING")
    def condintion(self, p):
        return ("con_strpop_eq_str", p.POPSTR, p.STRING)
    

    @_("STRING EQEQ POPSTR")
    def condintion(self, p):
        return ("con_str_eq_popstr", p.POPSTR, p.STRING)

    @_("IF condintion THEN statement ELSE statement")
    def statement(self, p):
        return ("ifst", p.condintion, p.statement0 , p.statement1)
        
        
    @_('FUN FUNCNAME "(" ")" START statement  END')
    def statement(self, p):
        print("test")
        return ("fun_def", p.FUNCNAME, p.statement )

    @_('CALL FUNCNAME ')
    def statement(self, p):
        return ("fun_call" , p.FUNCNAME)


    
    @_("FOR ITEM IN STACK START statement END")
    def statement(self, p):
        
        return ("stack_for_loop",  p.statement)

    @_("PUSH NUMBER")
    def statement(self, p):
        
        return ("push", p.NUMBER)

    @_("POP")
    def statement(self, p):
        
        return ("pop", )
        
    @_("SUB")
    def statement(self, p):
       
        return ("pop", )
    @_("PRINT STRING")
    def statement(self, p):
        
        
        return ("print", p.STRING)

    @_("ADD")
    def statement(self, p):
        
       
        return ("add", )
    @_("DIV")
    def statement(self, p):
     
        
        return ("div", )
    @_("MUL")
    def statement(self, p):
    
        
        return ("mul", )
    @_("DUPL")
    def statement(self , p):
         
         
         return ("dupl", )
    @_("DROP")
    def statement(self, p):
        
        return ("drop", )
    @_("SWAP")
    def statement(self, p):
        
        return ("swap", )

    @_("CLEAR")
    def statement(self, p):
        return ("clear", )
    @_("PUSHSTR STRING")
    def statement(self, p):
    
        return ("pushstr", p.STRING)
    
    @_("POPSTR")
    def statement(self, p):
        return ("popstr", )

    @_("DROPSTR")
    def statement(self, p):
        return ("dropstr", ) 

    
    # @_("SWAPSTR")
    # def statement(self, p):
    #     return ("swapstr", )

    @_("DUPLSTR")
    def statement (self, p):
        return ("strdupl", )
    
    @_("WHILE TRUE START statement END")
    def statement (self, p):
        return ("while_inf_loop", p.statement)

    @_("CLEARSTR")
    def statement (self, p):
        return ("clearstr", )

    @_("GETINPUT STR STRING")
    def statement (self, p):
        return ("getinput_str", p.STRING)
    
    @_("GETINPUT NUM STRING")
    def statement (self, p):
        return ("getinput_int", p.STRING)

    @_("SYSTEM STRING")
    def statement (self, p):
        return ("system_op", p.STRING)


 