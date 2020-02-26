from libc.math cimport pow

cdef extern from "lib.so":
    void print_bits(unsigned char c)

cpdef print_result ():
    """This is a cpdef function that can be called from Python."""
    print_bits('c')