import pytest
import subprocess
from git_rebase_helper.utils import squash_commits, get_commit_range, check_git_status
from git import Repo

@pytest.fixture
def git_repo(tmp_path):
    """Fixture for setting up a temporary Git repository."""
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path)
    # Add a test file and commit
    (repo_path / "file.txt").write_text("Hello, world!")
    repo.index.add(["file.txt"])
    repo.index.commit("Initial commit")
    return repo

def test_squash_commits(git_repo):
    """Test the squashing of commits."""
    repo = git_repo
    # Create another commit
    (repo.working_tree_dir / "file.txt").write_text("More content!")
    repo.index.add(["file.txt"])
    repo.index.commit("Second commit")

    # Run squash (squash the last two commits)
    result = squash_commits("HEAD~2..HEAD")
    assert result is True  # Assuming squash succeeds, it should return True

def test_get_commit_range(git_repo):
    """Test the commit range function."""
    repo = git_repo
    # Create another commit
    (repo.working_tree_dir / "file.txt").write_text("Adding more content.")
    repo.index.add(["file.txt"])
    repo.index.commit("Third commit")

    # Get the commit range for the last three commits
    commit_range = get_commit_range()
    assert commit_range is not None
    assert "HEAD~2..HEAD" in commit_range

def test_check_git_status(git_repo):
    """Test if Git status is clean."""
    repo = git_repo
    # Should be clean at first
    status = check_git_status()
    assert status is True

    # Make some changes to check status
    (repo.working_tree_dir / "file.txt").write_text("Uncommitted change")
    repo.index.add(["file.txt"])
    status = check_git_status()
    assert status is False
