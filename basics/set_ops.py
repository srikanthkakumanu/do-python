def demonstrate_set_operations():
    """
    Demonstrates set operations.
    Covers: union, intersection, difference, symmetric difference.
    """
    print("\n" + "="*60)
    print("9. SET OPERATIONS")
    print("="*60)

    # Set union
    print("\n--- Set Union Example ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union of Set A and Set B: {set_a | set_b}")

    # Set intersection
    print("\n--- Set Intersection Example ---")
    print(f"Intersection of Set A and Set B: {set_a & set_b}")

    # Set difference
    print("\n--- Set Difference Example ---")
    print(f"Difference of Set A - Set B: {set_a - set_b}")
    print(f"Difference of Set B - Set A: {set_b - set_a}")

    # Set symmetric difference
    print("\n--- Set Symmetric Difference Example ---")
    print(f"Symmetric Difference of Set A and Set B: {set_a ^ set_b}")


    # Set operations using set() function
    print("\n--- Set Operations using set() Function Example ---")
    set_a = {1, 2, 3}
    set_b = set([2, 3, 4])
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union of Set A and Set B: {set_a | set_b}")
    print(f"Intersection of Set A and Set B: {set_a & set_b}")
    print(f"Difference of Set A - Set B: {set_a - set_b}")
    print(f"Difference of Set B - Set A: {set_b - set_a}")
    print(f"Symmetric Difference of Set A and Set B: {set_a ^ set_b}")


    # Using union() method
    print("\n--- Set Union Example using union() method ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union of Set A and Set B using union() method: {set_a.union(set_b)}")


    # Using intersection() method
    print("\n--- Set Intersection Example using intersection() method ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Intersection of Set A and Set B using intersection() method: {set_a.intersection(set_b)}")

    # Using difference() method
    print("\n--- Set Difference Example using difference() method ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Is Set A and Set B difference: {set_a.difference(set_b)}")
    print(f"Is Set B and Set A difference: {set_b.difference(set_a)}")

    # Using intersection_update() method
    print("\n--- Set Intersection Update Example using intersection_update() method ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    set_a.intersection_update(set_b)
    print(f"Updated Set A using intersection_update() method: {set_a}")


    # Using discard() method
    print("\n--- Set Discard Example using discard() method ---")
    set_a = {1, 2, 3}
    print(f"Set A: {set_a}")
    set_a.discard(2)
    print(f"Updated Set A using discard() method: {set_a}")

    # Using remove() and discard() methods
    print("\n--- Set Remove and Discard Example ---")
    set_a = {1, 2, 3}
    print(f"Set A: {set_a}")
    try:
        set_a.remove(2)  # remove() method will raise an exception if the element is not found
        print(f"Updated Set A using remove() method: {set_a}")
    except KeyError:
        print("Element not found in the set. Using remove() method will raise an exception.")
    set_a.discard(2)  # discard() method will do nothing if the element is not found
    print(f"Updated Set A using discard() method: {set_a}")
    # Using difference_update() method
    print("\n--- Set Difference Update Example using difference_update() method ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Is Set A and Set B difference_update: {set_a.difference_update(set_b)}")

    # Using isdisjoint() method
    print("\n--- Set Disjoint Example using isdisjoint() method ---")
    set_a = {1, 2, 3}
    set_b = {4, 5, 6}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Is Set A and Set B disjoint: {set_a.isdisjoint(set_b)}")

    # Using symmetric_difference() method
    print("\n--- Set Symmetric Difference Example using symmetric_difference() method ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Symmetric Difference of Set A and Set B using symmetric_difference() method: {set_a.symmetric_difference(set_b)}")

    # Using symmetric_difference_update() method
    print("\n--- Set Symmetric Difference Update Example using symmetric_difference_update() method ---")
    set_a = {1, 2, 3}
    set_b = {2, 3, 4}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    set_a.symmetric_difference_update(set_b)
    print(f"Updated Set A using symmetric_difference_update() method: {set_a}")

    # Using frozenset() to create a frozen (immutable) set
    print("\n--- Frozen Set Example ---")
    mutable_set = {1, 2, 3}
    print(f"Mutable Set: {mutable_set}")
    frozen_set = frozenset(mutable_set)
    print(f"Frozen Set: {frozen_set}")
    try:
        frozen_set.add(4)  # Attempting to modify the frozen set will raise an exception
    except AttributeError as e:
        print(f"Error: {e}")


def main():
    """
    Main method to demonstrate set operations.
    """
    demonstrate_set_operations()


if __name__ == "__main__":
    main()