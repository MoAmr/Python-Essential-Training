# A class is the basis ofall data in Python.


class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck'

    # You'll notice that the first parameter of a method is always self.
    # Self is not a keyword. Yo can actually name that first parameter whatever you want to,
    # but self is traditional and recommended so that as people are reading your code,
    # they know what you're talking about.
    # Self here is a reference to the object, not the class.

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


def main():
    donald = Duck()
    donald.quack()
    donald.move()


if __name__ == '__main__': main()
