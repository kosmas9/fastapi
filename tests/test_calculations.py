import pytest
from app.calculations import add

@pytest.mark.parametrize("num1 , num2 , res",[(3, 2, 5),(1,7,8),(12,4,16)])
def test_add(num1,num2,res):
    print("testing add function")
    assert add(num1,num2) == res

