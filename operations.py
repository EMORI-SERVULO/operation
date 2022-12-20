def zero(*x):
    return print(eval(f'0{x[0]}')) if x else 0
def one(*x):
    return print(eval(f'1{x[0]}')) if x else 1
def two(*x):
    return print(eval(f'2{x[0]}')) if x else 2
def three(*x):
    return print(eval(f'3{x[0]}')) if x else 3
def four(*x):
    return print(eval(f'4{x[0]}')) if x else 4  
def five(*x):
    return print(eval(f'5{x[0]}')) if x else 5
def six(*x):
    return print(eval(f'6{x[0]}')) if x else 6
def seven(*x):
    return print(eval(f'7{x[0]}')) if x else 7
def eight(*x):
    return print(eval(f'8{x[0]}')) if x else 8
def nine(*x):
    return print(int(eval(f'9{x[0]}'))) if x else 9
def plus(n):
    return f"+{n}"
def minus(n):
    return f"-{n}"
def times(n):
    return f"*{n}"
def divided_by(n):
    return f"/{n}"


four(times(five())) # imprime 20
one(plus(eight())) # imprime 9
seven(minus(three())) # imprime 4
nine(divided_by(three())) # imprime 3
