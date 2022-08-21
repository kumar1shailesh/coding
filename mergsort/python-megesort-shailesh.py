def merge_sort(inputarray):
    if len(inputarray) > 1 :
        leftarray = inputarray[0:len(inputarray)//2]
        rightarray = inputarray[len(inputarray)//2:len(inputarray)]

        #recursion
        merge_sort(leftarray)
        merge_sort(rightarray)

        #merge
        i=0
        j=0
        k=0
        while i <len(leftarray) and j< len(rightarray):
            if leftarray[i] < rightarray[j]:
                inputarray[k] = leftarray[i]
                i +=1
            else:
                inputarray[k] = rightarray[j]
                j +=1
            k +=1

        while i < len(leftarray):
            inputarray[k] = leftarray[i]
            i += 1
            k += 1

        while j < len(rightarray):
            inputarray[k] = rightarray[j]
            j += 1
            k += 1
    print(inputarray)

inputarray = [3,4,2,6,8,87,45,67,5,66,88]
merge_sort = merge_sort(inputarray)
