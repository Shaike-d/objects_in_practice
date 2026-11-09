import classes_for_main_exe.class_Player as p
import classes_for_main_exe.class_Order as o
import classes_for_main_exe.class_BankAccount as b
import classes_for_main_exe.class_User as u

def answers():
    for answer in range(5):
        if answer == 0:
            print("wellcome")
        if answer == 1:
            print("answer 1")
            p.answer_1()
        if answer == 2:
            print("answer 2")
            o.answer_2()
        if answer == 3:
            print("answer 3")
            b.answer_3()
        if answer == 4:
            print("answer 4")
            u.answer_4()
        

