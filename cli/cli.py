from textual import events
from textual.app import App
from textual.widgets import Header, Footer, Log

from cli.input_bar import InputBar

from utils.config_reader import load_config
from utils.executor import execute

class Mesfit(App):
    
    def compose(self):
        yield Header()
        yield InputBar()
        yield Log()
        yield Footer()

    def on_mount(self):
        self.title = "MESFIT"
        self.config = load_config()

    def on_key(self, event: events.Key) -> None:
        log = self.query_one(Log)
        inp = self.query_one(InputBar)
        if event.key == "enter":
            log.clear()
            output = execute(inp.value, config = self.config)
            inp.value = ""
            log.write_lines([output.stdout])
