import sys
import subprocess
import fire
# import conda.cli.python_api as Conda

"""
    This python script will allow you to install all you python packages.
    Add all desire packages to the packages list and run this script like a regular python file.
"""

# Read all packages from file
with open("packages.txt") as f:
    packages = f.readlines()

# Install packages using pip


def pip():
    errors = []
    for package in packages:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package])
        except:
            errors.append(package)
            continue
    if len(errors) > 0:
        print("The following packages install resulted in error: ")
        for error in errors:
            print(" *" + error)
        print("Read the error log for more information.")
    else:
        print("All packages where installed correctly!")

# Install packages using conda


def conda():
    errors = []
    for package in packages:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "conda", "install", package])
        except:
            errors.append(package)
            continue
    if len(errors) > 0:
        print("The following packages install resulted in error: ")
        for error in errors:
            print(" *" + error)
        print("Read the error log for more information.")
    else:
        print("All packages where installed correctly!")


if __name__ == "__main__":
    fire.Fire({
        'pip': pip,
        'conda': conda
    })
