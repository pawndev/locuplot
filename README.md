# Locuplot

Locuplot is a python application to generate graph based on locust statistics reporting.

## Usage

### Install
Locuplot is available on pypi registry, you can:
```bash
pip install locuplot
```

### Usage

There is a help command `locuplot -h`

To use this project, there is 3 arguments to give.
`locuplot -d example\stats -p sample -e dist`

Arguments list:
- -d | --directory => Specify the folder where the locust stats are.
- -p | --prefix    => The prefix you gave to locust for generated stats
- -e | --export    => The export directory you want png and html generated files (default to `./dist`)

## Local setup

Make sure to install [poetry](https://python-poetry.org/) first. Then, make a `poetry install` in the project
root directory. 

To execute locuplot locally, use this commands:
```bash
poetry run locuplot -d example\stats -p sample
```

For further information you can display the helper like this:

```bash
poetry run locuplot -h
```

### Commands

These custom commands are launched via poetry and an awesome plugin named
[taskipy](https://github.com/illBeRoy/taskipy). Go check out this project !

Non exhaustive custom commands:

| Command                 | Description                                     |
|-------------------------|-------------------------------------------------|
| poetry run task locust  | Run sample locust test                          |
| poetry run task jupyter | Launch jupyter notebook with example statistics |

