import graphviz
from git import Repo

def visualize_commits(branch):
    repo = Repo(".")
    commits = list(repo.iter_commits(branch))

    dot = graphviz.Digraph(comment='Commit History')

    for commit in commits:
        dot.node(commit.hexsha[:7], commit.message.strip())

    dot.render("commit_history", view=True)
