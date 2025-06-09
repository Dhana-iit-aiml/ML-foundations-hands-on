
# any value inside a function is its local fun-> parent func scope (if nonlocal used) --> searches for global

a =2

def f():

    a =  6
    def f1():
        # note nonlocal is for inner function to use/modify the scope on parent function scope
        nonlocal a
        a = a +10
        print(f'value of a = {a} from f1() from inner func() ')
    f1()
    print(f'value of a = {a} from f() - parent func')

f()
print(f'value of a = {a} from f() - outside  -global scope')
