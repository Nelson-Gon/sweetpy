def extractor(my_list: list, *elem: int) -> int:
    """
    Return the index and count given a list.
    If several indices, the first index is returned.
    :param my_list: A list
    :param elem: Integers(for now).
    """
    [[print("Element: ", elem,
            "Index: ", my_list.index(elem),
            "Count: ", my_list.count(elem),
            end="\n")
      for elem in elem]]

