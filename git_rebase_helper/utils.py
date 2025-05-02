import subprocess
from git import Repo

def squash_commits(commit_range):
    """
    Squashes commits in the provided commit range.
    Args:
        commit_range (str): Range of commits to squash, e.g., 'HEAD~3..HEAD'.
    """
    try:
        repo = Repo(".")
        # Check if there are any commits to squash
        if not commit_range:
            raise ValueError("No commit range provided for squashing.")
        
        result = subprocess.run(
            ["git", "rebase", "-i", commit_range],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Squash successful:\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during squashing commits: {e.stderr}")
        return False

def get_commit_range():
    """
    Get the range of commits to be rebased.
    Example: If we want to rebase the last 3 commits: 'HEAD~3..HEAD'
    """
    repo = Repo(".")
    commits = list(repo.iter_commits('HEAD', max_count=3))
    if len(commits) < 2:
        print("Not enough commits to determine range.")
        return None
    return f"{commits[-1].hexsha}..{commits[0].hexsha}"

def check_git_status():
    """
    Checks the current status of the repository.
    Returns True if the repo is clean (no uncommitted changes), False otherwise.
    """
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout:
            print("Uncommitted changes detected:")
            print(result.stdout)
            return False
        else:
            print("Repository is clean.")
            return True
    except subprocess.CalledProcessError as e:
        print(f"Error checking Git status: {e.stderr}")
        return False
