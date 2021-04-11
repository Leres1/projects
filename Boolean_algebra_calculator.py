def NO(s):
    temp = ''
    for i in range(0, len(s)):
        if s[i] == 'F':
            temp += 'T'
        else:
            temp += 'F'
    return temp
# -


def AND(par1, par2):
    temp = ''
    for i in range(0, len(par1)):
        if par1[i] == 'T' and par2[i] == 'T':
            temp += 'T'
        else:
            temp += 'F'
    return temp
# |


def OR(par1, par2):
    temp = ''
    for i in range(0, len(par1)):
        if par1[i] == 'T' or par2[i] == 'T':
            temp += 'T'
        else:
            temp += 'F'
    return temp
# _


def IF(par1, par2):
    temp = ''
    for i in range(0, len(par1)):
        if par1[i] == 'T':
            temp += par2[i]
        else:
            temp += 'T'
    return temp
# &


def EQ(par1, par2):
    temp = ''
    for i in range(0, len(par1)):
        if par1[i] == 'T' and par2[i] == 'T':
            temp += 'T'
            continue
        if par1[i] == 'F' and par2[i] == 'F':
            temp += 'T'
            continue
        temp += 'F'
    return temp
# ~


def convert(txt):
    p = 'TTFF'
    q = 'TFTF'
    temp = ''
    for i in range(0, len(txt)):
        if txt[i] == 'p':
            temp += p
            continue
        if txt[i] == 'q':
            temp += q
            continue
        temp += txt[i]
    return temp


def withOutNo(txt):
    txt = convert(txt)
    i = 0
    temp = ''
    while True:
        if i >= len(txt):
            break
        if txt[i] == '-':
            if txt[i + 1] == 'T' or txt[i + 1] == 'F':
                temp += NO(txt[i + 1: i + 5])
                i = i + 5
            if i >= len(txt):
                break
        temp += txt[i]
        i += 1
    return temp
# checks the equation for minuses


def findLastBrackets(txt):
    if int(txt.count('(')) != 0:
        index = 0
        for i in range(0, len(txt)):
            if txt[i] == '(':
                index = i
        return index, txt.find(')', index, len(txt)), txt[index: txt.find(')', index, len(txt)) + 1]
    else:
        return ''
# will find the last open Brackets


def BracketsToNormal(txt):
    txt = txt[1:len(txt) - 1]
    return useFunc(txt)
# solves the equation in brackets


def useFunc(txt):
    tempList = []
    tempList2 = []
    firstVariable = txt[:4]
    for i in range(5, len(txt), 5):
        secondVariable = txt[i: i + 4]
        if txt[i - 1] == '|':
            tempList += [firstVariable + '|' + secondVariable]
            firstVariable = AND(firstVariable, secondVariable)
            tempList2 += [firstVariable]
        if txt[i - 1] == '_':
            tempList += [firstVariable + '_' + secondVariable]
            firstVariable = OR(firstVariable, secondVariable)
            tempList2 += [firstVariable]
        if txt[i - 1] == '&':
            tempList += [firstVariable + '&' + secondVariable]
            firstVariable = IF(firstVariable, secondVariable)
            tempList2 += [firstVariable]
        if txt[i - 1] == '~':
            tempList += [firstVariable + '~' + secondVariable]
            firstVariable = EQ(firstVariable, secondVariable)
            tempList2 += [firstVariable]
    return firstVariable, tempList, tempList2
# solves equations without parentheses and minuses


def deleteAllBrackets(txt):
    txt = withOutNo(txt)
    tempList = []
    tempList2 = []
    while txt.count('('):
        index, lastIndex, temp = findLastBrackets(txt)
        tempList += [temp]
        tempTxt1 = txt[:index]
        tempTxt2 = txt[lastIndex + 1:]
        s, s2, s3 = BracketsToNormal(temp)
        tempList2 += [s]
        txt = tempTxt1 + s + tempTxt2
        txt = withOutNo(txt)
    return txt, tempList, tempList2
# will return the equation without any brackets


def calculate(txt, history=False):
    txt = withOutNo(txt)
    txt, List, List2 = deleteAllBrackets(txt)
    txt, List3, List4 = useFunc(txt)
    List += List3
    List2 += List4
    if history:
        for i in range(0, len(List)):
            print(f'{i + 1}) ' + List[i] + ' = ' + List2[i])
    return txt
# solves the equation


# print(NO(p))
# print(AND(p, q))
# print(OR(p, q))
# print(IF(p, q))
# print(EC(p, q))
# print(convert('-(p&q)_q'))
# print(withOutNo('-p&q_-(q_p)'))
# print(calculate('-p&q_-(q_p)&-q'))
# print(findLastBrackets('-p$q_-(q_p)&-q'))
# print(BracketsToNormal(convert('(q_p&p)')))
# print(calculate('-p&q_-(q_p)&-q'))
# examples of functions
def Menu():
    while True:
        print('press 0 to exit')
        print("p = 'TTFF' q = 'TFTF'")
        print('Functions:\tNo( - ),\tAND( | ),\tOR( _ ),\tIF( & ),\tEquivalence( ~ )')
        print('Example of an equation - (p&q)&-((p|q)~p)_-q')
        # print(calculate('(p&q)&-(p|q)', True))
        equation = input()
        if equation == '0':
            break
        print('convert - ' + convert(equation))
        print('!operations minus no in history!')
        print('Answer - ' + calculate(equation, True))


Menu()
