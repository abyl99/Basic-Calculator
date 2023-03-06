#Basic calculator
    
def addition(x, y):
    '''This function adds two parameters, x & y'''
    return x+y
        
def subraction(x,y):
    '''This function subtracts two parameters, x & y'''
    return x-y

def multiplication(x,y):
    '''This function multiplies two parameters, x & y'''
    return x*y


print('Select operation')
print('For addition, write a')
print('For subtraction, write s')
print('For multiplication, write m')
print()

while True: 
    #Player is asked to enter a choice
    
    choice = input('Enter choice:')
    
    print()
    
    #Check if option is a,s or m
    if choice in ('a', 's', 'm'):
        
        #x is the first number entered
        x = int(input('Enter first number: '))
        
        #y is the second number entered
        y = int(input('Enter second number: '))
        
        #Check if choice is a
        if choice == 'a':
            #Printing the function addition of x and y
            print(x, '+', y, '=', addition(x,y))
            
        #Check if choice is s
        elif choice == 's':
            
            #Printing the function subtraction of x and y
            print(x, '-', y, '=', subraction(x,y))
           
          #Check if choice is m
        elif choice == 'm':
            
             #Printing the function multiplicatoin of x and y
            print(x, '*', y, '=', multiplication(x,y))
            
    #Check if choice is other than a,s or m
    else:
        print('Invalid entry. Try again')
