#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from builtins import list


def test(fun, *args):
    """
    Funkcja ta posłuży do testowania i wyświetlania informacji czy Twoja implementacja jest poprawna.
    :param fun: 
    :param args: 
    :return: 
    """
    print "".join(['-' for i in range(40)])
    print fun.__name__[:-1].upper()+" "+fun.__name__[-1]
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print "Yes, "+decoded.replace("my","your")
        else:
            print "No, "+decoded.replace("my","your").replace("has","has not")+" yet"
    else:
        print "Is correct? "+ str(res == args[-1])
    print "".join(['-' for i in range(40)])


print("Hello!")

def zadanie1(listObject):
    #  Zadaniem tej funkcji jest przetworzenie przekazanej listy (przekazana jako listObject)
    #  tak oby usunąć powtarzające się elementy ale tylko pomiędzy sąsiadami.
    for obj in listObject[:-1]:
        n = listObject.index(obj)
        if obj == listObject[n+1] :
            del listObject[n+1]
        #print(listObject)
    return listObject


moja_lista = [1, 2, 3, 3, 5, 68, 68, 24]
zadanie1(moja_lista)
print(moja_lista)

test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1, 2, 3, 5, 68, 24])


def zadanie2(list1, list2):
    """
    Funkcja ta powinna zwracać nową listę która jest sumą przekazanych list, 
    tak aby kolejne elementy nowej listy składały się naprzemiennie, raz element z jednej listy a raz z drugiej. 
    Uwaga, listy mogą nie być tej samej długości.
    """
    mixedList = list()


    return mixedList

#test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12,'c','5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])

# wektor vs lista?
