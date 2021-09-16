from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cuddly-potato",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=[
        "django",
        "mutagen",
        "uwsgi",
    ],
    url="https://github.com/rmartin16/cuddly-potato",
    author="Russell Martin",
    description="Podcast feeder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="python rss podcast feed",
    zip_safe=False,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
)
