import time

def find_pairs(numbers, target):
    ''' In find_pairs2, it uses a dictionary (num_dict) to store numbers as keys while 
    iterating through the list of numbers. This allows constant-time (O(1)) lookups to check 
    if a complementary number exists in the dictionary. This results in a linear time (O(n)) 
    complexity for finding pairs, which is faster than O(n^2).
    '''
    num_dict = {}
    pairs = []

    for num in numbers:
        complement = target - num
        if complement in num_dict:
            pairs.append((num, complement))
        num_dict[num] = True

    return pairs

def find_pairs2(numbers, target_sum):
  """ uses nested loops to compare all possible pairs of numbers in the list. This results
   in a quadratic time (O(n^2)) complexity, making it less efficient for larger input lists compared to find_pairs
  """

  pairs = []
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        pairs.append((numbers[i], numbers[j]))

  return pairs


def find_pairs_with_set(numbers, target):
    ''' Using a Set (O(n) time complexity):
    '''
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    
    return list(pairs)

def find_pairs_with_sort(numbers, target):
    '''Sorting and Two-Pointers (O(n log n) time complexity):
    '''
    numbers.sort()
    left, right = 0, len(numbers) - 1
    pairs = []
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            pairs.append((numbers[left], numbers[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs

# Función que ejecuta y mide el tiempo de cada función
def measure_execution_time(numbers, target):
    functions = [
        ('find_pairs', find_pairs),
        ('find_pairs2', find_pairs2),
        ('find_pairs_with_set', find_pairs_with_set),
        ('find_pairs_with_sort', find_pairs_with_sort),
    ]

    for name, function in functions:
        start_time = time.time()
        result = function(numbers, target)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'{name}: {execution_time:.6f} seconds')





