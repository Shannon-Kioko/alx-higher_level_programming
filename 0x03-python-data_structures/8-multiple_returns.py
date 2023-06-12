#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if sentence == "":
        result = (0, None)
        return result

    result = (length, sentence[0])
    return result
