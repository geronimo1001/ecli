import click

@click.group()
@click.option('--debug/--no-debug')
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")

@cli.command()
@click.option('--username')
def greet(username):
    click.echo(f"Hello {username}!")

if __name__ == '__main__':
    cli(auto_envvar_prefix='GREETER')