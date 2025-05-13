from notebook_es import Nota

n1= Nota('hello first')
n2 = Nota('hello again')
print(n1.id)
print(n2.id)
print(n1.match('hello'))
print(n2.match('second'))