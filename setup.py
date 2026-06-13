import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="END-TO-END-ML-PROJECT-With-DVC-MLflow"
AUTHOR_USER_NAME='kanishka-rani-2005'
SRC_REPO="WineQuality"
AUTHOR_EMAIL="kanishka22043@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python pck for ml app",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)