def numberOfPairs(a, k):
    pair_count = 0
    dict_for_pairs = {}
    int_dict ={}
    for i in a:
        if i not in int_dict:
            int_dict[i] = 1
        else:
            int_dict[i]+=1
    
    for y in a:
        temp = k - y
        if temp in int_dict:
            if temp == y:
                if int_dict[temp] > 1:
                    dict_for_pairs[(y,temp)] = 1
            else:        
                dict_for_pairs[(max(y,temp), min(y,temp))] = 1
    S = set(dict_for_pairs.keys())
    # print(S)
    return (S)


print(numberOfPairs([1,3,44,46,1,3,9,],47))