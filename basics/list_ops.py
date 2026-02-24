# =============================================================================
# LIST OPERATIONS DEMONSTRATION - FUNCTIONAL APPROACH
# =============================================================================
# This file demonstrates various list operations in Python using modular functions.
# Each operation is encapsulated in its own function for better organization and reusability.

def demonstrate_basic_list_operations():
    """
    Demonstrates basic list setup and accessing elements.
    Covers: creating lists, copying, sorting, and accessing elements by index.
    """
    print("\n" + "="*60)
    print("1. BASIC LIST SETUP AND ACCESSING ELEMENTS")
    print("="*60)

    # Original list of colors
    original_colors = ['red', 'green', 'blue', 'yellow', 'purple', 'magenta', 'cyan', 'white', 'black']
    print(f"Original colors list: {original_colors}")

    # Create a copy and sort it
    colors = original_colors.copy()
    colors.sort()
    print(f"Sorted colors list: {colors}")

    # Accessing individual elements
    print("\n--- Accessing List Elements ---")
    print(f"First element (index 0): {colors[0]}")
    print(f"Second element with title case: {colors[1].title()}")
    print(f"Last element (index -1): {colors[-1]}")
    print(f"Second last element (index -2): {colors[-2]}")
    print(f"Third last element (index -3): {colors[-3]}")
    print(f"Length of list: {len(colors)}")
    print(f"Second last element using len(): {colors[len(colors)-2]}")

    # String formatting with list elements
    c = f"The color is {colors[1].title()}"
    print(f"Formatted string: {c}")

    return colors  # Return the colors list for use in other functions


def demonstrate_modifying_elements(colors):
    """
    Demonstrates modifying list elements.
    Covers: changing elements by index, appending, and inserting.
    """
    print("\n" + "="*60)
    print("2. MODIFYING LIST ELEMENTS")
    print("="*60)

    # Modifying an element by index
    colors[1] = 'yellow'
    print(f"After modifying index 1 to 'yellow': {colors}")

    # Adding elements to the list
    print("\n--- Adding Elements ---")
    colors.append('purple')
    print(f"After appending 'purple': {colors}")

    colors.insert(1, 'magenta')
    print(f"After inserting 'magenta' at index 1: {colors}")

    return colors


def demonstrate_removing_elements(colors):
    """
    Demonstrates removing elements from lists.
    Covers: del, pop(), and remove() methods.
    """
    print("\n" + "="*60)
    print("3. REMOVING ELEMENTS FROM LISTS")
    print("="*60)

    # Deleting using del statement
    print("\n--- Removing Elements ---")
    print(f"Current list before deletion: {colors}")
    del colors[1]
    print(f"After deleting element at index 1: {colors}")

    # Removing using pop() method (removes and returns the last element by default)
    removed_color = colors.pop()
    print(f"After popping last element: {colors}")
    print(f"Removed color: {removed_color}")

    # Removing using pop() with specific index
    removed_color = colors.pop(1)
    print(f"After popping element at index 1: {colors}")
    print(f"Removed color from index 1: {removed_color}")

    # Removing using remove() method (removes first occurrence of a value)
    colors.remove('magenta')  # The remove() method deletes only the first occurrence of the value you specify
    print(f"After removing 'magenta': {colors}")

    return colors


def demonstrate_sorting_reversing(colors):
    """
    Demonstrates sorting and reversing lists.
    Covers: sort(), sort(reverse=True), sorted(), and reverse().
    """
    print("\n" + "="*60)
    print("4. SORTING AND REVERSING LISTS")
    print("="*60)

    print(f"List before sorting: {colors}")

    # Sorting in ascending order
    colors.sort()
    print(f"After sort() (ascending): {colors}")

    # Sorting in descending order
    colors.sort(reverse=True)
    print(f"After sort(reverse=True) (descending): {colors}")

    # Using sorted() function (returns new list, original unchanged)
    sorted_colors = sorted(colors)
    print(f"Original list after sorted(): {colors}")
    print(f"New sorted list: {sorted_colors}")

    # Reversing the list
    colors.reverse()
    print(f"After reverse(): {colors}")

    return colors


def demonstrate_looping_lists(colors):
    """
    Demonstrates looping through lists.
    Covers: simple loops, loops with index, and practical examples.
    """
    print("\n" + "="*60)
    print("5. LOOPING THROUGH LISTS")
    print("="*60)

    print("\n--- Simple Loop Through Colors ---")
    for color in colors:
        print(f"  - {color.title()}")

    print("\n--- Loop Through Colors with Index ---")
    for i in range(len(colors)):
        print(f"  Index {i}: {colors[i].title()}")

    print("\n--- Magic Show Example ---")
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(f"  {magician.title()}, that was a great trick!")
        print(f"  I can't wait to see your next trick, {magician.title()}.")

    print("\nThank you, everyone. That was a great magic show!")


