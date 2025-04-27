# console_runner.py

from practical_1 import run_practical_1
from practical_2 import run_practical_2
from practical_3 import run_practical_3
from practical_4 import run_practical_4
from practical_5 import run_practical_5
from practical_6 import run_practical_6
from practical_7 import run_practical_7
from practical_8 import run_practical_8
from practical_9 import run_practical_9
from practical_10 import run_practical_10

def run_practical(practical_number):
    try:
        if practical_number == 1:
            run_practical_1()
        elif practical_number == 2:
            run_practical_2()
        elif practical_number == 3:
            run_practical_3()
        elif practical_number == 4:
            run_practical_4()
        elif practical_number == 5:
            run_practical_5()
        elif practical_number == 6:
            run_practical_6()
        elif practical_number == 7:
            run_practical_7()
        elif practical_number == 8:
            run_practical_8()
        elif practical_number == 9:
            run_practical_9()
        elif practical_number == 10:
            run_practical_10()
        else:
            print("❌ Invalid practical number.")
    except Exception as e:
        print("⚠️ Error:", e)

