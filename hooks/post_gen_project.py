import os
import shutil
import subprocess
import sys

REMOVE_PATHS = [
    '{% if cookiecutter.ci != "GitHub Actions" %} .github {% endif %}',
    '{% if cookiecutter.ci != "Travis CI" %} .travis.yml {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

# Initialize the newly created directory as a Git repo
subprocess.run(["git", "init"])
subprocess.run(["git", "add", "./"])
subprocess.run(["git", "commit", "-m", "Initialize the NUR packages skeleton"])
