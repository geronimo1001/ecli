import click

@click.group()
def cli():
    pass

@cli.command()
def about():
    click.echo("Emla CLI")

@cli.command()
def version():
    click.echo("ECLI v1.0")

@cli.command()
@click.option('--username', required=False, default ="geronimo",
    help ='Show user account being queried')
def showuser(username):
    click.echo("User account: {}".format(username))

@cli.command()
@click.option('--string', required=False, default ='World',
        help ='This is a greeting')
def hello(string):
    click.echo("Hello, {}".format(string))

if __name__=="__main__":
    cli()
