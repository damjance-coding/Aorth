import c
stack = [0, ]
stringstack = ["Default value", ]
class Execute:
    def __init__(self, tree, env):
        
        self.env = env
        result = self.walkTree(tree)
        
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)
        
    def walkTree(self, node): 
      
      if node[0] == "print":
         c.c.write(fr'''
printf("{node[1]}\n");
''')
      
      if node[0] == "push":
         
        
        
         c.cpush(node[1])

      if node[0] == 'ifst':
            con = node[1] ##condiiton
            
            if con[0] == "condition_sd":
               c.c.write(f'''

if({con[1]} < {con[2]})        
               
''')
               c.c.write('''
{
''')
               self.walkTree(node[2])

               c.c.write(''' 
               
}            
   ''')

               c.c.write(''' 
else{

               
''')          
               self.walkTree(node[3])


               c.c.write('''
       
 }              
               
               ''')


            if con[0] == "condition_gd":
               c.c.write(f'''

if({con[1]} > {con[2]})        
               
''')
               c.c.write('''
{
''')
               self.walkTree(node[2])

               c.c.write(''' 
               
}            
   ''')

               c.c.write(''' 
else{

               
''')          
               self.walkTree(node[3])


               c.c.write('''
       
 }              
               
               ''')

            if con[0] == "coneqeq":
               c.c.write(f'''
               
if({con[1]} == {con[2]})
               
               ''') 
               c.c.write('''
               
{ ''')
               self.walkTree(node[2])
               c.c.write('''

}''')
               c.c.write(''' 
               
else{
               
               ''')

               self.walkTree(node[3])

               c.c.write('''

}''')
            
            if con[0] == "condition_pop_eqeq_num":
               c.c.write(f''' 
               
int x = stack[top];

if(x == {con[2]})
               
               ''')
               c.c.write('''
{              
top -= 1;


               ''')

               self.walkTree(node[2])

               c.c.write('''

}''')
               c.c.write(''' 
               
else{
top -= 1;              
               ''')

               self.walkTree(node[3])

               c.c.write('''

}''')


            if con[0] == "condition_pop_gd_num":
               c.c.write(f''' 
               
int x = stack[top];

if (x > {con[2]})
               
               ''')

               c.c.write('''
{              
top -= 1;


               ''')

               self.walkTree(node[2])

               c.c.write('''

}''')
               c.c.write(''' 
               
else{
top -= 1;              
               ''')

               self.walkTree(node[3])

               c.c.write('''
}
''')

            if con[0] == "condition_pop_sd_num":
               c.c.write(f''' 
               
int x = stack[top];

if (x < {con[2]})
               
               ''')

               c.c.write('''
{              
top -= 1;


               ''')

               self.walkTree(node[2])

               c.c.write('''

}''')
               c.c.write(''' 
               
else{
top -= 1;            
               ''')

               self.walkTree(node[3])

               c.c.write('''
}
''')
            
            if con[0] == "condition_num_gd_pop":

               c.c.write(f''' 
               
int x = stack[top];

if ({con[1]} > x)
               
               ''')

               c.c.write('''
{              
top -= 1;


               ''')

               self.walkTree(node[2])

               c.c.write('''

}''')
               c.c.write(''' 
               
else{
top -= 1;             
               ''')

               self.walkTree(node[3])

               c.c.write('''
}
''')

            if con[0] == "condition_num_sd_pop":
               
               c.c.write(f''' 
               
int x = stack[top];

if ({con[1]} < x)
               
               ''')

               c.c.write('''
{              
top -= 1;


               ''')

               self.walkTree(node[2])

               c.c.write('''

}''')
               c.c.write(''' 
               
else{
top -= 1;             
               ''')

               self.walkTree(node[3])

               c.c.write('''
}
''')

            if con[0] == "condition_num_eq_pop":
               c.c.write(f''' 
               
int x = stack[top];

if({con[1]} == x)
               
               ''')
               c.c.write('''
{              
top -= 1;


               ''')

               self.walkTree(node[2])

               c.c.write('''

}''')
               c.c.write(''' 
               
else{
top -= 1;              
               ''')

               self.walkTree(node[3])

               c.c.write('''

}''')
            
            if con[0] == "con_str_eq_str":
               c.c.write(f''' 
               
               
if(strcmp("{con[1]}", "{con[2]}") == 0)               
               
''')
               c.c.write('''
{              



               ''')

               self.walkTree(node[2])

               c.c.write('''

}''')
               c.c.write(''' 
               
else{
               
               ''')

               self.walkTree(node[3])

               c.c.write('''

}''')


            if con[0] =="con_strpop_eq_str":
                 c.c.write(f'''

data = strtop(StringStack);
if(strcmp(data, "{con[2]}") == 0)



    
''')         
                 c.c.write('''
{                 
pop(StringStack);
                 
                 ''')
                 self.walkTree(node[2])

                 c.c.write('''

}''')
                 c.c.write(''' 
               
else{
pop(StringStack);              
               ''')

                 self.walkTree(node[3])

                 c.c.write('''

}''')

            if con[0] == "con_str_eq_popstr":
                 
                 c.c.write(f'''

data = strtop(StringStack);
if(strcmp(data, "{con[2]}") == 0)



    
''')         
                 c.c.write('''
{                 
pop(StringStack);
                 
                 ''')
                 self.walkTree(node[2])

                 c.c.write('''

}''')
                 c.c.write(''' 
               
else{
pop(StringStack);              
               ''')

                 self.walkTree(node[3])

                 c.c.write('''

}''')

      if node[0] == "fun_def":
         
         self.env[node[1]] = node[2]
     
      if node[0] == "fun_call":
          try: 
                 
                 self.walkTree(self.env[node[1]])
          except LookupError:
                print("Undefined function '%s'" % node[1])
                return 0

   
  
    

      if node[0] == "stack_for_loop":
         c.c.write('''
         
int x = top;         
while(x != 0){
x -= 1;


''')
         self.walkTree(node[1])

         c.c.write('''
         
}      
         
    ''')
      
      if node[0] == "clear":
         c.clear()
         
      if node[0] == "pop":
         
        
         c.cpop()
      if node[0] == "add":
        

         
         c.cadd()

      if node[0] == "sub":
   
         c.csub()
      if node[0] == "mul":
    
         c.cmul()
      if node[0] == "div":
        
    
         c.cdiv()
      if node[0] == "dupl":
      
         c.cdupl()
      if node[0] == "swap":
       
         c.cswap()
      if node[0] == "drop":
       
        c.cdrop()
      if node[0] == "pushstr":
         
         c.strpush(node[1])
      if node[0] == "popstr":
       
         c.strpop()
      if node[0] == "dropstr":
     
         c.strdrop()
     

      if node[0] == "strdupl":

         c.strdupl()

      if node[0] == "strclear":
         

         c.strclear()

      if node[0] == "getinput_str":
         c.take_string_input(node[1])

      if node[0] == "getinput_int":
         c.take_int_inpt(node[1])

      if node[0] == "while_inf_loop":
         c.c.write('''
         
while(1){
         
         ''')

         self.walkTree(node[1])

         c.c.write(''' 
         
}         
''')


      if node[0] == "system_op":
         c.system_op(node[1])
      
