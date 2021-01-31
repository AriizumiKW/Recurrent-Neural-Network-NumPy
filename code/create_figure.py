import matplotlib.pyplot as plt
import re
import numpy as np


def q2_loss():
    data = open('data_q2.txt')
    x = []
    y = []
    for line in data:
        y.append(round(float(re.split(' ', line)[-1][:-1]), 2))
        x.append(re.split(' ', line)[1][:-1])
    plt.plot(list(range(0, len(y))), y, label='q2_loss')
    plt.legend()
    plt.savefig('./q2_loss.pdf')


def q3_loss():
    data = open('data_q3.txt')
    x = []
    y = []
    for line in data:
        y.append(round(float(re.split('  ', line)[5][10:]), 2))
        x.append(re.split(' ', line)[1][:-1])
    plt.plot(x, y, label='q3_loss')
    plt.xticks(range(0, 51, 5))
    plt.legend()
    plt.savefig('./q3_loss.pdf')


def q3_acc():
    data = open('data_q3.txt')
    x = []
    y = []
    for line in data:
        y.append(round(float(re.split(' ', line)[-1][:-1]), 2))
        x.append(re.split(' ', line)[1][:-1])
    plt.plot(x, y, label='q3_loss')
    plt.xticks(range(0, 51, 5))
    plt.legend()
    plt.savefig('./q3_acc.pdf')


q2_loss()
