import pytest
from pathlib import Path
from git_rebase_helper.utils import squash_commits, get_commit_range, check_git_status
from git import Repo

@pytest.fixture
def git_repo(tmp_path):
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path)
    file_path = repo_path / "file.txt"
    file_path.write_text("Hello, world!")
    repo.index.add(["file.txt"])
    repo.index.commit("Initial commit")
    return repo

def test_squash_commits(git_repo):
    repo = git_repo
    file_path = Path(repo.working_tree_dir) / "file.txt"

    file_path.write_text("More content!")
    repo.index.add(["file.txt"])
    repo.index.commit("Second commit")
    file_path.write_text("Even more content!")
    repo.index.add(["file.txt"])
    repo.index.commit("Third commit")
    assert squash_commits("HEAD~2..HEAD", repo) is True


def test_get_commit_range(git_repo):
    repo = git_repo
    file_path = Path(repo.working_tree_dir) / "file.txt"
    file_path.write_text("Adding more content.")
    repo.index.add(["file.txt"])
    repo.index.commit("Third commit")
    commit_range = get_commit_range(repo)
    assert commit_range is not None

def test_check_git_status(git_repo):
    repo = git_repo
    file_path = Path(repo.working_tree_dir) / "file.txt"
    assert check_git_status(repo) is True
    file_path.write_text("Uncommitted change")
    assert check_git_status(repo) is False