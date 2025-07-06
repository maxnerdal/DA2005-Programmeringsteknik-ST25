def read_file(file):
    """
    takes filename as input and returns a list of stripped strings on for each row
    """
    try:
        with open(file, 'r') as infile:
            row_list = [line.strip() for line in infile]
        return row_list
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return []