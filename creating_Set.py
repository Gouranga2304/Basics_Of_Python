#creating the set
fruits = {"apple", "banana", "cherry"}
print (fruits)


#Key set methods
my_set = {1, 2, 3, 4}
print(my_set)

my_set.add(5)        # {1, 2, 3, 4, 5}
print(my_set)

my_set.remove(2)
print(my_set)   
                       # {1, 3, 4, 5}
my_set.discard(10) 
print(my_set)
                    # No error if element not found
my_set.pop()
print(my_set)   
                        # Removes random element

