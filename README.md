# CRUD-Assessmet-3
E-Commerce website 1

Incomplete items:
  Search functionality
  Website visual stying needs work (CSS)
  Website functionality
    Ability to add items to Shopping Cart persisted to the database
    Ability to retrieve Shopping Cart items from the database, and present them on the front end
    Ability to see item quantities aggregated and total order price in Shopping Cart


# Start up
1. Open your terminal or command prompt.

2. Navigate to the directory where your Python project is located. 
  cd path/to/project

3. Once you are in the project directory, create a new virtual environment using the python -m venv command followed by the name you want to give your environment. 
  python -m venv myenv

4. Activate the virtual environment using the appropriate command for your operating system:
  Windows: myenv\Scripts\activate
  Linux or macOS: source myenv/bin/activate
    (When the virtual environment is activated, you should see the name of the environment in your command prompt or terminal.)

5. Install the packages listed in your requirements.txt file using the pip install command followed by the file path to the requirements.txt file. 
  pip install -r requirements.txt

6. Wait for the installation to complete. This will install all the packages listed in your requirements.txt file into your virtual environment.

7. Once the installation is complete, you can use the packages in your Python code.

8. To exit the virtual environment, you can use the deactivate command.

9. Passwords: In the root directory create 2 files .env and .gitignore (touch .env / touch .gitignore).
  Assessment_3/CRUD-Assessmet-3/my_ecommerce_site/.gitignore
    .env
    ../env
    
   Assessment_3/CRUD-Assessmet-3/my_ecommerce_site/.env
    django = ''
  
  Assessment_3/CRUD-Assessmet-3/my_ecommerce_site/my_ecommerce_site/settings.py
    
    from pathlib import Path
    import os # <-------------------------------------------------------------- added for password security
    from dotenv import load_dotenv # <----------------------------------------- added for password security

    load_dotenv()

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ['django'] # <-------------------------------------- added for password security
