from setuptools import setup

setup(
    name = "eyes",
    version = "1.0",
    install_requires = [
            "requests",
            "flask",
            "MySQL-python",
            "flask-sqlalchemy",
            "flask-wtf",
            "flask-debugtoolbar",
        ],
)

