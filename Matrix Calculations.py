#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
YZV102E - HOMEWORK 2
Student ID: beyza nur keskin
Student Name: 150200320
"""


def print_matrix(matrix):
    
    matrix = list(matrix)
    for j in matrix:
        print(*j, sep=' ')
    
# I tried to write matrix in desired format

def read_matrix():
    
    n=int(input())
    # first step i get input from user for size of matrix
    matrix=[]
    # then i created a list based on this input
    for i in range(n):
        row=input().split()
        matrix.append(list(row))

    return matrix

def is_symmetric(matrix):
    
   # i tried to find symmetric of matrix there is nothing to explain.
    for r in range(len(matrix)):
        sayac=0
        for t in range(len(matrix)):
            if sayac!=0:
                break
            sayi1=matrix[r][t]
            sayi2=matrix[t][r]
            if sayi1!=sayi2:
        # i checked the equivalence
                sayac=+1
        if sayac!=0:
            is_sym = False
        else:
            is_sym = True
 
    return is_sym
def transpose_matrix(matrix):
    # i tried to find transpose of matrix there is nothing to explain too.
    transpose_matrix=[]
    
    for m in range(len(matrix)):
        empty_row = [0 for i in range(len(matrix))]
        transpose_matrix.append(empty_row)
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            transpose_matrix[a][b]=matrix[b][a]
    #i changed their places
    
    
    return transpose_matrix
        
def find_smallest_and_biggest(matrix):
    
    mtl= list()
    # i created a new empty list 
    for f in matrix:
        for e in f:
            mtl.append(e)
    # I created a list from the elements of the matrix because i wanted to find min and max element easier
    mini = mtl[0]
    for h in mtl:
        if mini > h:
            mini = h        

    # i found min and max element
    maxi = mtl[0]
    for g in mtl:
        if maxi < g:
            maxi = g        

    return mini , maxi

def find_mean(matrix):
    
    
    #i also created a list to calculate the average because it gets easier
    mtl= list()
    for f in matrix:
        for e in f:
            mtl.append(e)
    sumofmtl = 0
    for l in mtl:
        sumofmtl += int(l)
    sumofmtl = 0
    k = 0
    for j in mtl:
        sumofmtl += int(j)
        k +=1
    meanofmtl = sumofmtl / k
    # i calculated mean of the matrix

    return meanofmtl

def find_position_of_element(matrix,element):
    
    
    # this part is little bit complicated.It was easier to 
    #process from the list, but this time I had difficulty 
    #calculating the positions of the indexes. 
    #so I found a connection between their position in the list
    #and their position in the matrix and I calculated it.
    
    mtl= list()
    for f in matrix:
        for e in f:
            mtl.append(e)
            
   
    mini = mtl[0]
    for h in mtl:
        if mini > h:
            mini = h

    minx= mtl.index(mini)        
    sutun = minx // len(matrix)
    satir = minx % len(matrix)
    positionn = []
    positionn.append(sutun)
    positionn.append(satir)
   
    maxi = mtl[0]
    for g in mtl:
        if maxi < g:
            maxi = g  


    maxx= mtl.index(maxi)


    sutun1 = maxx // len(matrix)
    satir2 = maxx % len(matrix)


    positionx = []

    positionx.append(sutun1)
    positionx.append(satir2)
    
    if element == min1:
        return positionn
    elif element == max2:
        return positionx

def find_special_cards(matrix, position_small, position_big):
 
    special_cards = []
    nl = 0 
    for i in matrix:
        del matrix[nl][position_big]
        nl += 1
    del matrix[position_small]
    #rows were already in the matrix as a list. 
    # When I wrote an index, I was completely deleting the order of that list. therefore I did so.
    
    special_cards.append(matrix)


    return special_cards

def card_game(matrix):
    

    
    sum_special_cards = 0
    
    
                
                        
            
 

    return sum_special_cards



if __name__ == "__main__":
    card = read_matrix()

    print("Card Matrix: ")
    print_matrix(card)

    print("Transpose of the Matrix: ")
    card_t = transpose_matrix(card)
    print_matrix(card_t)

    print("Is the matrix symmetric: ", is_symmetric(card))

    min1, max2 = find_smallest_and_biggest(card_t)
    print("Smallest Number of the Matrix: ", min1)
    print("Biggest Number of the Matrix: ", max2)

    print("Mean of the elements: %.2f" % find_mean(card_t))
    
    
    
    
    
    
    
    

    small_pos = find_position_of_element(card_t,min1)
    big_pos = find_position_of_element(card_t,max2)
    print("Position of the smallest Number : ", small_pos)
    print("Position of the Biggest Number : ", big_pos)
    
    
    
    
    
    
    

    print("Special Cards : ")
    print(find_special_cards(card_t, small_pos[0], big_pos[1]))

    print("Sum of the special cards: ", card_game(card))

