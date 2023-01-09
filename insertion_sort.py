def insort(arr):
    n=int(len(arr))
    for j in range (1,n):
        key=arr[j]

        i=j-1
        while(i>=0 and arr[i]>key):
            arr[i+1]=arr[i]
            i=i-1
        
        arr[i+1]=key
    
    return(arr)

def main():
    a=[9,3,2,6,1,8]
    print(insort(a))

main()