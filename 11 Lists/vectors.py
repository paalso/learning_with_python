import math

def det2(u, v):
    return u[0] * v[1] - u[1] * v[0]


def det3(u, v, w):
    return u[0] * det2(v[1:], w[1:]) \
        - u[1] * det2((v[0], v[2]), (w[0], w[2])) \
        + u[2] * det2(v[:2], w[:2])


def vector_len(v):
    """ Returns vector's length """
    d = 0
    for e in v:
        d += e * e
    return d ** 0.5


def add_vectors(u, v):
    """ Takes two lists of numbers of the same length, and returns a new list
    containing the sums of the corresponding elements of each """
    result = []
    for i in range(len(u)):
        result.append(u[i] + v[i])
    return result


def scalar_mult(s, v):
    """ Takes a number, s, and a list, v and returns
    the scalar multiple of v by s """
    result = []
    for e in v:
        result.append(s * e)
    return result


def sub_vectors(u, v):
    """ Takes two lists of numbers of the same length, and returns a new list
    containing the substractions of the corresponding elements of each """
    return add_vectors(u, scalar_mult(-1, v))


def dot_product(u, v):
    """ Takes two lists of numbers of the same length, and returns the sum
    of the products of the corresponding elements of each (the dot_product) """
    p = 0
    for i in range(len(u)):
        p += u[i] * v[i]
    return p


def cross_product(u, v):
    """ Takes two lists of numbers of length 3 and
        returns their cross product """
    u_x, u_y, u_z = u
    v_x, v_y, v_z = v
    return [u_y * v_z - u_z * v_y, u_z * v_x - u_x * v_z, u_x * v_y - v_x * u_y]


def get_cosinus_between_vectors(u, v):
    """ Returns cosinus of the angle between two vectors """
    return dot_product(u, v) / (vector_len(v) * vector_len(u))


def get_angle_between_vectors(u, v):
    """ Returns the angle between two vectors """
    return math.acos(dot_product(u, v) / (vector_len(v) * vector_len(u)))
