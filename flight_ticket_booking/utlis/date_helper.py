class DateHelper(object):
    @classmethod
    def at_weekend(cls, date):
        weekday = date.weekday()
        return weekday > 4
