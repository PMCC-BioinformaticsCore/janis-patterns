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

# Command we're trying to replicate:
#   grep '<pattern>' '<file>' | wc -l
#
# The important bit is we'll add an argument "| wc -l", but make
#   sure "shell_quote=False", otherwise it would get added to the
#   command line as: grep '<pattern>' '<file>' '| wc -l'
#

CountLinesThatMatchPattern = j.CommandToolBuilder(
    tool="countLinesThatMatchPattern",
    container="ubuntu:latest",
    version="development",
    base_command="grep",
    arguments=[j.ToolArgument("| wc -l", position=2, shell_quote=False)],
    inputs=[
        j.ToolInput("pattern", j.String, position=0),
        j.ToolInput("file", j.File, position=1),
    ],
    outputs=[
        j.ToolOutput(
            "out", j.Int, selector=j.standard.ReadContents(j.Stdout()).as_int(),
        )
    ],
)
