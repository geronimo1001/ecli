import click
import json
import requests
import datetime
from rich.console import Console
from rich.table import Table

console = Console()

# Temporary solution to set URL
uservar = 1
uservar = int(uservar)
if uservar == 1:
    userapiurl = "https://api.emlalock.com/info?userid=s9n33u90x27jqsr&apikey=1intd05gi0l"
    useruuid = "s9n33u90x27jqsr"
elif uservar == 2:
    userapiurl = "https://api.emlalock.com/info?userid=4d89h9ev72jmft8&apikey=wh2wqiikwn"
    useruuid = "4d89h9ev72jmft8"

# Set URL based on selected user
url = requests.get(userapiurl)
text = url.text
#sessionDict = json.loads(text)

#print(sessionDict)

def get_holder_info():
    global holder_id
    sessionDict = json.loads(text)
    holder_id = sessionDict['chastitysession']['holderid']
    #print(holder_id)

def get_time_stats():
    global startDate
    global startDateFriendly
    global endDate
    global endDateFriendly
    global timeInLock
    global timeInLockFriendly
    sessionDict = json.loads(text)
    startDate = sessionDict['chastitysession']['startdate']
    startDateFriendly = datetime.datetime.fromtimestamp(startDate)
    endDate = sessionDict['chastitysession']['enddate']
    endDateFriendly = datetime.datetime.fromtimestamp(endDate)
    timeInLock = endDate - startDate
    timeInLockFriendly = datetime.datetime.fromtimestamp(timeInLock)

def showall():
    global showallthedata
    sessionDict = json.loads(text)
    showallthedata = sessionDict['chastitysession']['duration']

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
def show_user(username):
    click.echo("User account: {}".format(username))

@cli.command()
@click.option('--string', required=False, default ='World',
        help ='This is a greeting')
def hello(string):
    click.echo("Hello, {}".format(string))

@cli.command()
@click.option('--show_holder', required=False, default ='World',
        help ='Show existing holder if any')
def show_holder(show_holder):
    #starting_holder_id = sessionDict['chastitysession']['holderid']
    get_holder_info()
    if holder_id == useruuid:
        click.echo("You do not have a keyholder.".format(show_holder))
    else:
        # Need to fix this
        #click.echo(f"Holder ID is: {holder_id}".format(show_time))
        click.echo(f"Holder ID is: {holder_id}".format(show_holder))

@cli.command()
@click.option('--show_all', required=False, default ='World',
        help ='Show all API data')
def show_all(show_all):
    showall()
    click.echo(f"Session Data: {showallthedata}".format(show_all))

@cli.command()
@click.option('--show_time', required=False, default ='World',
        help ='Show existing holder if any')
def show_time(show_time):
    #starting_holder_id = sessionDict['chastitysession']['holderid']
    get_time_stats()
    click.echo(f"Session Start: {startDateFriendly}".format(show_time))
    click.echo(f"Session End:   {endDateFriendly}".format(show_time))
    click.echo(f"Time Locked:   {timeInLockFriendly}".format(show_time))
    #table = Table(show_header=True, header_style="blue")
    #table.add_column("Start Date")
    #table.add_column("End Date")
    #table.add_row(startDateFriendly)
    #table.add_row(endDateFriendly)
    #console.print(table)

if __name__=="__main__":
    cli()
