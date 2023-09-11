#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        the_tuple = (0, None)
    else:
        the_tuple = (len(sentence), sentence[:1])
    return(the_tuple)
