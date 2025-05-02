import subprocess


def resolve_conflict():
    # Check for conflicts using Git
    subprocess.run(["git", "status"], check=True)

    subprocess.run(["git", "checkout", "--theirs", "file_with_conflict"], check=True)
    subprocess.run(["git", "add", "file_with_conflict"], check=True)
    print("Conflict resolved automatically.")
