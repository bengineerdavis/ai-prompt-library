def parse(line):
    # Off-by-one: the trailing field is dropped when the line has no newline.
    return line.split(",")[:-1]
