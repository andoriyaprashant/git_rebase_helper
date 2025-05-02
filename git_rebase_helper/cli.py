import click
from git_rebase_helper.rebase import perform_rebase
from git_rebase_helper.visualize import visualize_commits
from git_rebase_helper.dry_run import dry_run_rebase
from git_rebase_helper.conflict import resolve_conflict

@click.group()
def cli():
    """Git Rebase Helper CLI Tool"""
    pass

@cli.command()
@click.argument('base_branch')
@click.argument('feature_branch')
def rebase(base_branch, feature_branch):
    """Perform a Git rebase"""
    if perform_rebase(base_branch, feature_branch):
        print("Rebase completed successfully.")
    else:
        print("Rebase failed.")

@cli.command()
@click.argument('branch')
def visualize(branch):
    """Visualize commit history before rebase"""
    visualize_commits(branch)

@cli.command()
@click.argument('base_branch')
@click.argument('feature_branch')
def dry_run(base_branch, feature_branch):
    """Simulate the rebase process without making changes"""
    dry_run_rebase(base_branch, feature_branch)

@cli.command()
def resolve():
    """Resolve conflicts automatically"""
    resolve_conflict()

if __name__ == "__main__":
    cli()
