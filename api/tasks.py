from django.core.management import call_command

from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(call_command('update_records'),'interval',hours=1)
    scheduler.start()
