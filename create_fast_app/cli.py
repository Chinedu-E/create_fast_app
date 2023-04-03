import os
import sys
import click

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from create_fast_app import utils

@click.command()
@click.option("--ml", default=False, help="Attach A machine learning directory to project", type=bool)
@click.option("--type", type=str, default="microservice")
@click.argument('project_name')
def create_fastapi_app(project_name, type, ml):
    """Create a new FastAPI project."""
    # Get the absolute path of the directory where the script is running
    current_dir = os.getcwd()
    project_dir = os.path.join(current_dir, project_name)
    os.makedirs(project_dir)
    
    # Copy the FastAPI project template to the new directory
    if type == "microservice":
        utils.generate_microservice_app(project_dir)
        
    elif type == "monolith":
        utils.generate_monolith_app(project_dir)
        
    elif type == "ml_app":
        utils.generate_ml_app(project_dir)
        
    else:
        click.echo("Invalid project given. Must be one of [ml_app, monolith, microservice]")
        
    
    # Create a virtual environment and install the required dependencies
    os.chdir(project_dir)
    utils.install_packages()
    
    # Print the success message
    click.echo(f'Success! Created {project_name} at {current_dir}/{project_name}')



if __name__ == '__main__':
    create_fastapi_app()
