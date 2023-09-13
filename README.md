# Mach-Eight-Sample-Project


## Introduction

Thank you for checking out this Django project that finds pairs of integers that sum to a given value. This project was created as part of the Mach Eight Sample Project.

## Requirements

Before you get started, ensure you have the following installed:

- Python (3.7 or higher)
- Django (3.0 or higher)

## Getting Started

1. Clone this repository to your local machine using the following command:

   ```shell
   git clone https://github.com/LuisColorado-tech/Mach-Eight-Sample-Project.git

2. Navigate to the project directory:

    ```shell
    cd Mach-Eight-Sample-Project


3. Create a virtual environment (optional but recommended):
    ```shell
    python -m venv venv
    
4. Activate the virtual environment:

    On Windows:


        venv\Scripts\activate
    
    On macOS and Linux:

        source venv/bin/activate

5. Install project dependencies:

        pip install -r requirements.txt

6. Apply database migrations:

        python manage.py migrate

7. Run the development server:

        python manage.py runserver

8. Open your web browser and visit http://localhost:8000/

## How to Use
    Enter a comma-separated list of integers in the "Enter a comma-separated list of numbers" field.

    Enter the target sum in the "Enter the target sum" field.

    Click the "Find Pairs" button.

    The page will display pairs of integers that sum to the target value, if any are found.

# Description

This repository contains a `utils.py` file with a set of 5 functions related to the search for pairs of numbers in a list. The last of these functions, `measure_execution_time`, is used to measure the execution time of the other functions.

## Key Functions

Here's a brief description of some of the key functions contained in the `utils.py` file:

1. **find_pairs**: This function searches for pairs of numbers in a given list that sum up to a specific target. It uses a dictionary-based approach to improve efficiency and has a time complexity of O(n).

2. **find_pairs2**: This function uses nested loops to compare all possible pairs of numbers in the list. It has a time complexity of O(n^2), which makes it less efficient for larger input lists.

3. **find_pairs_with_set**: It utilizes a set data structure to search for pairs of numbers in the list. It has a time complexity of O(n) and is efficient for larger input lists.

4. **find_pairs_with_sort**: This function sorts the list and uses two pointers to find pairs of numbers that sum up to the target. It has a time complexity of O(n log n).

## Execution Time Measurement

The `measure_execution_time` function is responsible for measuring the execution time of these functions. It iterates through the pair-searching functions, executes each one with input data, and displays the time taken by each function.

This repository is useful for comparing the efficiency of different pair-searching approaches in Python and understanding how the performance of functions varies based on time complexity.
(InteractiveConsole)
>>> numbers=[-48,32,15,-45,17,21,14,-28,-1,30,0,42,10,-23,39,-47,20,-2,-20,26,-6,27,50,-7,37,-4,-42,-44,-19,16,47,-8,-12,-50,-30,-38,25,-33,-21,-15,48,2,36,1,-25,7,38,-24,-17,-26,-37,33,-34,31,-3,-18,44,-22,4,-14,-11,6,9,-40,-29,-13,41,22,-9,19,35,11,-35,-46,-43,12,28,8,45,49,-5,43,-27,34,18,40,23,3,46,29,-31,-32,5,-10,-31]
>>> target = 20
>>> from suma_pairs.utils import *
>>> measure_execution_time(numbers, target)
find_pairs: 0.000024 seconds
find_pairs2: 0.000546 seconds
find_pairs_with_set: 0.000121 seconds
find_pairs_with_sort: 0.000035 seconds



