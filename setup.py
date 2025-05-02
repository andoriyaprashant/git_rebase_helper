from setuptools import setup, find_packages

setup(
    name="git-rebase-helper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gitpython",
        "click",
        "graphviz"
    ],
    entry_points={
        'console_scripts': [
            'git-rebase-helper=git_rebase_helper.cli:cli',
        ],
    },
)
