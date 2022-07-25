# To Create requirements.txt file
pip freeze > requirements.txt

https://www.youtube.com/watch?v=oA8brF3w5XQ
https://www.youtube.com/watch?v=K_RTlbOOCts&t=414s
gunicorn --bind=0.0.0.0 --timeout 600 run

python -m venv venv

venv\Scripts\activate

SET FLASK_APP="app.py"
SET FLASK_DEBUG=1
flask run

# [Use Only Once - At First time configuration] To install all Libs required for aplication
	pip install -r requirements.txt

# [Use Only Once - At First time configuration] To configure database
	$ flask db init - This command creates a migrations directory in the <Project Folder> directory:
	$ flask db migrate - This command will create initial migrations
	$ flask db upgrade - This command will create basic tables to database using above migrations

# To Enable environment for Flask Server
	venv\scripts\activate

# To run the Flask Server on powershell terminal
	$env:FLASK_CONFIG="development"
	$env:FLASK_APP="run.py"
	$env:FLASK_DEBUG=1
	flask run

	Press CTRL+C to quit the flask server

# To close environment
	deactivate