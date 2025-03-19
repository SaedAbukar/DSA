def combine_lists(n, m):
    combined_list = []
    index1 = 0
    index2 = 0
    
    while index1 < len(n) and index2 < len(m):
        if n[index1] < m[index2]:
            combined_list.append(n[index1])
            index1 += 1
        else:
            combined_list.append(m[index2])
            index2 += 1
            
    if index1 < len(n):
        combined_list.extend(n[index1:])
    if index2 < len(m):
        combined_list.extend(m[index2:])
    
    return combined_list
