def merge(list_a, list_b):
  #create new sorted list - empty
  combined_list = []
  #loop while there are still elements in both arrays
  while len(list_a) != 0 and len(list_b) != 0:
    #if the month of the first element in list_a is less 
    # than the month of list_b 
    # add the lower of the two compared elements
    # remove that element from the raw list
    if int(list_a[0][1]) < int(list_b[0][1]):
      combined_list.append(list_a[0])
      list_a.remove(list_a[0])
    elif int(list_a[0][1]) > int(list_b[0][1]):
      combined_list.append(list_b[0])
      list_b.remove(list_b[0])
    else:
      # if the day of the first element in list_a is less 
      # than the day of list_b 
      # add the lower of the two compared elements
      # remove that element from the raw list
      if int(list_a[0][2]) < int(list_b[0][2]):
        combined_list.append(list_a[0])
        list_a.remove(list_a[0])
      elif int(list_a[0][2]) > int(list_b[0][2]):
        combined_list.append(list_b[0])
        list_b.remove(list_b[0])
      else:
        # if the minute of the first element in list_a is less 
        # than the minute of list_b 
        # add the lower of the two compared elements
        # remove that element from the raw list
        if int(list_a[0][4]) < int(list_b[0][4]):
          combined_list.append(list_a[0])
          list_a.remove(list_a[0])
        elif int(list_a[0][4]) > int(list_b[0][4]):
          combined_list.append(list_b[0])
          list_b.remove(list_b[0])
  # after the loop, if list a is empty, add the last element in list b
  # to the combined list, else, b is empty, so add the last element of a
  if len(list_a) == 0:
    combined_list.append(list_b[0])
  else:
    combined_list.append(list_a[0])
  #return this ordered list
  return combined_list

def mergeSort(raw_array):
  if len(raw_array) == 0 or len(raw_array) == 1:
    return raw_array
  else:
    #Split array into two
    middle = len(raw_array)//2
    list_1 = mergeSort(raw_array[:middle])
    list_2 = mergeSort(raw_array[middle:])
    print("Return Merge")
    return merge(list_1, list_2)