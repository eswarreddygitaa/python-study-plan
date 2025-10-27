# Given sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1  # Join A and B (Union)
A_union_B = A.union(B)
print("Join (Union) of A and B:", A_union_B)

#2  # Find A intersection B
A_intersection_B = A.intersection(B)
print("Intersection of A and B:", A_intersection_B)

#3  # Is A subset of B
is_subset = A.issubset(B)
print("Is A a subset of B?:", is_subset)

#4  # Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint?:", are_disjoint)

#5  # Join A with B and B with A (Union both ways, same result)
A_join_B = A.union(B)
B_join_A = B.union(A)
print("A joined with B:", A_join_B)
print("B joined with A:", B_join_A)

#6  # What is the symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", sym_diff)

#7  # Delete the sets completely
del A
del B
print("Sets A and B have been deleted.")
