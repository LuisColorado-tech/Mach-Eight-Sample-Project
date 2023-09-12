def find_pairs(numbers, target):
    num_dict = {}
    pairs = []

    for num in numbers:
        complement = target - num
        if complement in num_dict:
            pairs.append((num, complement))
        num_dict[num] = True

    return pairs
