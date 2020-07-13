from custom_actions import *
import inspect

g = globals().copy()

actions = {obj().name(): obj() for name, obj in g.items() if inspect.isclass(obj)}