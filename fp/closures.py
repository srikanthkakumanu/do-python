# A closure is a function that remember values from its enclosing scope

def counter(start=0):  # higher order function
    count = start

    def increment():  # inner function
        nonlocal count  # retains access to 'count' even after counter() ends
        count += 1
        return count

    return increment  # returns the inner function

def move_factory(character_name):
    uppercase_name = character_name.upper()
    def print_move(move_name):
        print(f'{uppercase_name} performs {move_name}!')
    return print_move

def main():
    # Example-1
    counter1 = counter(5)  # closure retains count = 5
    print(counter1())
    print(counter1())

    counter2 = counter(10)  # new closure with count = 10
    print(counter2())

    # Example-2
    the_move = move_factory('Ryu') # it remembers the RYU uppercase even after completion of enclosing scope execution
    the_move('Sweeping Slash')


if __name__ == "__main__":
    main()