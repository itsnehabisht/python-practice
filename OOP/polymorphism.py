class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img

    def shownum(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(4, 7)
num1.shownum()

num2 = Complex(6, 4)
num2.shownum()

num3 = num1 + num2
num3.shownum()