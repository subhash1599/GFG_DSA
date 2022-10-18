
def maximum_element(arr):

    res=arr[0]

    for i in arr:

        if res<i:
            res=i   
    return res  

print(maximum_element([1,34,0,56,2,12,13,4,90,8]))