from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

# Example 1: Panel
panel = Panel("Hello, [bold magenta]World[/bold magenta]!", title="Important Panel", border_style="red")
console.print(panel)

# Example 2: Markdown
markdown_text = """
# Rich Markdown

This is *Spartacus* speaking.

* Bullet 1
* Bullet 2
"""
markdown = Markdown(markdown_text)
console.print(markdown)

# Example 3: Emoji
console.print(":rocket: Launching in :counter [red]3 :white_check_mark:")