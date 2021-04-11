def unique_list(list):
    
  new_list = []
  for a in list:
    if a not in new_list:
      new_list.append(a)
  return new_list

print(unique_list([1, 2, 2, 3, 2])) 