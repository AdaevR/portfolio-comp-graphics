def to_pygame(coords, height, obj_height = 0):
    """Convert an object's coords into pygame coordinates (lower-left of object => top left in pygame coords)."""
    return (coords[0], height - coords[1] - obj_height)
