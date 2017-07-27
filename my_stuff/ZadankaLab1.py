#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from builtins import list


def test(fun, *args):
    """
    Funkcja ta posłuży do testowania i wyświetlania informacji czy Twoja implementacja jest poprawna.
    :param fun: 
    :param args: 
    :return: 
    """
    print ("".join(['-' for i in range(40)]))
    print (fun.__name__[:-1].upper() + " " + fun.__name__[-1])
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print ("Yes, " + decoded.replace("my", "your"))
        else:
            print ("No, " + decoded.replace("my", "your").replace("has", "has not") + " yet")
    else:
        print ("Is correct? " + str(res == args[-1]))
    print ("".join(['-' for i in range(40)]))


print("Hello!")


def zadanie1(listObject):
    #  Zadaniem tej funkcji jest przetworzenie przekazanej listy (przekazana jako listObject)
    #  tak oby usunąć powtarzające się elementy ale tylko pomiędzy sąsiadami.
    for obj in listObject[:-1]:
        n = listObject.index(obj)
        if obj == listObject[n + 1]:
            del listObject[n + 1]
            # print(listObject)
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
    shorterLength = min(len(list1), len(list2))

    if len(list1) > len(list2):
        longerList = list1
    else:
        longerList = list2

    for l, r in zip(list1[:shorterLength], list2[:shorterLength]):
        mixedList.append(l)
        mixedList.append(r)

    for obj in longerList[shorterLength:]:
        mixedList.append(obj)

    return mixedList


output = zadanie2([1, 2, 19, 'dd', ':P', ":("], [12, 'c', '5'])

test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12, 'c', '5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])


# def zadanie3(listTuples):
#     """
#     Funkcja powinna zwracać posortowaną (listę) elementów typu [tuple].
#     Sortowanie wykonaj biorąc pod uwagę ostatni element każdego tuple.
#     :param listTuples:
#     :return:
#     """
#     sorted_list = list(listTuples)
#     isSwapped = True
#
#     while isSwapped: # bubble sort
#         isSwapped = False
#         for k in range(len(sorted_list)-1):
#             if sorted_list[k] > sorted_list[k + 1]:
#                 sorted_list[k], sorted_list[k + 1] = sorted_list[k + 1], sorted_list[k]
#                 isSwapped=True
#
#     return sorted_list
#
#
# posortowane = zadanie3([6,3,1,4,7,2])



def zadanie3(listOfTuples):
    """
    Funkcja powinna zwracać posortowaną [listę] elementów typu (tuple). 
    Sortowanie wykonaj biorąc pod uwagę ostatni element każdego tuple.
    :param listOfTuples: 
    :return: 
    """

    sorted_list = list(listOfTuples) #Q - is it the same: sorted_list = copy.deepcopy(listOfTuples) # make a deep copy
    isSwapped = True
    while isSwapped: # bubble sort
        isSwapped = False
        for k in range(len(sorted_list)-1):
            if sorted_list[k][-1] > sorted_list[k + 1][-1]:
                sorted_list[k], sorted_list[k + 1] = sorted_list[k + 1], sorted_list[k]
                isSwapped=True

    return sorted_list

#
# testListOfTuples = [(1, 3), (3, 3, 2), (2, 1)]
# posortowane3 = zadanie3a([(1, 3), (3, 3, 2), (2, 1)])

test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])



def zadanie4(text):
    """
    Zadaniem funkcji “zadanie4” jest odczytanie ukrytego zdania w poniższym tekście:
    “okmyaiaetiaigaafbaf??aaiaetiaigaafbaf??aokwatchoafbusdoafbusdokhasasbrsi31480asbrsi31480okended$aq340af”
    Napis ten został zakodowany w następujący sposób: 
    1. do początku każdego wyrazu dodano “ok”, np: “To jest dom” -> “okTo okjest okdom” 
    2. za każdym oryginalnym wyrazem wstawiono dodatkowy losowy wyraz do zdania, 
        np: “okTo okjest okdom” -> “okTo asifha okjest ??A?Sd okdom :asrof” 
    3. na koniec spacje zastąpione zostały znakiem “"
        np.:"okToasifhaokjest??A?Sdokdom : asrof" -> "okToasifhaokjest??A?Sd??A?Sdokdom$:asrof"

    To zadanie można rozwiązać za pomocą metod klasy string replace, join, startswith i split.
    :param text: 
    :return: 
    """
    # type your code

    encryptedMSG = str(text)
    #words = encryptedMSG.split('ok')
    words = encryptedMSG.split('$')

    decryptedMsgWords = list()
    for word in words:
        if word.startswith('ok'):
            word = word.replace('ok','')
            decryptedMsgWords.append(word)

    return " ".join(decryptedMsgWords)


test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af", [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])




# Q:
# wektor vs lista?
