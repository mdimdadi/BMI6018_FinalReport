'''
This module contains a function that will create a dictionary

'''



def make_dictionary(keys, values):

    '''
    This function will take two arguments
    Both arguments will be lists
    The function will return a dictionary containing keys from keys list and values from values list

    '''
    dictionary = {}
    keys = [ddf.get_value(ddf.index[0], 'Month') for ddf in keys]
    for k, val_a in zip(keys, values): #zip is used to iterate over two lists simultaneously!
        dictionary[k] = val_a
    return dictionary
