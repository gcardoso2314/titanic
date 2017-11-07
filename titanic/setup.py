from setuptools import setup

def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()

setup(
    name = "titanic",
    version = "0.1",
    author = "Gerard Cardoso",
    author_email = "gerard2314@gmail.com",
    description = "Analysis of the Titanic dataset",
    license = "MIT",
    url = "https://github.com/gerard2314/titanic",
    packages=['titanic'],
    install_requires=[
        'pypandoc>=1.4',
        'pyyaml>=3.12'
    ],
    long_description=readme(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
