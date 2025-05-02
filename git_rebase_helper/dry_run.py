import subprocess

def dry_run_rebase(base_branch, feature_branch):
    try:
        result = subprocess.run(
            ["git", "rebase", "--dry-run", base_branch],
            capture_output=True,
            text=True
        )
        print("Dry Run Rebase Results:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error during dry run: {e.stderr}")
