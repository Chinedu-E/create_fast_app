# create-fast-app

`create-fast-app` is a Python package that helps you quickly create new FastAPI projects with basic templates. It includes a command-line interface (CLI) that lets you specify the type of project you want to create, as well as options to attach a machine learning directory.

## Requirements

## Installation
To use create-fastapi-app, you must have Python 3.6 or later installed on your system. You can install the package using pip:

```bash
pip install create-fast-app
```

## Usage
To create a new FastAPI project, run the following command:

```
create-fast-app <project-name> --type=<project-type>
```

Replace `<project-name>` with the desired name for your new project. The `--type` option is used to specify the type of project you want to create. There are three options available:
- `microservice`: Creates a FastAPI microservice project.
- `monolith`: Creates a FastAPI monolith project.
- `ml_app`: Creates a FastAPI machine learning project.

By default, the --type option is set to microservice.


You can also include the --ml option to attach a machine learning directory to your project. This option is only available for microservice and monolith project types.


For example, to create a FastAPI monolith project with a machine learning directory attached, run:

```
create-fast-app my-project --type=monolith --ml=True
```

After running the command, `create-fast-app` will create a new directory with your project name in the current working directory. It will then copy the appropriate FastAPI project template and install the required dependencies in a new virtual environment.

## Project Structure

The directory structure for each project type is as follows:

