# Q.10 You have to modify a tuple item without converting it into a list. Provide an example of any case where this exactly can happen. 

simple_tuple = (1, 2, 3)
print("Before adding a list:", simple_tuple)

modified_tuple = simple_tuple + ([4, 5, 6],)
print("After adding a list:", modified_tuple)

modified_tuple[3].append(7)
print("After modifying the list inside the tuple:", modified_tuple)