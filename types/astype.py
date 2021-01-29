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
Sometimes a tool will give us an output type that isn't exactly what we expect.
For example, a tool might return a File (like "cat"), but you actually know it'll
return a TextFile because you know the input.

Usually, your subsequent tools will throw a type warning, as:
    File -> TextFile (incompatible)
"""

import janis_core as j
from janis_unix.tools import Cat

# Declare a new subclass of j.File and write a new tool to accept it


class SubFile(j.File):
    @staticmethod
    def name():
        return "SubFile"


ToolThatAcceptsSubFile = j.CommandToolBuilder(
    tool="acceptingSubFile",
    base_command="cat",
    inputs=[j.ToolInput("inp", SubFile)],
    outputs=[j.ToolOutput("out", j.Stdout(SubFile))],
    version="test",
    container="ubuntu:latest",
)

# Declare workflow we're we'll use the type alias

w = j.WorkflowBuilder("aliasing")
w.input("inp", SubFile)
w.step("stp1", Cat(file=w.inp))

# This line would cause the following critical message to be logged:
#   [CRITICAL]: Mismatch of types when joining 'stp1.out' to 'stp2.inp': stdout<File> -/→ SubFile
# w.step("stp2", ToolThatAcceptsSubFile(inp=w.stp1.out))

# Instead, we'll use the .as_type method:
w.step("stp2", ToolThatAcceptsSubFile(inp=w.stp1.out.as_type(SubFile)))

w.output("out", source=w.stp2.out)

if __name__ == "__main__":
    w.translate("wdl")