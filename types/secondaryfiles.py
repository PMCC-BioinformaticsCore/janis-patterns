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
A little example creating a datatype with secondaries, then using
this new datatype in a tool and workflow
"""

import janis_core as j


class MyDataTypeWithSecondaries(j.File):
    def __init__(self, optional=False):
        super().__init__(optional=optional)

    @staticmethod
    def secondary_files():
        return [".csv"]


ToolWithSecondaryFiles = j.CommandToolBuilder(
    tool="secondary_files",
    version="v0.1.0",
    container="ubuntu:latest",
    base_command="echo",
    inputs=[j.ToolInput("inp", MyDataTypeWithSecondaries, position=0)],
    outputs=[
        j.ToolOutput(
            "out",
            MyDataTypeWithSecondaries,
            selector="file.txt",
        )
    ],
)

WorkflowWithSecondaries = j.WorkflowBuilder("workflow_with_secondaries")

inner_dt = MyDataTypeWithSecondaries
scatter = None

# helper method to show how scatters / not scatters work
should_scatter = False
if should_scatter:
    inner_dt = j.Array(MyDataTypeWithSecondaries)
    scatter = "inp"

WorkflowWithSecondaries.input("inp", inner_dt)
WorkflowWithSecondaries.step(
    "stp", ToolWithSecondaryFiles(inp=WorkflowWithSecondaries.inp), scatter=scatter
)
WorkflowWithSecondaries.output("out", source=WorkflowWithSecondaries.stp.out)

if __name__ == "__main__":
    ToolWithSecondaryFiles().translate("wdl")
    # WorkflowWithSecondaries().translate("wdl")
