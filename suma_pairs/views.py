from django.shortcuts import render
from suma_pairs.utils import find_pairs

def find_pairs_view(request):
    if request.method == 'POST':
        input_numbers = request.POST.get('input_numbers')
        target_sum = request.POST.get('target_sum')

        if input_numbers and target_sum:
            numbers = list(map(int, input_numbers.split(',')))
            target = int(target_sum)

            pairs = find_pairs(numbers, target)

            context = {
                'input_numbers': input_numbers,
                'target_sum': target_sum,
                'pairs': pairs,
            }

            return render(request, 'suma_pairs/find_pairs.html', context)

    return render(request, 'suma_pairs/find_pairs.html')
