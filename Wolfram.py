#!/usr/bin/python3

#Code written by 
#       _          _   __
#  ___ | |_  _ __ / | / _|  ___
# / __|| __|| '__|| || |_  / _ \
# \__ \| |_ | |   | ||  _||  __/
# |___/ \__||_|   |_||_|   \___|
#

# Простая реализациия элементарных клеточных автоматов с применением ООП.
# Использование: создаете экземлпяр класса WolframCA с аргументами 
# rule - Десятичное представление кода Вольфрама (int от 0 до 255) 
# height - Количество итераций автомата (int от 1 до inf)
# width - Количество клеток в одной строке автомата (int от 1 до inf)
# Далее запускаете метод run() 
#
# Пример:
#
#   rule101 = WolframCA(101, 500, 500)
#   rule101.run()
#
# Примечание: правила строятся на случайной конфигурации


import numpy as np
import matplotlib.pyplot as plt

class WolframCA:
    def __init__(self, rule: int, height: int, width: int) -> None:
        self.rule = rule
        self.height = height
        self.width = width

        self.rule_2 = None
        self.prev_state = None
        self.initial_state = None
        

    def set_rule(self) -> str:
        num = str(bin(self.rule))
        if (len(num) - 2) < 8:
            missing = 8 - (len(num) - 2)
            num = '0' * missing + num[2:]
            return num
        
        else:
            num = num[2:]
            return num
    
    def get_rule(self) -> None:
        self.rule_2 = self.set_rule()

    def set_initial_state(self) -> np.ndarray:
        return np.random.randint(2, size=self.width)

    def get_initial_state(self) -> None:
        self.initial_state = self.set_initial_state()

    def read_state(self, prev: int, nxt: int, curr: int) -> int:
        if prev == 1 and curr == 1 and nxt == 1:
            return int(self.rule_2[0])
        elif prev == 1 and curr == 1 and nxt == 0:
            return int(self.rule_2[1])
        elif prev == 1 and curr == 0 and nxt  == 1:
            return int(self.rule_2[2])
        elif prev == 1 and curr == 0 and nxt  == 0:
            return int(self.rule_2[3])
        elif prev == 0 and curr == 1 and nxt == 1:
            return int(self.rule_2[4])
        elif prev == 0 and curr == 1 and nxt == 0:
            return int(self.rule_2[5])
        elif prev == 0 and curr == 0 and nxt == 1:
            return int(self.rule_2[6])
        else:
            return int(self.rule_2[7])

    def get_new_state(self, i) -> np.ndarray:
        new_state = np.zeros((1, self.width))[0]
        if i == 0:
            self.prev_state = self.initial_state
        for j in range(self.width):
            if j == 0:
                new_state[j] = self.read_state(0, self.prev_state[j+1], self.prev_state[j])
            elif j == self.width - 1:
                new_state[j] = self.read_state(self.prev_state[j-1], 0, self.prev_state[j])
            else:
                new_state[j] = self.read_state(self.prev_state[j-1], self.prev_state[j+1], self.prev_state[j])
        self.prev_state = new_state

        return new_state

    def draw_config(self, matr) -> None:
        plt.imshow(matr, cmap="Greys", interpolation="nearest")
        plt.show()


    def run(self) -> None:
        self.get_rule()
        self.get_initial_state()

        config = self.initial_state 
        for i in range(self.height):
            new_state = self.get_new_state(i)
            config = np.vstack((config, new_state))
        
        self.draw_config(config)


if __name__ == "__main__":
    rule101 = WolframCA(30, 300, 300)
    rule101.run()
