from dateutil.relativedelta import relativedelta
from datetime import datetime

def solution(today, terms, privacies):
    terms_dict = {}
    for i in terms:
        term,period = i.split()
        terms_dict[term] = period
    answer = []
    for i in range(len(privacies)):
        register_date, type1 = privacies[i].split()
        x =(datetime.strptime(register_date ,'%Y.%m.%d')+relativedelta(months =int(terms_dict[type1]))).strftime('%Y.%m.%d')   
        if today >= x:
            answer.append(i+1)
    return answer