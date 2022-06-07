from main import suma

class calculadora():
    
    def sumar(x , y):
        ''' 
        Funcion que toma dos parametros y devuelve la suma
        
        args: 
        
        x(int/float): primer valor a sumar
        y(int/float): segundo valor a sumar
        
        return: suma(x , y)
        '''
        return suma(x , y)

def test_class_monkey(monkeypatch):
    monkeypatch.setattr(calculadora , "sumar" , lambda x: 4)
    c = calculadora()
    assert c.sumar() == 4
