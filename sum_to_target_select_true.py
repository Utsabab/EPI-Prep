#In the given array of tuples, the first is the integer and the second is the boolean True or False. Select least number of integers to have a sum of k_value.
#Next in the selected tuples, if any of the integer has False as the boolean replace it with the other integer with boolean True to make at least k_value.

def find_least_numbers(k_value, array_of_tuples):
  total_sum = 0
  for i,x in enumerate(array_of_tuples):
    if total_sum < k_value:
      total_sum += x[0]
      index_till = i
      index = i
      j = i + 1
    else:
      break     

  cant_be_replaced = True
  while (array_of_tuples[index][1] == 'True') and (cant_be_replaced):
    index = index - 1
    if index <= 0:
      cant_be_replaced = False
  sum_minus = total_sum - array_of_tuples[index][0]
  while (array_of_tuples[j][1] == 'False') and (cant_be_replaced):
    j = j + 1
    if j > (len(array_of_tuples) - 1):
      cant_be_replaced = False
  if (sum_minus + array_of_tuples[j][0]) > k_value:
    array_of_tuples = swap_func(array_of_tuples, index, j)
  return array_of_tuples[0:index_till+1]

def swap_func(array_of_tuples, first_index, second_index):
  temp_tuple = []
  temp_tuple.append(array_of_tuples[second_index][0])
  temp_tuple.append(array_of_tuples[second_index][1])
  array_of_tuples[second_index] = array_of_tuples[first_index]
  array_of_tuples[first_index] = temp_tuple
  return array_of_tuples
  
print(find_least_numbers(1000, [(600,'False'),(301,'False'),(300,'True'),(250,'False'),(240,'False'),(230,'True')]))