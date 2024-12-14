PYTHON_MANAGE = python manage.py
MIGRATE = migrate
MIGRATIONS = makemigrations


.PHONY: run
run:
	$(PYTHON_MANAGE) runserver


.PHONY: migrate
migrate:
	$(PYTHON_MANAGE) $(MIGRATE)


.PHONY: migrations
migrations:
	$(PYTHON_MANAGE) $(MIGRATIONS)

.PHONY: superuser
superuser:
	$(PYTHON_MANAGE) createsuperuser

.PHONY: grun
grun:
	gunicorn core.project.wsgi:application -b 0.0.0.0:8000