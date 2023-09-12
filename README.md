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

8. Open your web browser and visit http://localhost:8000/find_pairs/

## How to Use
    Enter a comma-separated list of integers in the "Enter a comma-separated list of numbers" field.

    Enter the target sum in the "Enter the target sum" field.

    Click the "Find Pairs" button.

    The page will display pairs of integers that sum to the target value, if any are found.

## Project Structure
    find_pairs - Django app containing the main functionality.
    templates - Contains HTML templates for rendering the web page.
    suma_pairs/utils.py - Utility function for finding pairs of integers.
    suma_pairs/views.py - Django views for handling the logic.
    suma_pairs/urls.py - URL routing for the app.
    suma_pairs/settings.py - Django project settings.
