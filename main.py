from rich.console import Console
from rich.progress import track
import time

console = Console()

def format_for_rainbow(string: str, offset = 0) -> str:
    lenght = len(string)
    s = ""
    rainbow = ["red", "orange", "yellow", "green", "blue", "purple", "magenta"]
    rainbow_rgb = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (128, 0, 128), (255, 0, 255)]
    for i in range(lenght):
        s += f"[{rainbow[(i+offset) % 7]}]{string[i]}[/]"
    return s

offset = 0
while True:
    if offset == 7:
        offset = 0
    try:
        console.print(format_for_rainbow("Hello, World!", offset), end="\r")
        time.sleep(0.1)
    except KeyboardInterrupt:
        console.print(format_for_rainbow("\nGoodbye!", offset))
        break
    offset += 1
