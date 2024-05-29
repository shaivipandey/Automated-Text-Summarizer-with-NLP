import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Automated-Text-Summarizer-with-NLP"
AUTHOR_USER_NAME = "Shaivi Pandey"
SRC_REPO = "TextSummarizer"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/shaivipandey/Automated-Text-Summarizer-with-NLP",
    project_urls={
        "Bug Tracker": f"https://github.com/shaivipandey/Automated-Text-Summarizer-with-NLP/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)