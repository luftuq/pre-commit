# Setting environment for pre-commit hooks

Pre-commit includes 
 - ruff
 - mypy

How to
 - Install [git](https://git-scm.com/)
 - Clone this repo into VS Code folder
``` shell
 git clone %url% 
```
 - Create conda environment
``` shell
 conda create env -n pre-commit -f conda_environment.yaml
```
 - run
``` shell
pre-commit install 
```

Now pre-commit hooks will run automatically on git commit


Usage
 - Run pre-commit without committing and on all files
``` shell
pre-commit run --all-files
```
 - Update repositories of hooks to new version
``` shell
pre-commit autoupdate
```

