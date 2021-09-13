import datetime

inp = '1999-11-03'
required = '%Y-%m-%d'
if not datetime.datetime.strptime(inp, required):
    print("yes")
else:
    print("no")