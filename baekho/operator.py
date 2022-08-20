from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import send_mail, china, usa, japan, vietnam, australia

def start():
    scheduler=BackgroundScheduler(timezone="Asia/Seoul")
    
    # 5개국 
    # scheduler.add_job(china, "cron", hour=15 , minute=3)
    # # scheduler.add_job(usa, "cron", hour= , minute=5)
    # # scheduler.add_job(japan, "cron", hour= , minute=5)
    # scheduler.add_job(vietnam, "cron",hour=15 , minute=3)
    # scheduler.add_job(australia, "cron", hour=15 , minute=3)

    scheduler.add_job(send_mail, "cron", hour=12, minute=22)

    print("==크롤링 스케줄러 시작==")
    scheduler.start()
    print("==크롤링 스케줄러 완료==")