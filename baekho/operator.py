from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import send_mail, china, usa, japan, vietnam, australia

def start():
    scheduler=BackgroundScheduler(timezone="Asia/Seoul")

    # scheduler.add_job(send_mail, "cron", hour=14, minute=58)

    print("==스케줄러 시작==")
    scheduler.start()
    print("==스케줄러 완료==")