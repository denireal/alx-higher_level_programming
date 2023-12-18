#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    division_results = []

    for i in range(list_length):
        try:
            # Check if indices are within the range of both lists
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            # Attempt division
            div = my_list_1[i] / my_list_2[i]

            # Append result to division_results
            division_results.append(div)

        except (TypeError, ValueError):
            print("wrong type")
            division_results.append(0)
        except ZeroDivisionError:
            print("division by 0")
            division_results.append(0)
        except IndexError:
            print("out of range")
            division_results.append(0)

    return division_results
