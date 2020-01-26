# Lists and Tuples in Python.
# Note: Lists are mutable and tuples are not.

def main():
    list_game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    list_tuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    # print(', '.join(game))
    # print(len(game))
    # del game[1:3]
    # del game[1:5:2]
    # game.pop()
    # game.pop(3)
    # game.remove('Paper')
    # game.insert(0, 'Computer')
    # game.append('Computer')
    # print(game[i])
    # print(game[1:5:2])
    print_list(list_game)
    print_list(list_tuple)


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()
