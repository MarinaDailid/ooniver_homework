some_list = [1,2,3,4]
i = 0
len_some_list = len(some_list)
while i < len_some_list:
    some_list[i]=some_list[i] * 2
    print(some_list[i] , end='')
    i += 1
