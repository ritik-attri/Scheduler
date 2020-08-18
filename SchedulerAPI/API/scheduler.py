
from apscheduler.schedulers.background import BackgroundScheduler
from .views import checker
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=checker,trigger='interval',minutes=1)
    scheduler.start()

