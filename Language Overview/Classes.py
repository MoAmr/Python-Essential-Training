# Objects in Python


class Duck:
    sound = 'Quaaaaack!'
    walking = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def main():
    donald = Duck()
    donald.quack()
    donald.walk()


if __name__ == '__main__': main()
