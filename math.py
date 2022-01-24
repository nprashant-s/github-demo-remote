#add implimentation
def add(x,y):
    return x+y
    
#subtract implimentation 
def subtract(x,y):
    return x-y          #on master branch
        
def multiply(x,y):
    return x*y          #on bug456 branch

def divide(x,y):
    if y ==0:                       #on master branch
            return DIVIDE_BY_0_ERROR
    else:
        return x/y
    
