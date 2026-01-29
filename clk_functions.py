#!/usr/bin/env python3
#biteegithdealer
#PokerAs

import click as clk
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.panel import Panel

#Custom themes
custom_theme = Theme({
    "welcome": "bold underline magenta",
    "body": "bold white"
})

console = Console(theme=custom_theme)

@clk.group()
def quicknote():
    pass

#Function the welcome
@quicknote.command()
def welcome_quicknote():

    #Content the panel welcome
    title = Text("WELCOME TO QUICKNOTE", style="welcome")
    content = Text.assemble(
        (
            "A fast and minimal CLI tool to manage your notes.\n\n"
            "Get started with:\n"
            "  quicknote note        Create your first note\n"
            "  quicknote list        List your notes\n\n",
            "white",
        ),
        (
            "This is a QuickCode project.\n"
            "If you'd like to see more of our projects, visit:\n"
            "https://quickcode.dev\n\n"
            "QuickCode Group.",
            "bold blue",
        ),
    )

    #Panel welcome
    panel = Panel(
        content,
        title=title,
        border_style="magenta",
        expand=False
    )

    console.print(panel)