import numpy as np

def are_vectors_intersecting(vec1, vec2):
    """
    Check if two vectors with XYZ coordinates are intersecting.
    """
    dot_product = np.dot(vec1, vec2)
    return dot_product == 0

# Example usage
vec1 = np.array([19.58])
vec2 = np.array([22.57,13.18])


print(are_vectors_intersecting(vec1, vec2))  # False
print(are_vectors_intersecting(vec1, vec3))  # True
