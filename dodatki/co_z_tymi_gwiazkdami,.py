def foo(a, b, *args):
    print(f"a={a}")
    print(f"b={b}")
    print(f"args={args}")


foo(1, 2, 1, 2, 3)

lista = [1, 2, 3]
foo(1, 2, *lista)  # foo(1, 2, 1, 2, 3)

a, *_, c = 1, 2, 1, 2, 3

print("a=", a)
print("_=", _)
print("c=", c)

def bar(a=1, b=2, **kwargs):
    print("a=", a)
    print("b=", b)
    print("kwargs=", kwargs)
    print("-"*40)


bar()
bar(2)
bar(2, 3)
bar(2, 3, d=4)

def baz(*args, **kwargs):
    print("args=", args)
    print("kwargs=", kwargs)
    print("-"*40)

    if kwargs.get("imie"):
        imie = kwargs.get("imie")
        print("hello", imie)

baz(1, 2, d=10, imie=44)


def xxx(a, b, *args, k=1, v=2, **kwargs):
    pass