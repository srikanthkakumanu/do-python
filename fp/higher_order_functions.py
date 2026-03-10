# Higher Order Functions
# A higher order function either takes a function as a argument or returns a function or both.
# It makes code more modular, reusable
def ninja_action(action, x): # higher order function: it takes a function as argument i.e. action
    return action('ninja', x)

def attack(character, x):
    return f'The {character} attacks with the strength of {x}'

def defend(character, x):
    return f'The {character} defends with a block power of {x}'

action_one = ninja_action(attack, 5)
action_two = ninja_action(defend, 7)
print(action_one, action_two)
