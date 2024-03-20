from setuptools import setup

with open("ReadMe.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "Prachi"
SRC_REPOSITORY = 'src'
REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPOSITORY,
    version= '0.0.1',
    author = AUTHOR_NAME,
    description= 'Using Python packages to make a web app for content recommendation to the user',
    long_description= long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPOSITORY],
    python_requires = '>=3.7',
    install_req = REQUIREMENTS,
)

#run: streamlit run yourscript.py