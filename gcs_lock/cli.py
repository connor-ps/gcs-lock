"""Console script for gcs_lock."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("gcs-lock")
    click.echo("=" * len("gcs-lock"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")


if __name__ == "__main__":
    main()  # pragma: no cover
