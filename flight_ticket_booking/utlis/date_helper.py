import datetime


class DateHelper(object):
    @classmethod
    def next_weekday(cls, date):
        weekday = date.weekday()
        if weekday < 5:
            return date
        else:
            return date + datetime.timedelta(days=7 - weekday)

    @classmethod
    def next_weekend(cls, date):
        weekday = date.weekday()
        if weekday > 4:
            return date
        else:
            return date + datetime.timedelta(days=5 - weekday)

    @classmethod
    def prev_weekday(cls, date):
        weekday = date.weekday()
        if weekday < 5:
            return date
        else:
            return date + datetime.timedelta(days=4 - weekday)

    @classmethod
    def prev_weekend(cls, date):
        weekday = date.weekday()
        if weekday > 4:
            return date
        else:
            return date + datetime.timedelta(days=-1 - weekday)
