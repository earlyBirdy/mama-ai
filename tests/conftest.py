"""Pytest configuration to ensure the project root is importable.

This makes `import src` work even if pytest changes the working directory.
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
