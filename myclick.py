#!/usr/bin/env python3

"""
Command line tool using argparse
"""

import click

# Create a top-level group under which other groups and commands will reside
@click.group()
# Create a function to act as the top-level group. The click.group method transforms the function into a group
def cli():
    pass

# Create a group to hold the ship commands
@click.group(help='Ship related commands')
def ships():
    pass

# Add the ships group as a command to the top-level group.
# Note that the cli function is a now a group with an add_command method
cli.add_command(ships)

# Add a command to the ships group.
# Notice that ships.command is used instead of click.command
@ships.command(help='Sail a ship')
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")


@ships.command(help='Lists all of the ships')
def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

# Add command to cli group
@cli.command(help='Talk to the sailor')
@click.option('--greeting', default='Ahoy there', help='Greeting for sailor')
@click.argument('name')
def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    # Call the top level group
    cli()