


def all_sub_lists(lst):
    sub_lists = [[]]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sub_list = lst[i:j]
            sub_lists.append(sub_list)
    final_lst = sorted(sub_lists, key=len)
    return final_lst
    
        
            
print(all_sub_lists([1, 2, 3])) #[[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
print(all_sub_lists([4, 6, 1, 3])) #[[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]