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

import janis_core as j

CommandLineThatBindsArrays = j.CommandToolBuilder(
    tool="CommandLineThatBindsArrays",
    container="ubuntu:latest",
    version="development",
    base_command="echo",
    inputs=[
        # NO prefix, joined by space (' ')  [DEFAULT]
        #   need a position to ensure it binds onto the command line
        j.ToolInput("array1", j.Array(j.String), position=0),
        #
        # No prefix, joined by commans (',')
        j.ToolInput("array2", j.Array(j.String), separator=",", position=1),
        #
        # Single prefix, then joined by space (' ')
        j.ToolInput("array3", j.Array(j.String), prefix="--prefix"),
        #
        # Single prefix, then joined by commas (',')
        j.ToolInput("array4", j.Array(j.String), prefix="--prefix", separator=","),
        #
        # Prefix applies to each element
        j.ToolInput(
            "array5",
            j.Array(j.String),
            prefix="--prefix",
            prefix_applies_to_all_elements=True,
        ),
    ],
    outputs=[j.ToolOutput("out", j.Stdout())],
)
