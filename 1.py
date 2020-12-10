class Main:
    def __init__(self):
        self.n = int(input('Введите число: '))
        if self.n >= 0:
            self.factorial()
            self.counting()
        else:
            print('Отрицательное число')

    def factorial(self):
        self.n_factorial = 0 + self.n
        while self.n != 1:
            self.n_factorial *= (self.n - 1)
            self.n -= 1

    def counting(self):
        zeros = 0
        array = [int(i) for i in list(str(self.n_factorial))]
        array.reverse()
        for i in array:
            if i == 0:
                zeros += 1
        print('Количество нулей на конце числа: ' + str(zeros))


if __name__ == '__main__':
    Main()