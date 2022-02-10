from textual.app import App

# using align to simple layout data
from rich.align import Align

# reactive for mutable input
from textual.reactive import Reactive
from textual.widget import Widget


# display and handling counter app
class Title(Widget):
    counter = Reactive(0)

    def set_counter(self, counter_value: int):
        self.counter += counter_value

    def render(self):
        text_output = f"the counter is: {self.counter}"
        self.style = "on color(8)"
        return Align.center(text_output, vertical="middle")

# panel that showing which comment should be used
class SimpleCommand(Widget):
    def render(self):
        self.style="on color(0)"
        return Align.left("Press 'y' to increment, 'u' to decrement, and 'q' to quit", vertical="bottom")

# show all panel into terminal
class Menu(App):
    title_obj = Title()

    async def on_load(self, event):
        await self.bind("q", "quit")
        await self.bind("y", "increment(1)")
        await self.bind("u", "decrement(1)")

    async def action_increment(self, increment: int):
        self.title_obj.set_counter(increment)

    async def action_decrement(self, decrement: int):
        self.title_obj.set_counter(-decrement)

    async def on_mount(self):
        await self.view.dock(self.title_obj, size=20)
        await self.view.dock(SimpleCommand(), edge="bottom", size=2)


if __name__ == "__main__":
    Menu.run(title="Simple Increment")
