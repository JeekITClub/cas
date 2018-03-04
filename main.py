import random
import numpy as np
import tensorflow
import matplotlib.pyplot as plt


class Student:
    def __init__(self, choice):
        self.choice = choice
        self.policy_class = 0


student_list = []


def transform(student):
    s = student
    if s.choice == [1, 1, 1, 0, 0, 0]:
        return 1
    elif s.choice == [1, 1, 0, 1, 0, 0]:
        return 2
    elif s.choice == [1, 1, 0, 0, 1, 0]:
        return 3


class PolicyClassroom:
    def __init__(self, class_num):
        self.student = np.zeros(20)
        self.class_num = class_num

    def add_student(self, choice):
        self.student[choice] += 1

    def diversity(self):
        sum = 0.0
        for choice in self.student:
            sum += choice
        diversity = 0.0
        for choice in self.student:
            diversity += choice ** 2 / sum ** 2
        return diversity


class LearningClassroom:
    def __init__(self):
        pass


class QLearning:

    def __init__(self):
        pass


class1 = PolicyClassroom(1)
diversity_list = []
for i in range(1, 40):
    choice = random.randint(1, 20) - 1
    print(choice)
    class1.add_student(choice)
    diversity_list.append(class1.diversity())
    print(class1.diversity())
    # plt.subplot(2,1,1)

plt.plot(np.linspace(0, 39, 39), diversity_list)
plt.title('Diversity')
plt.show()
