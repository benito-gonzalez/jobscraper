from _datetime import datetime
from pytz import timezone


ERRORFILE = "errors.log"
zone = "Europe/Helsinki"


def get_formatted_date():
    date = datetime.now(timezone(zone)).strftime("%d-%m-%Y %H:%M:%S")
    return "[" + date + "]\t"


def set_company_not_found(company_name):
    f = open(ERRORFILE, 'a')
    f.write(get_formatted_date() + "Company can not be retrieved from DB. '" + company_name + "' does not exist\n")
    f.close()


def set_invalid_request(url, e):
    f = open(ERRORFILE, 'a')
    f.write(get_formatted_date() + "Error during requests to {0} : {1}".format(url, str(e)) + "\n")
    f.close()


def set_invalid_response(url):
    f = open(ERRORFILE, 'a')
    f.write(get_formatted_date() + "Error during response from{0}".format(url) + "\n")
    f.close()
