from django.shortcuts import render
from suma_pairs.utils import *


def home_view(request):
    return render(request, 'suma_pairs/home.html')

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

def find_pairs2_view(request):
    if request.method == 'POST':
        input_numbers = request.POST.get('input_numbers')
        target_sum = request.POST.get('target_sum')

        if input_numbers and target_sum:
            numbers = list(map(int, input_numbers.split(',')))
            target = int(target_sum)

            pairs = find_pairs2(numbers, target)

            context = {
                'input_numbers': input_numbers,
                'target_sum': target_sum,
                'pairs': pairs,
            }

            return render(request, 'suma_pairs/find_pairs.html', context)

    return render(request, 'suma_pairs/find_pairs.html')
def find_pairs_with_set_view(request):
    if request.method == 'POST':
        input_numbers = request.POST.get('input_numbers')
        target_sum = request.POST.get('target_sum')

        if input_numbers and target_sum:
            numbers = list(map(int, input_numbers.split(',')))
            target = int(target_sum)

            pairs = find_pairs_with_set(numbers, target)

            context = {
                'input_numbers': input_numbers,
                'target_sum': target_sum,
                'pairs': pairs,
            }

            return render(request, 'suma_pairs/find_pairs.html', context)

    return render(request, 'suma_pairs/find_pairs.html')

def find_pairs_with_sort_view(request):
    if request.method == 'POST':
        input_numbers = request.POST.get('input_numbers')
        target_sum = request.POST.get('target_sum')

        if input_numbers and target_sum:
            numbers = list(map(int, input_numbers.split(',')))
            target = int(target_sum)

            pairs = find_pairs_with_sort(numbers, target)

            context = {
                'input_numbers': input_numbers,
                'target_sum': target_sum,
                'pairs': pairs,
            }

            return render(request, 'suma_pairs/find_pairs.html', context)

    return render(request, 'suma_pairs/find_pairs.html')

