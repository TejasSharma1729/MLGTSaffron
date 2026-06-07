"""
Master path to all dataset files and dataset.
REPO_ROOT is the root of this project (constant, importable).
Edit DATASETS_DIR to access the correct dataset dir from anywhere in this project.
"""
import os

""" Constant path to the root of this project. """
REPO_ROOT: str = os.path.dirname(os.path.abspath(__file__))

""" Set this to the directory where all datasets are stored."""
DATASETS_DIR: str = os.path.join(REPO_ROOT, "data")