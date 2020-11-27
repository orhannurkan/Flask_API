    # PROJECT: Flask API
    - run ML_server.py file
    - open server link
    - login by user:orhan password:12345
    - then send a prediction request or upload an image
    
    Learning Objectives¶
You will learn how to create an API in Python with the Flask module. At the end of the challenge, you will be able to:

Create a Flask app
Add a route that shows hello world
Add a route with GET method
Add a route with POST method
Get data from a GET request, transorm it and return it
Get data from a POST request, transorm it and return it
Deploy your API on Heroku
The Mission
You are an intern in a company to provide AI models to their customers. Unfortunatly, the machine learning engineers that work with you are not very good... They spend more time drinking coffee and playing video games than doing their job. After a few weeks, the project manager comes to you and tells you that they have a client that is really upset to not have his model yet. He asks you to create the API to get the data and return a random prediction. It will give him more time to beg the ML engineers to finish the project.

You decide to use Flask as it's the best tool to boostrap an API in python. You receive a mail from the client:

Dear lazy company,
WE NEED OUR MODEL TO BE READY BY TOMORROW OR YOU WILL BE IN TROUBLE!!!
OUR LAWYERS ARE READY TO SUE YOU!

We will test your API in 48h.
You will find in attachment the routes that should be working (AND I HOPE FOR YOU THEY WILL):

Kind regards,
Your lovely client,
MadCompany
Attachments:
# Route to check if the server runs
GET /status -> "Alive!"

# Route to login
POST /login -> "Login success for user {USER_NAME_HERE} with password of length: {PASSWORD_LENGTH_HERE}!"
body: {
    username: <USER_NAME_HERE>
    password: <PASSWORD_HERE>
}

# Route that returns the prediction
GET /predict/<seller_avaible:int>/<month:str>/<customer_visiting_website:int> -> Prediction (int between 2000 and 5000)
Must-have features
A GET route at /status that returns the string "alive"
A POST route at /login that returns a string containing "Login success for user USER_NAME_HERE with password of length: PASSWORD_LENGTH_HERE!".
A GET route at /predict that takes 3 arguments (month, customer_visiting_website, seller_available) and returns an int between 2000 and 5000.
Nice-to-have features
Folow pep8 rules.
Add a docstring for each route.
Use type hints in all your functions.
Use the Black formatter to format your code.
Add a route that takes an image and saves it on the server. Return the image's server path.
Add unit tests for at least one route.
Miscellaneous information
Feel free to play with Flask and add your own routes!

Deliverables
Publish your source code on the GitHub repository.
Wrap your API in a Docker container.
Deploy it on Heroku.
Pimp up the README file:
What, Why, When, How, Who.
Pending things to do
It must contain a link to the "live" version. The "live" version must contain a link to the source code on GitHub.
Publish the link to the "live" version on your startup's Ryver channel.
Steps
Create the repository.
Study the request (What & Why ?)
Identify technical challenges (How ?)
ULM prototype.
Design your API.
Create a Docker file to auto-run you API.
Deploy it on Heroku.
Evaluation criterias
Criteria	Indicator	Yes/No
1. Is complete	The student has realized all must-have features.	
There is a published Heroku server available.	
...	
2. Is Correct	The code has been formated using Black.	
There is a route that can save an image and return its path	
3. Is clean	There is a docstring for each function	
Each function is typed
A final note of encouragement
And remember, I'm sure you're going to make it!
