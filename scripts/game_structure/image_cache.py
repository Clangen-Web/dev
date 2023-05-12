import pygame
from scripts.platformwrapper import is_web

_images = {}
def load_image(path):
    """
    If not in the cache already, loads the image from path as a surface.
    Otherwise, the image is retrieved from the cache.
    """
    if is_web:
        return pygame.image.load(path)
    if path not in _images:
        _images[path] = pygame.image.load(path)
    return _images[path]
