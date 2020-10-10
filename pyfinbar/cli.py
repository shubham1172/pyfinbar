import click
import json
from pyfinbar.client import MoneyControlStock
from pyfinbar.ui.root import get_root


@click.group()
def cli():
    pass

@cli.command(help="Fetch stock data")
@click.option("--format", default="plain", help="plain,colored,json")
def fetch(format):
    if format in ["plain", "colored"]:
        click.echo(
            " ".join([x.to_string(colored=format == "colored") for x in MoneyControlStock.fetch_values()]))
    elif format == "json":
        click.echo(json.dumps([x.to_object() for x in MoneyControlStock.fetch_values()]))
    else:
        raise AttributeError()


@cli.command(help="Start dock")
@click.option("--position", default=0, help="placement of dock (y-axis) in percentage")
@click.option("--refresh-rate", default=5, help="data refresh rate in seconds")
def dock(position, refresh_rate):
    root = get_root(position, refresh_rate)
    root.mainloop()


if __name__ == "__main__":
    cli()
