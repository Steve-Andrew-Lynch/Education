

aList = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['X', 'S', 'O', 'B']]

def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    column_list = []
    for i in board:
        column_list.append(i[column_index])
    result = str("".join(column_list))

    return result


print(make_str_from_column(aList, 3))


