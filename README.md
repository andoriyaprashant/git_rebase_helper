# git-rebase-helper

A command-line tool to simplify Git rebasing tasks.  
This tool provides a set of commands to help you perform, simulate, visualize, and resolve conflicts during a Git rebase.

---

## Installation

You can install the `git-rebase-helper` package using `pip`:

```bash
pip install git-rebase-helper
```

Alternatively, to install it in editable mode (for development or testing):

```bash
git clone https://github.com/your-username/git-rebase-helper.git
cd git-rebase-helper
pip install -e .
```

Make sure you have the following dependencies installed:

- git  
- click  
- gitpython  
- graphviz  

---

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
