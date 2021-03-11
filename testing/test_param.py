import pytest
@pytest.mark.parametrize('c',[1,2,3])
@pytest.mark.parametrize('a',[4,5,6])
@pytest.mark.parametrize('b',[7,8,9])
def test_parm(a,b,c):
    print(a,b,c)