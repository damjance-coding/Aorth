import sys
file = sys.argv[1]
c =  open(f"{file[:1-3]}.c", "a")
c.write('''
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>       // for clock_t, clock(), CLOCKS_PER_SEC
#include <unistd.h>
#include <string.h>

''')

c.write('''




struct stack_entry {
  char *data;
  struct stack_entry *next;
};


struct stack_t
{
  struct stack_entry *head;
  size_t stackSize;  // not strictly necessary, but
                     // useful for logging
};


struct stack_t *newStack(void)
{
  struct stack_t *stack = malloc(sizeof *stack);
  if (stack)
  {
    stack->head = NULL;
    stack->stackSize = 0;
  }
  return stack;
}


char *copyString(char *str)
{
  char *tmp = malloc(strlen(str) + 1);
  if (tmp)
    strcpy(tmp, str);
  return tmp;
}


void push(struct stack_t *theStack, char *value)
{
  struct stack_entry *entry = malloc(sizeof *entry); 
  if (entry)
  {
    entry->data = copyString(value);
    entry->next = theStack->head;
    theStack->head = entry;
    theStack->stackSize++;
  }
  else
  {
    // handle error here
  }
}


char *strtop(struct stack_t *theStack)
{
  if (theStack && theStack->head)
    return theStack->head->data;
  else
    return NULL;
}


void pop(struct stack_t *theStack)
{
  if (theStack->head != NULL)
  {
    struct stack_entry *tmp = theStack->head;
    theStack->head = theStack->head->next;
    free(tmp->data);
    free(tmp);
    theStack->stackSize--;
  }
}

void clear (struct stack_t *theStack)
{
  while (theStack->head != NULL)
    pop(theStack);
}






// N will be the capacity of the Static Stack
#define N 1000

// Initializing the top of the stack to be -1
int top = 0;
int num;
int x;
int y;

char string[N];
// Initializing the stack using an array
int stack[N];

// Function prototypes


''')


c.write("int main(){ \n")
c.write('''
double time_spent = 0.0;
 
clock_t begin = clock();

struct stack_t *StringStack = newStack();
char *data;


''')    


def clear():
    c.write('''
    
while(top != 0){


top-=1;

}

    ''')

def cpush(i: int):
  c.write('''

// Checking overflow state
if(top == N-1){

printf("Overflow State: can't add more elements into the stack");

}


  
  ''')
  c.write('''
else{
        
       
''')
  c.write(f'''

top+=1;
stack[top] = {i};


''')

  c.write('''
} 
 ''')


def cpop():
    c.write(r'''


if(top == 0 || top == -1){
printf("Underflow State: Stack already empty, can't remove any element");
}
else{
int x = stack[top];
printf("%d \n", x);
top-=1;

}

    
    ''')



def cadd():
    c.write('''

if(top == N-1){
printf("Overflow State: can't add more elements into the stack");
}
else if(top == -1){
printf("Underflow State: Stack already empty, Or lacks one element");
}
else{
x = stack[top];
top-=1;
y = stack[top];
top-=1;


top += 1;
stack[top] = x + y;
}



    ''')

def csub():
    c.write('''

if(top == N-1){
printf("Overflow State: can't add more elements into the stack");
}
else if(top == -1){
printf("Underflow State: Stack already empty, Or lacks one element");
}
else{
x = stack[top];
top-=1;
y = stack[top];
top-=1;


top += 1;
stack[top] = y - x;

}

    ''')

def cdiv():
    c.write('''

if(top == N-1){
printf("Overflow State: can't add more elements into the stack");
}
else if(top == -1){
printf("Underflow State: Stack already empty, Or lacks one element");
}
else{
 
x = stack[top];
top-=1;
y = stack[top];
top-=1;


top += 1;
stack[top] = y / x;

}

    
    ''')

def cmul():
    c.write('''

if(top == N-1){
printf("Overflow State: can't add more elements into the stack");
}
else if(top == -1){
printf("Underflow State: Stack already empty, Or lacks one element");
}
else{

x = stack[top];
top-=1;
y = stack[top];
top-=1;


top += 1;
stack[top] = y * x;

}


    ''')
def cdupl():
    c.write('''

if(top == N-1){
printf("Overflow State: can't add more elements into the stack");
}
else if(top == -1){
printf("Underflow State: Stack already empty");
}
else{

x = stack[top];
top-=1;




}

    
 ''')

def cdrop():
     c.write('''

if(top == -1){
printf("Underflow State: Stack already empty");
}

else{





}

    
 ''')
def cswap():
    c.write('''

if(top == N-1){
printf("Overflow State: can't add more elements into the stack");
}

else{

x = stack[top];
top-=1;
y = stack[top];
top-=1;

top += 1;
stack[top] = x;
top += 1;
stack[top] = y;

}

    
 ''')





def strpush(i):
    c.write(f'''

push(StringStack, "{str(i)}");




    ''')


def strpop():
    c.write(r'''

data = strtop(StringStack);
printf("%s\n", data);
pop(StringStack);

    
''')

def strdrop():
    c.write('''
    
pop(StringStack);
    
    ''')

def strdupl():
    
    c.write(''' 

data = strtop(StringStack);
push(StringStack, data);    
    
''')

def strclear():
    c.write(''' 
 
clear(StringStack); 

    
''')

def take_string_input(msg):
    c.write(fr'''  
    

printf("{msg}");
scanf("%s",string);
push(StringStack, string);

''')

def take_int_inpt(msg):
    c.write(fr'''  
    
num;
printf("{msg}");
scanf("%d", &num);
top+=1;
stack[top] = num;

''')

def system_op(op):
    c.write(f'''
    
system("{op}");

    
    ''')
