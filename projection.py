import numpy as np

def project_3d_to_2d(points_3d, focal_length=500, center_x=320, center_y=240):
    """Rudimentary perspective projection."""
    points_2d = []
    for x, y, z in points_3d:
        if z <= 0:  # Avoid division by zero and objects behind the camera
            continue
        u = int(focal_length * x / z + center_x)
        v = int(focal_length * y / z + center_y)
        points_2d.append((u, v))
    return np.array(points_2d, dtype=np.int32)
#
# def rotate_points(points, angles, center):
#     """
#     Rotate points by the given angles (in degrees) around each axis,
#     keeping the shape centered around the specified center point.
#
#     Args:
#         points: Array of 3D points to rotate
#         angles: List/array of rotation angles in degrees [x_angle, y_angle, z_angle]
#         center: Center point [x, y, z] to rotate around
#
#     Returns:
#         Array of rotated points
#     """
#     # Convert angles to radians
#     angles_rad = np.radians(angles)
#
#     # Convert center to numpy array if it's not already
#     center = np.array(center)
#
#     # Step 1: Translate points to origin (subtract center)
#     centered_points = points - center
#
#     # Step 2: Create rotation matrices
#     # Rotation around X-axis
#     rx = np.array([
#         [1, 0, 0],
#         [0, np.cos(angles_rad[0]), -np.sin(angles_rad[0])],
#         [0, np.sin(angles_rad[0]), np.cos(angles_rad[0])]
#     ])
#
#     # Rotation around Y-axis
#     ry = np.array([
#         [np.cos(angles_rad[1]), 0, np.sin(angles_rad[1])],
#         [0, 1, 0],
#         [-np.sin(angles_rad[1]), 0, np.cos(angles_rad[1])]
#     ])
#
#     # Rotation around Z-axis
#     rz = np.array([
#         [np.cos(angles_rad[2]), -np.sin(angles_rad[2]), 0],
#         [np.sin(angles_rad[2]), np.cos(angles_rad[2]), 0],
#         [0, 0, 1]
#     ])
#
#     # Combined rotation matrix: R = Rz * Ry * Rx
#     r = rz @ ry @ rx
#
#     # Apply rotation to centered points
#     rotated_centered_points = np.dot(centered_points, r.T)
#
#     # Step 3: Translate back to the original center
#     rotated_points = rotated_centered_points + center
#
#     return rotated_points

def rotate_points(points, angles, center, actual_center=None):
    """
    Rotate points by the given angles (in degrees) around each axis,
    keeping the shape centered around the specified center point.

    Args:
        points: Array of 3D points to rotate
        angles: List/array of rotation angles in degrees [x_angle, y_angle, z_angle]
        center: Center point [x, y, z] to rotate around
        actual_center: Optional parameter to specify the actual centroid of the points if
                       different from the desired center. If None, will compute the centroid.

    Returns:
        Array of rotated points
    """
    # Convert angles to radians
    angles_rad = np.radians(angles)

    # Convert center to numpy array if it's not already
    center = np.array(center)

    # Determine the actual geometric center of the points if not provided
    if actual_center is None:
        actual_center = np.mean(points, axis=0)
    else:
        actual_center = np.array(actual_center)

    # First translate points so that the actual center aligns with the desired center
    offset = center - actual_center
    adjusted_points = points + offset

    # Now proceed with rotation around the desired center
    # Step 1: Translate points to origin
    centered_points = adjusted_points - center

    # Step 2: Create rotation matrices
    # Rotation around X-axis
    rx = np.array([
        [1, 0, 0],
        [0, np.cos(angles_rad[0]), -np.sin(angles_rad[0])],
        [0, np.sin(angles_rad[0]), np.cos(angles_rad[0])]
    ])

    # Rotation around Y-axis
    ry = np.array([
        [np.cos(angles_rad[1]), 0, np.sin(angles_rad[1])],
        [0, 1, 0],
        [-np.sin(angles_rad[1]), 0, np.cos(angles_rad[1])]
    ])

    # Rotation around Z-axis
    rz = np.array([
        [np.cos(angles_rad[2]), -np.sin(angles_rad[2]), 0],
        [np.sin(angles_rad[2]), np.cos(angles_rad[2]), 0],
        [0, 0, 1]
    ])

    # Combined rotation matrix: R = Rz * Ry * Rx
    r = rz @ ry @ rx

    # Apply rotation to centered points
    rotated_centered_points = np.dot(centered_points, r.T)

    # Step 3: Translate back to the desired center
    rotated_points = rotated_centered_points + center

    return rotated_points