## miniproject4ND
INF601 - Advanced Programming in Python  
Nikhil Dhage



### Description
This project use django to create and serve a web app for a restaurant.

### Frameworks/Packages/API 
This project uses the following packages and API
```
asgiref==3.7.2
Django==4.2.7
python-http-client==3.3.7
sendgrid==6.11.0
sqlparse==0.4.4
starkbank-ecdsa==2.2.0
tzdata==2023.3

```

### Pip Install Requirements
Please run the following

```
pip install -r requirements.txt
```

### How to Run
To start the Django development server, please type the following commands:

For **Windows**:

```
python manage.py runserver

```

### Register for a sendgrid account
!. Go to The following url 
```
Sengrid Account Registration : https://sendgrid.com/en-us

```

2. Register and create an account

3. Log in with your account credentials. You may need to setup a two -factor auth method


### Get an API Key 
You must have a sendgrid account to use the sendgrid api 
PLease follow the instructions below

1. Navigate to Settings on the left navigation bar, and then select API Keys.
2. Click Create API Key.
3. Give your API key a name.
4. Select Full Access, Restricted Access, or Billing Access.
5. If you're selecting Restricted Access, or Billing Access, select the specific permissions to give each category. For more information, see API key permissions.
6. Click Create & View.
7. Copy your API key somewhere safe. Sendgrid supports local .env files


### Setup API KEY 
1. Create a local .config or a .env 
2. copy sendgrid API KEY into .env or .config file

```
API_KEY='YOUR_API_KEY'

```


### Sendgrid API Reference 
This is the API Reference docs url 
Choose Python for instructions and example code
for th python mail helper api.

```
https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/authentication

```

### How to Quit
Use this command to quit the flask app or terminate the app 
in the console of your editor'
```
Ctrl + C 