def demonstrate_numerical_lists():
    """
    Demonstrates working with numerical lists.
    Covers: range(), creating lists with range, list statistics, and loops.
    """
    print("\n" + "="*60)
    print("6. WORKING WITH NUMERICAL LISTS")
    print("="*60)

    # Using range() function
    print("\n--- Using range() Function ---")
    print("Numbers from 1 to 4:")
    for value in range(1, 5):
        print(f"  {value}")

    # Creating lists with range()
    print("\n--- Creating Lists with range() ---")
    even_numbers = list(range(2, 11, 2))
    print(f"Even numbers from 2 to 10: {even_numbers}")

    # Creating squares list with loop
    print("\n--- Creating Squares List with Loop ---")
    squares = []
    for value in range(1, 11):
        square = value ** 2
        squares.append(square)
    print(f"Squares of numbers 1-10: {squares}")

    # List statistics
    print("\n--- List Statistics ---")
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(f"Digits list: {digits}")
    print(f"Minimum value: {min(digits)}")
    print(f"Maximum value: {max(digits)}")
    print(f"Sum of all values: {sum(digits)}")


def demonstrate_list_comprehensions():
    """
    Demonstrates list comprehensions.
    Covers: concise list creation using comprehension syntax.
    """
    print("\n" + "="*60)
    print("7. LIST COMPREHENSIONS")
    print("="*60)

    # List comprehension technique - creating cubes
    print("\n--- List Comprehension Example ---")
    cubes = [value ** 3 for value in range(1, 11)]
    print(f"Cubes of numbers 1-10 using list comprehension: {cubes}")
    print("Note: This is equivalent to a for loop but more concise!")


def demonstrate_list_slicing():
    """
    Demonstrates list slicing operations.
    Covers: various slicing techniques and looping through slices.
    """
    print("\n" + "="*60)
    print("8. LIST SLICING")
    print("="*60)

    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(f"Original players list: {players}")

    print("\n--- Different Slicing Examples ---")
    print(f"players[0:3] (first 3 players): {players[0:3]}")
    print(f"players[1:4] (players 2-4): {players[1:4]}")
    print(f"players[:4] (from start to index 3): {players[:4]}")
    print(f"players[2:] (from index 2 to end): {players[2:]}")
    print(f"players[-3:] (last 3 players): {players[-3:]}")

    # Looping through a slice
    print("\n--- Looping Through a Slice ---")
    print("Here are the first three players on my team:")
    for player in players[:3]:
        print(f"  - {player.title()}")


def demonstrate_copying_lists():
    """
    Demonstrates copying lists.
    Covers: creating true copies vs references.
    """
    print("\n" + "="*60)
    print("9. COPYING LISTS")
    print("="*60)

    # Creating a copy of a list
    print("\n--- List Copying Example ---")
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]  # This creates a true copy, not a reference

    print("My favorite foods are:")
    for food in my_foods:
        print(f"  - {food.title()}")

    print("\nMy friend's favorite foods are:")
    for food in friend_foods:
        print(f"  - {food.title()}")

    print("\nNote: Using [:] creates a separate copy, so modifying one list doesn't affect the other.")


def main():
    """
    Main function that orchestrates all list operation demonstrations.
    Calls each function in sequence to showcase all list operations.
    """
    print("="*80)
    print("LIST OPERATIONS DEMONSTRATION - FUNCTIONAL APPROACH")
    print("="*80)
    print("This program demonstrates various list operations using modular functions.")

    # Start with basic operations and get the colors list
    colors = demonstrate_basic_list_operations()

    # Modify the list elements
    colors = demonstrate_modifying_elements(colors)

    # Remove elements from the list
    colors = demonstrate_removing_elements(colors)

    # Sort and reverse the list
    colors = demonstrate_sorting_reversing(colors)

    # Demonstrate looping
    demonstrate_looping_lists(colors)

    # Demonstrate numerical list operations
    demonstrate_numerical_lists()

    # Demonstrate list comprehensions
    demonstrate_list_comprehensions()

    # Demonstrate list slicing
    demonstrate_list_slicing()

    # Demonstrate copying lists
    demonstrate_copying_lists()

    # End of demonstration
    print("\n" + "="*60)
    print("LIST OPERATIONS DEMONSTRATION COMPLETE!")
    print("="*60)


# Run the demonstration if this file is executed directly
if __name__ == "__main__":
    main()