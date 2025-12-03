LINK: https://docs.djangoproject.com/en/5.2/intro/tutorial01/

## To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:
```
python -m venv tutorial-env
```

## Once you’ve created a virtual environment, you may activate it.

On Windows, run:
```
tutorial-env\Scripts\activate
```

## To deactivate a virtual environment, type:
```
deactivate
```
into the terminal.


# 1. Create project folder
mkdir backendprojects/project3
cd backendprojects/project3

# 2. Create venv INSIDE project3
python -m venv venv

# 3. Activate it
venv\Scripts\activate

# 4. Install what THIS project needs
pip install django
pip install pillow  # if needed
# etc.

# 5. Start Django project
django-admin startproject myproject .

## What About Git/Sharing?
Add to .gitignore in each project:

```
venv/
__pycache__/
*.pyc
```

## Then share only:

requirements.txt (generated from that project's venv)

Friend clones it:
```
git clone your-repo project3
cd project3
python -m venv venv          # Creates THEIR OWN venv
venv\Scripts\activate
pip install -r requirements.txt  # Gets exact same packages
```


# Pro-Level Requirements Structure:
Single file (simple projects):
```
requirements.txt
```
# Split files (medium projects):
```
requirements/
├── base.txt      # Everyone needs these
├── dev.txt       # Development only
├── prod.txt      # Production only
└── local.txt     # Your local machine only
```
# Pipenv/Poetry (modern approach):
```
pyproject.toml    # Replaces requirements.txt
Pipfile           # Alternative modern approach
```