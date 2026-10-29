from rich.console import Console
from rich.text import Text
import time

console = Console()
message = 'Hola futuro programador'

for letter in message:
    console.print(Text(letter, style='bold magenta'), end='')
    time.sleep(0.1)