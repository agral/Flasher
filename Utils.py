#!/usr/bin/env python3


def import_CSV_data_from_file(filename, separator=",", comment_token=None):
    """Reads the provided file line-by-line, importing the data it contains.

    params:
        filename - a string representing the path to the CSV file.
        separator - a character to be used as a separator token.
        comment_token - a character to be used as a comment token (optional).

    throws:
        RuntimeError if the file is malformed.

    The file should have the following structure:
      * Every line must have exactly the same number of fields N,
        separated by (N-1) instances of a separator,
      * If comment character has been specified, everything from the beginning
        of a comment character to the end of line is treated as a comment
        and not processed.
    """

    result = []
    assumed_separators_count = None
    line_number = 0

    with open(filename, "r") as csv_file:
        for line in csv_file:
            line_number += 1

            # Removes the comment (if applicable),
            # then strips the raw line of all the prefixing/trailing whitespace:
            line = line.split(comment_token)[0].strip()

            if len(line) > 0:
                # Checks file sanity: the number of separators in this line
                # has to match the number of separators seen in the previous lines:
                separators_count = line.count(separator)
                if separators_count != assumed_separators_count:
                    if assumed_separators_count == None:
                        assumed_separators_count = separators_count
                    else:
                        msg = "File {} in line #{}: Wrong number of ".format(
                                filename, line_number)
                        msg += "separators (expected: {}, got: {}).".format(
                                assumed_separators_count, separators_count)
                        raise RuntimeError(msg)
                fields = line.split(separator)
                print(fields)
                result.append(fields)
    return result
