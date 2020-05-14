from threading import Thread

class MyExam:

    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("Q1 solved")
    def q2(self):
        print("Q2 solved")
    def q3(self):
        print("Q3 solved")

mye = MyExam()
t = Thread(target=mye.solve_question)
t.start()
