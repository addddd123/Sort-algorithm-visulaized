import random
import time
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
hath=['/','*','-','+', 'x', 'o', 'O']
Length=20
def bubblesort(getList):#get list is random gernrated array
   
    swap=None
    c=1
    while c ==1:
        c=0
        for i in range(len(getList)-1):
            if getList[i]>getList[i+1]:
                c=1
                swap=getList[i+1]
                getList[i+1]=getList[i]
                getList[i]=swap
                plt.bar(np.arange(0,Length),getList, align='center', alpha=0.5,color=['black', 'red', 'green', 'blue', 'cyan'],linestyle='-',hatch=random.choices(hath))
               
                
                plt.title('Bubble sort in action')
                
                plt.pause(0.001)
                plt.clf()
                
   
    return getList
def insertionSort(getList1):
    for i in range(1,len(getList1)):
        key=getList1[i]
        j=i-1
        while j>=0 and key<getList1[j]:
            getList1[j+1]=getList1[j]
            j=j-1
            plt.bar(np.arange(0,Length),getList1, align='center', alpha=0.5,color=['black', 'red', 'green', 'blue', 'cyan'],linestyle='-',hatch='/')
            plt.title('Insertion sort in action')
            plt.pause(0.001)
            plt.clf()
        getList1[j+1]=key
        plt.bar(np.arange(0,Length),getList1, align='center', alpha=0.5,color=['black', 'red', 'green', 'blue', 'cyan'],linestyle='-',hatch='/')
        plt.title('Insertion sort in action')
        plt.pause(0.001)
        plt.clf()
    return getList1
####################################################################################          
def genrateRandom():
    randomList=[]
    
    # Length=int(input("input enter length of list \n"))
    # start=int(input("enter start of sequence \n"))
    # stop=int(input("enter stop of sequence "))
    for i in range(Length):
        randomList.append(random.randint(10,3000))
    print("random sequenc is ",randomList)
    return randomList

################################################################
def selectionsort(getList):
    k=0
    cond=0
    while cond!=len(getList):
        min=getList[k]
        
        for i in range(k,len(getList)):
            if min> getList[i]:
                min=getList[i]
                getList[i]=getList[k]
                getList[k]=min
                
                plt.bar(np.arange(0,Length),getList, align='center', alpha=0.5,color=['black', 'red', 'green', 'blue', 'cyan'],linestyle='-')
                plt.title('Selection sort in action')
                plt.pause(0.001)
                plt.clf()
        plt.bar(np.arange(0,Length),getList, align='center', alpha=0.5,color=['black', 'red', 'green', 'blue', 'cyan'],linestyle='-')
        plt.title('Selection sort in action')
        plt.pause(0.001)
        plt.clf()
        k+=1
        cond+=1
################# Qucik SOrt############################################      
        
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
            while start < len(array) and array[start] <= pivot:
                start += 1
            while array[end] > pivot:
                end -= 1
            
            if(start < end):
                array[start], array[end] = array[end], array[start]
                
           
    array[end], array[pivot_index] = array[pivot_index], array[end]
    plt.bar(np.arange(0,Length),array, align='center', alpha=0.5,color=['black', 'red', 'green', 'blue', 'cyan'],linestyle='-',hatch='/')
    plt.title("Qucik sort in action")
    plt.pause(0.001)
    plt.clf()
    return end
	
def quick_sort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
####################################################





key=11111
while key!=0:
    if key==1:
        bubblesort(genrateRandom())
        plt.show()
    elif key==2:
        insertionSort(genrateRandom())
        plt.show()
    elif key==3:
        selectionsort(genrateRandom())
        plt.show()
    elif key==4:
        array=genrateRandom()
        quick_sort(0, len(array) - 1,array )
        plt.show()
    else:
        pass
    key=int(input("""
            enter 0 to exit
            enter 1 for bubble sort
            enter 2 for insertion sort
            enter 3 for selection sort
            enter 4 for qucik sort
            """))