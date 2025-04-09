def get_pairs(list):
    even = Queue()
    odd = Queue()
    pairs = []
    for i in list:
        if i % 2 == 0:
            if odd._size > 0:
                n = odd.dequeue()
                pairs.append((i, n))
            else:
                even.enqueue(i)
        else:
            if even._size > 0:
                n = even.dequeue()
                pairs.append((n, i))
            else:
                odd.enqueue(i)
                
    return pairs