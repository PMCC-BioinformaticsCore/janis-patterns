import janis as j
from janis_unix.tools import Echo

w = j.WorkflowBuilder("hello_world")

# Declare an input called "text"
w.input("text", j.String)

# Use the "Echo" tool in a step called "print"
w.step("print", Echo(inp=w.text))

# Create an output called "out"
w.output("out", source=w.print.out)
