l_input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten_list = []

def FlattenFunc(l_input):
    for i in l_input:
        if (type(i) == list):
            FlattenFunc(i)
        else:
            flatten_list.append(i)

    return flatten_list

print(FlattenFunc(l_input))

L=[[1, 2], [3, 4], [5, 6, 7]]

def Reverse(L):
    L.reverse()
    for i in L:
        if (type(i) == list):
            i.reverse()
    return L

print(Reverse(L))


 
