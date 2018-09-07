import os
import sys
from inspect import stack


def bundle_dir():
    """Handle resource management within an executable file."""
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(stack()[1][1]))
    if os.path.exists(bundle_dir):
        return bundle_dir


def resource_path(relative):
    """Adjust path for executable use in executable file"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
