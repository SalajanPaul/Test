# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def suma():
    print(f'introduceti primul numar, a')
    a = input()
    print("a=", a)
    print(f'introduceti al doilea numar, b')
    b = input()
    print("b=", b)
    print('a+b=' ,int(a)+int(b))


def scadere():
    print(f'prima cifra, a')
    a = input()
    print("a=", a)
    print(f'a doua cifra, b')
    b = input()
    print("b=", b)
    print ('a-b=' ,int(a)-int(b))

def inmultire():
    print(f'prima cifra, a')
    a = input()
    print("a=", a)
    print(f'a doua cifra, b')
    b = input()
    print("b=", b)
    print('a*b=' ,int(a)*int(b))

def ariaTD():
    print(f'prima cateta, (ab)')
    a = input()
    print("ab=", a)
    print(f'a doua cateta, (ac)')
    b = input()
    print("ac=", b)
    print('Aria triunghiului este' , int(a)*int(b)/2)












# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print('suma')
   suma()
   print('scadere')
   scadere()
   print('inmultire')
   inmultire()
   print('aria triunghiuui dreptunghic')
   ariaTD()




