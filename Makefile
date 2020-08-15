migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
shell_plus:
	python manage.py shell_plus
superuser:
	python manage.py createsuperuser
restartdb:
	sudo service mongod restart
stopdb:
	sudo service mongod stop
startdb:
	sudo service mongod start
