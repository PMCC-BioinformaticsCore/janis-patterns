# Janis - Python framework for portable workflow generation
# Copyright (C) 2020  Michael Franklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Create a step whose value is dependent on multiplying an input number,
and the length of an list input. We construct the combination of operators
using fairly natural Python syntax.
"""

import janis_core as j
from janis_core import ToolInput, ToolOutput, Int, Stdout, File
from janis_unix.tools import Echo


AddTwo = j.CommandToolBuilder(
    tool="expr",
    base_command=None,
    arguments=[j.ToolArgument("expr 2 + ", position=0, shell_quote=False)],
    version="dev", container="ubuntu:latest",
    inputs=[
        ToolInput("inp", Int(), position=1)
    ],
    outputs=[
        ToolOutput("out", Stdout()),
    ]
)


w = j.WorkflowBuilder("str_to_int")

w.input("str_input", str)

w.step("echo", Echo(inp=w.str_input))
w.step("exp", AddTwo(inp=w.echo.out.contents().as_int()))

w.output("out", source=w.exp.out)

if __name__ == "__main__":
    w.translate("wdl")
