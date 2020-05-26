from setuptools import setup

setup(
    name="random_password-cli",
    version="0.1.0",
    packages=["random_password"],
    entry_points={"console_scripts": ["random_pass = random_password.__main__:main"]},
)
