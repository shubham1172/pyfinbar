import click
import json
from pygfbar.auth import Credentials
from pygfbar.data import SheetReader


@click.group()
def cli():
    pass


@cli.command(help="Authorize the application with Google")
def auth():
    try:
        Credentials().get()
        click.echo("Authorization successful!")
    except Exception as e:
        click.echo("Authorization failed: " + e)


@cli.command(help="Fetch stock data")
@click.option("--format", default="plain", help="plain,colored,json")
def fetch(format):
    s = SheetReader()
    if format in ["plain", "colored"]:
        click.echo(
            " ".join([x.to_string(colored=format == "colored") for x in s.get_data()]))
    elif format == "json":
        click.echo(json.dumps([x.to_object() for x in s.get_data()]))


if __name__ == "__main__":
    cli()
