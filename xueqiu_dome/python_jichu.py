



def tmp(func):
    def wrapper(*args,**kwargs):
        print('before')
        func(*args,**kwargs)
        print('after')
    return wrapper

@tmp
def a(a1,a2,a3,a4):
    print('a')
    print(a1,a2,a3,a4)


def test_a():
    a('b',1,2,3)
