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
NB: Although WDL supports optional files, some backends of Cromwell do not.
"""

import janis_core as j

ToolWithOptionalOutput = j.CommandToolBuilder(
    tool="optional_output_tool",
    version="v0.1.0",
    container="ubuntu:latest",
    base_command=[],
    arguments=[j.ToolArgument("echo 1 > ", shell_quote=False)],
    inputs=[
        j.ToolInput(
            "outputFilename", j.String(optional=True), default="out.csv", position=1
        )
    ],
    outputs=[
        j.ToolOutput("out", j.File(optional=True), selector=j.InputSelector("outputFilename"))
    ],
)
