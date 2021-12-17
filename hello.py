#!/usr/bin/env python3

import logging
import sys
import time
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from colorama import Fore

# https://betterprogramming.pub/introduction-to-apscheduler-86337f3bb4a6
# https://apscheduler.readthedocs.io/en/stable/userguide.html
# https://enqueuezero.com/projects/apscheduler/
# https://docs.python.org/3/howto/logging.html
# https://pypi.org/project/colorama/


def hello():
    now = datetime.now()
    curr_date = now.strftime("%Y/%m/%d-%H:%M:%S")
    # https://stackoverflow.com/questions/107705/disable-output-buffering/107717
    print(f"{Fore.GREEN}{curr_date} -> Hello from {sys.platform}", flush=True)


def hello_daily():
    now = datetime.now()
    curr_date = now.strftime("%Y/%m/%d-%H:%M:%S")
    # https://stackoverflow.com/questions/107705/disable-output-buffering/107717
    print(f"{Fore.YELLOW}{curr_date} -> Hello daily from {sys.platform}", flush=True)


if __name__ == "__main__":
    logging.basicConfig()
    # logging.getLogger("apscheduler").setLevel(logging.DEBUG)
    # logging.getLogger("apscheduler").setLevel(logging.INFO)

    sched = BackgroundScheduler(daemon=True)
    sched.add_job(hello, "interval", seconds=10)
    sched.add_job(hello_daily, "cron", hour="3", minute="0", day="*")
    for job in sched.get_jobs():
        print(job)
    sched.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown()
