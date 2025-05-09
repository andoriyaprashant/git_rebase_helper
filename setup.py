from setuptools import setup, find_packages

setup(
    name='git-rebase-helper',
    version='0.2', 
    packages=find_packages(),
    install_requires=[
        'click',
        'gitpython',
        'graphviz',
    ],
    entry_points={
        'console_scripts': [
            'git-rebase-helper = git_rebase_helper.cli:cli',
        ],
    },
    long_description="""# git-rebase-helper

# git-rebase-helper

`git-rebase-helper` is a command-line tool designed to simplify Git rebasing tasks. It offers an easy way to manage and automate Git rebase processes, visualize commit histories, simulate rebases, and resolve conflicts during rebasing. This tool is perfect for developers looking for a smoother Git workflow when dealing with rebases.

## Features:
- **Rebase**: Easily perform a rebase between a base branch and a feature branch.
- **Dry-run**: Simulate the rebase process without making any changes to your repository.
- **Visualize**: View the commit history of a branch before performing the rebase.
- **Resolve**: Automatically attempt to resolve common rebase conflicts.

This tool helps streamline your Git workflow, saving time and reducing the chance of errors during rebasing operations.

##  Usage

Run the CLI tool:

```bash
git-rebase-helper --help
```

### Available Commands

| Command     | Description                                              |
|-------------|----------------------------------------------------------|
| `rebase`    | Perform a Git rebase between two branches.               |
| `dry-run`   | Simulate the rebase process without making changes.      |
| `visualize` | Visualize the commit history of a branch.                |
| `resolve`   | Automatically resolve common rebase conflicts.           |

---

## Example Usage

> Replace `<base-branch>` and `<feature-branch>` with your actual branch names.

### Rebase a feature branch onto a base branch

```bash
git-rebase-helper rebase <base-branch> <feature-branch>
git-rebase-helper rebase main rebasecheck
```

### Dry run to preview a rebase

```bash
git-rebase-helper dry-run <base-branch> <feature-branch>
git-rebase-helper dry-run main rebasecheck
```

### Visualize commit history of a branch

```bash
git-rebase-helper visualize <branch-name>
git-rebase-helper visualize rebasecheck
```

### Attempt to auto-resolve merge conflicts

```bash
git-rebase-helper resolve
```
    """,
    long_description_content_type='text/markdown',
)
