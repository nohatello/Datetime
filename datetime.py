import datetime
def datize(year,month,day):
    state = None
    try:
        datize = datetime.date(year,month,day)
        state = True
    except:
        state = False
    return state
# for example:
print(datize(2008,8,9))