# Locuplot

Locuplot is a python application to generate graph based on locust statistics reporting.

## Usage
TODO: When we will release locuplot to the pip registry, complete this section.
TODO: Reference how to install the application.
TODO: Reference command line arguments

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

