from setuptools import setup
import os

VERSION = "0.1a0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-dns",
    description="Custom SQL function for making DNS lookups",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-dns",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-dns/issues",
        "CI": "https://github.com/simonw/datasette-dns/actions",
        "Changelog": "https://github.com/simonw/datasette-dns/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_dns"],
    entry_points={"datasette": ["dns = datasette_dns"]},
    install_requires=["datasette", "dnspython"],
    extras_require={"test": ["pytest", "pytest-asyncio", "httpx"]},
    tests_require=["datasette-dns[test]"],
)
