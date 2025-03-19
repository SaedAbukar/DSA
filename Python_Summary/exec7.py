def custom_encoder(m):
    n = m.lower()
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    encoded_list = []
    for i in n:
        if i in reference_string: 
            encoded_list.append(reference_string.index(i))
        else:
           encoded_list.append(-1)
               
    return encoded_list