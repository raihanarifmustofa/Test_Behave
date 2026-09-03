import os
import sys
import django

def before_all(context):
    # Path to directory (Isi sesuai direktori kalian)
    project_path = r"PROJECT PATH"

    # Add project path to sys.path
    sys.path.insert(0, project_path)
