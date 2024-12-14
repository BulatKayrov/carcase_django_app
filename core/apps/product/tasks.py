from core.project.celery import app



@app.task
def you_task():
    print('Hello from view')


