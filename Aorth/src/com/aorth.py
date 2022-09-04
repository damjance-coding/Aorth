from lexer import MyLexer
import os
import sys
import c
file = sys.argv[1]
from parser import MyParser
from exec import Execute



def com():
   parser = MyParser()
   lexer = MyLexer()
   env = {}
   with open(sys.argv[1], "r") as f:
    lines = [line.strip() for line in f]
   for line in lines:
    p = line.strip()
    
    tree = parser.parse(lexer.tokenize(p))
    
    if tree != None: Execute(tree, env)
   c.c.write('''

 
 
clock_t end = clock();
 
// calculate elapsed time by finding difference (end - begin) and
    // dividing the difference by CLOCKS_PER_SEC to convert to seconds
time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
 
printf("-----%f seconds----", time_spent);
   ''')
   c.c.write('''return 0;\n}''')
   c.c.close()
   
   os.system(f"gcc {file[:1-3]}.c -o {file[:1-3]}.o")
   os.remove(f"{file[:1-3]}.c")
   
   

   
com()   