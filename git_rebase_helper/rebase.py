import subprocess
from git import Repo

def perform_rebase(base_branch, feature_branch):
    try:

        repo = Repo(".")

        repo.git.fetch()

        repo.git.checkout(feature_branch)

        result = subprocess.run(
            ["git", "rebase", base_branch],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout) 
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during rebase: {e.stderr}")
        return False
