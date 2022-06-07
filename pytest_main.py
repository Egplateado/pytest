import pytest
from main import suma

def test_suma():
    assert suma(4 , 4) == 8
''' Creamos las tuplas a probar usando el decorater '''
@pytest.mark.parametrize(
    "input_a ,input_b , expected",
    [
        (3 , 2 , 5),
        (2 , 3 , 5),
        (suma(3 , 2) , 5 , 10),
        (3 , suma(2 , 5) , 1)
    ]
)     

def test_suma_multi(input_a , input_b , expected):
    assert suma(input_a , input_b) == expected