def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # Handle division by zero
        return None
    except Exception as e:
        # Handle other exceptions
        print("Exception:", e)
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Finally: Inside result block")
