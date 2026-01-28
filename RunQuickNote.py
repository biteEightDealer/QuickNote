import click as clk

@clk.command()
def quicknote():
    clk.echo("WELCOME TO QUICKNOTE")

if __name__ == '__main__':
    quicknote()