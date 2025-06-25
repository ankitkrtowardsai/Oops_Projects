def input_is_valid(msg, start=1, end=10):
    while True:
        try:
            val = int(input(msg))
            if val < start or val > end:
                raise ValueError
            return val
        except ValueError:
            print(f"Please enter a number between {start} and {end}.")