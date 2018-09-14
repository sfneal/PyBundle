# Set directory paths and file names for executable bundles
import os
import sys
from inspect import stack


def frozen_bundle():
    if getattr(sys, 'frozen', False):
        # Running in a bundle
        return True
    else:
        # Running in a development Python environment
        return False


def bundle_dir():
    """Handle resource management within an executable file."""
    if frozen_bundle():
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.dirname(os.path.abspath(stack()[1][1]))
    if os.path.exists(bundle_dir):
        return bundle_dir


def resource_path(relative):
    """Adjust path for executable use in executable file"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
