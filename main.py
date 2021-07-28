import ml
import sys
class main():
    def __init__(self,satisfaction,evaluation,project,hours,timespend,accident,promotion,depart,salary):
        self.satisfaction = satisfaction
        self.evaluation = evaluation
        self.project = project
        self.hours = hours
        self.timespend = timespend
        self.accident = accident
        self.promotion = promotion
        self.depart = depart
        self.salary = salary

def check_promo():
    check = ml.prom
    if ml.prom > 1 or ml.prom < 0:
        print(f"anda memasukkan {check} silahkan ulangi dan pilih 1 atau 0")
        sys.exit()
    else:
        pass


def check_dep():
    check2 = ml.dep
    if ml.dep > 9 or ml.dep < 0:
        print(f"anda memasukkan {check2} silahkan ulangi dan pilih 1 atau 0")
        sys.exit()
    else:
         pass

def check_sal():
    check3 = ml.sal
    if ml.sal > 2 or ml.sal < 0:
        print(f"anda memasukkan {check3} silahkan ulangi dan pilih 1 atau 0")
        sys.exit()
    else:
         pass

print("Hi selamat datang")