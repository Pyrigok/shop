run:
	python3 shop_project/manage.py runserver

superuser:
	python3 shop_project/manage.py createsuperuser

migrations:
	python shop_project/manage.py makemigrations

migrate:
	python shop_project/manage.py migrate

active:
	source shop_venv/bin/activate

celery:
	celery -A shop_project worker -l INFO
	#celery -A shop_project/shop_project/providers/ worker --loglevel=info
	#celery -A shop_project worker -l INFO -Q general, order_creation_queue, confirmation_email_queue

redis:
	redis-server

users:
	python shop_project/manage.py create_users

goods:
	python shop_project/manage.py create_goods

orders:
	python shop_project/manage.py create_orders

static:
	python shop_project/manage.py collectstatic
