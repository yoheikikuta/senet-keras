import numpy as np
from scipy.misc import imresize


def arr_resize(arr, size):
    '''
    Resize Colored image array.
    '''
    resized_arr = np.empty((arr.shape[0],size,size,3))
    for idx, elem in enumerate(arr):
        resized_arr[idx] = imresize(elem, (size,size,3), interp='bilinear')

    return resized_arr
