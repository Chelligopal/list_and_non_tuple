def tillTheEnd(x): 
    return x[-1]  
  
def sort_list_tillTheEnd(tuples):  
  return sorted(tuples, key=tillTheEnd)  
  
print(sort_list_tillTheEnd([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))  