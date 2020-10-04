import click
import json
from pygfbar.auth import Credentials
from pygfbar.sheet_reader import SheetReader
from pygfbar.ui.root import get_root


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
    else:
        raise AttributeError()


@cli.command(help="Start dock")
@click.option("--position", default=0, help="placement of dock (y-axis) in percentage")
@click.option("--refresh-rate", default=5, help="data refresh rate in seconds")
def dock(position, refresh_rate):
    try:
        Credentials().get()
    except Exception as e:
        click.echo("Authorization failed: " + e)
        return

    root = get_root(position, refresh_rate)
    root.mainloop()


if __name__ == "__main__":
    cli()
