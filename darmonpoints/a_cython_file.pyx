from sage.all import ZZ
cimport cython

cpdef cython_test():
    cdef int i=0
    for i in range(10):
        pass
    return 123
