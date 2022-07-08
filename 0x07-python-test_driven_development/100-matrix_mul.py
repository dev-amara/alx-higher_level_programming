#!/usr/bin/python3
"""Matrix multiplication module"""

def matrix_mul(m_a, m_b):
    """Returns the product of two matrix
        Args:
            m_a (list<list>): A matrix (list of list)
            m_b (list<list>): A matrix (list of list)
        Return: m_a x m_b (the product matrix)
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if not m_a:
        raise ValueError("m_a can't be empty")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not m_b:
        raise ValueError("m_b can't be empty")

    rw_a_len = -1
    cl_a_len = len(m_a)
    for rw_a in m_a:
        if type(rw_a) is not list:
            raise TypeError("m_a must be a list of lists")
        if rw_a_len == -1:
            rw_a_len = len(rw_a)
        if rw_a_len != len(rw_a):
            raise TypeError(
                    "each row of m_a must be of the same size")
        for v_a in rw_a:
            if type(v_a) not in [int, float]:
                raise TypeError(
                        "m_a should contain only integers or floats")
    if rw_a_len == 0:
        raise ValueError("m_a can't be empty")

    rw_b_len = -1
    cl_b_len = len(m_b)
    for rw_b in m_b:
        if type(rw_b) is not list:
            raise TypeError("m_b must be a list of lists")
        if rw_b_len == -1:
            rw_b_len = len(rw_b)
        if rw_b_len != len(rw_b):
            raise TypeError(
                    "each row of m_b must be of the same size")
        for v_b in rw_b:
            if type(v_b) not in [int, float]:
                raise TypeError(
                        "m_b should contain only integers or floats")
    if rw_b_len == 0:
        raise ValueError("m_b can't be empty")

    if rw_a_len == cl_b_len:
        pass
    elif rw_b_len == cl_a_len:
        m_a, m_b = m_b, m_a
        cl_a_len, cl_b_len = cl_b_len, cl_a_len
        rw_a_len, rw_b_len = rw_b_len, rw_a_len
    else:
        raise ValueError("m_a and m_b can't be multiplied")

    m = []
    for rw_a in m_a:
        rw_m = []
        for ci_b in range(len(m_b[0])):
            r = 0
            for ri_b, rw_b in enumerate(m_b):
                v_a = rw_a[ri_b]
                v_b = rw_b[ci_b]
                r += v_a * v_b
            rw_m.append(r)
        m.append(rw_m)

    return m
