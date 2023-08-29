import subprocess
from os.path import dirname, exists
from os import mkdir


def get_git_root_path():
    """Return the absolute path of the repository root."""
    try:
        base_dir = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
        return base_dir.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        print("Current directory is not a Git repository.")
        return None

def get_parent_directory(path):
    """Return the parent directory of the given path."""
    return dirname(path)

git_root = get_git_root_path()
parent_dir = None
if git_root:
    parent_dir = get_parent_directory(git_root)
    if parent_dir is None:
        raise ValueError("Project dir is not connected to git. Exiting...")

STORAGE = f"{parent_dir}/nfl_analytics/storage"

if not exists(STORAGE):
    mkdir(STORAGE)
