score = int(input('Enter a score between 0 and 100: '))

# Conditional / Ternary
is_top_score = True if score >= 90 else False
print('is_top_score: ', is_top_score)

# nested Ternary
temp = int(input('Enter a temperature in celsius between 0 and 40: '))
weather = 'hot' if temp > 25 else ('mild' if temp > 15 else 'cold')
print(f'weather is: {weather}')

user_input = ''
while user_input != 'q':
    user_input = input('Enter a letter or q to quit: ')
    print('You entered: ', user_input)