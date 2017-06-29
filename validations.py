import re

NAME = re.compile(r'^[a-zA-z]+$')
EMAIL = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

def formIsValid(client):
    errors=[]
    isValid=True
    if len(client['email'])<1:
        errors.append("Please enter an email.")
        isValid = False
    if not re.match(EMAIL, client['email']):
        errors.append("Not a valid Email address.")
        isValid = False
    return {"isValid":isValid, "errors":errors}
