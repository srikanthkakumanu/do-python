belt_color = input('What is your belt color: ')

match belt_color:
    case 'white':
        award = 'Ninja Fledgling'
    case 'red':
        award = 'Intermediate Ninja'
    case 'blue':
        award = 'Advanced Ninja'
    case 'purple':
        award = 'Pro Ninja'
    case 'black':
        award = 'Master Ninja'
    case _:
        award = 'Unknown Belt Color'

print(award)
