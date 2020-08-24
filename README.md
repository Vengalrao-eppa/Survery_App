Instructions to run the APP

- Unzip the folder
- go to SRC folder
- Activate Environment: run venv/scripts/activate 
- To create database, run the following commands
	1. python - to enter python shell
		from app import create_app, db
		app = create_app()
		app.app_context().push()
		with app.app_context():
			db.create_all(app=app)
	(creates the database)
- Run utility script to load questions to QuestionTable
	python load_db.py

-----------------------------------------------------------------------------------------------------------
Survey APP - API Development

I have created 4 API's for the entire application

1. /api/v1/home - Accept Methods: GET, POST
	- This API is for Home/Index page
	- User should enter name and email (from UI side)
	- Details will be saved into Database
	- email and name are the mandatory fields
	- Get Request Response
		{
			"message": "welcome to the Survey App!"
        }
	- Sample Post Payload
		{
			"email": "test_app_4@gmail.com",
			"name": "Test App 4"
		}

2. /api/v1/questions - Accept Methods: GET
	- This API to load questions from database and pass to UI developer
	- Questions need to serialize to JSON (as it is passed as STRING from backend)
	- UI needs to have a logic to show the questions to the end user
	- The IDEA I can think of is, since we have all the questions UI developer can write a logic to handle the questions
	- Each payload have fields like QuestionID, QuestionText, QuestionType, Options, NextQuestion
	- For a QuestionID we can have multiple values
		- We can have different QuestionText's
	- QuestionType: Text, Choice, YES/NO
	- The reason UI should handle this is because Backend should not query the database for each question to show to EndUser
	- We should not save the response to database everytime as it creates an unnecessary load on Database
	- We should collect the user responses and save them to database in one transaction 
	
3. /api/v1/question/<question_id> - Accept Methods: POST
	- Returns the question details as a response
	
4. /api/v1/<user_id>
	- UI Developer should pass a list of collected responses along with USERID
	- Saves all the responses of an user in Database
	
Misc:
	- I have written a utility function to load the questions json file into Database (SQLAlchemy)

	
-----------------------------------------------------------------------------------------------------------
I can think of the following implementations to achieve Optimization
1. I did not get a chance to use the MONGODB as it was taking time for me to setup the environment in Cloud
	- I have done the development locally
2. We can implement a cache to store the User Responses more faster
3. I can write another API to load/create the questions table
4. I would create the docker for the application and deploy in Cloud GCP

