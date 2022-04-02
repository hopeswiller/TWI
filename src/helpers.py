from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

date_format_dash = '%Y-%m-%d'
date_format_slash = '%Y/%m/%d'

def main():
    production_date_str = input("Enter Production Date (yyyy-mm-dd): ")
    date_format = find_format(production_date_str)
    production_date = datetime.strptime(production_date_str, date_format).date()
    # production_date = datetime.now().date()

    print(f"production_date = {production_date}")

    expiry_date = calculate_expiry_date(production_date)

    print(f"expiry_date = {expiry_date}")



def calculate_expiry_date(production_date):
    expiry_date = None
    # adding 18months to current date
    expiry_date = (production_date + relativedelta(months=18)) - relativedelta(days=1)
    return expiry_date


def get_date_range(start,end):
    delta = end - start
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days


def find_format(date_str):
    slash_dash = date_str.find('/')
    if slash_dash < 0:
        slash_dash = date_str.find('-')
        return date_format_dash

    return date_format_slash