migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
shell_plus:
	python manage.py shell_plus
superuser:
	python manage.py createsuperuser
mongorestart:
	sudo service mongod restart
mongostart:
	sudo service mongodb start
mongorepair:
	sudo mongod --repair
mongostatus:
	sudo service mongodb status