def suma(x , y):
    ''' Realiza la suma de 2 parametros
        x(int/float): primer parametro
        y(int/float): segundo parametro
        regresa el valor de ambos  
    '''
    return x + y

def escribir(fpath , data_in):
    ''' 
    funcion que escribe en un archivo 
    Args:
    
    fpath: path absoluto del archivo
    data_in: información a escribir
    '''
    with open(fpath , "w") as file_in:
        file_in.write(data_in)
