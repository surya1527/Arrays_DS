# Iterative python program to reverse an array

# Function to reverse A[] from start to end
def reverseList(A):
    start = 0 
    end = len(A) - 1
    while(start < end):
        A[start] , A[end] = A[end] , A[start]   #Swapping the start and end elements in the array by index value

        #Incrementing and decrementing the index values simultaneously 

        start+=1
        end-=1

    return
		

# Driver code to test above function

A = list(map(int,input().split()))    #Enter multiple values into the list
print("array of elements are:", A)

reverseList(A)
print("Reverse array or list is: " ,A )
