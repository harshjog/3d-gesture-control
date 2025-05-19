import numpy as np

def create_specific(n, center, size, resolution = 50):
    if n == 0:
        points = create_sphere(center, size, resolution)
        return points[:, 0], points[:, 1], points[:, 2]  # Return x, y, z
    elif n == 1:
        points = create_dense_cube_edges(center, size, resolution)
        return points[:, 0], points[:, 1], points[:, 2]  # Return x, y, z
    else:
        print("please enter valid input")
        return None, None, None  # Or handle the error differently

# Define all 3D object functions here
def create_sphere(center, size, resolution):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    x = size * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = size * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = size * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
    points = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=-1)
    return points

def create_dense_cube_edges(center, size, resolution):
    """
    Generates a denser set of points by sampling along the edges of a cube.

    Args:
        center (numpy.ndarray): Center of the cube [x, y, z].
        size (float): Side length of the cube.
        resolution (int): Number of points to sample along each edge (including endpoints).

    Returns:
        numpy.ndarray: An array of shape (num_points, 3) containing the coordinates of the sampled points.
    """
    x_c, y_c, z_c = center
    half_size = size / 2.0

    # 8 vertices of the cube
    vertices = np.array([
        [x_c - half_size, y_c - half_size, z_c - half_size], # 0
        [x_c + half_size, y_c - half_size, z_c - half_size], # 1
        [x_c + half_size, y_c + half_size, z_c - half_size], # 2
        [x_c - half_size, y_c + half_size, z_c - half_size], # 3
        [x_c - half_size, y_c - half_size, z_c + half_size], # 4
        [x_c + half_size, y_c - half_size, z_c + half_size], # 5
        [x_c + half_size, y_c + half_size, z_c + half_size], # 6
        [x_c - half_size, y_c + half_size, z_c + half_size]  # 7
    ])

    # Define the 12 edges by the vertex indices
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0), # Bottom face
        (4, 5), (5, 6), (6, 7), (7, 4), # Top face
        (0, 4), (1, 5), (2, 6), (3, 7)  # Connecting edges
    ]

    all_points = []
    num_samples = resolution

    for start_index, end_index in edges:
        start_point = vertices[start_index]
        end_point = vertices[end_index]

        # Interpolate points along the edge
        for i in range(num_samples):
            fraction = i / (num_samples - 1) if num_samples > 1 else 0.5 # Avoid division by zero
            point = start_point + fraction * (end_point - start_point)
            all_points.append(point)

    return np.array(all_points)

def create_coordinate_axes(center, length=100):
    """Create coordinate axes (x, y, z) for visualization."""
    x_axis = np.array([[center[0], center[1], center[2]],
                       [center[0] + length, center[1], center[2]]])
    y_axis = np.array([[center[0], center[1], center[2]],
                       [center[0], center[1] + length, center[2]]])
    z_axis = np.array([[center[0], center[1], center[2]],
                       [center[0], center[1], center[2] + length]])
    return x_axis, y_axis, z_axis

