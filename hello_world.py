print('hello world')

my_list = [2, 7, 21, 4, 12, 1]
result = [x * 2 for x in my_list]
print (result)

import numpy as np
nyArray = np.array(my_list)
print(nyArray)
result = nyArray ** 2
print(result)
result = sum(nyArray)
print(result)


# Condition for filtering
condition = nyArray > 5

# Filter array
filter_array = nyArray[condition]
print(filter_array) 
