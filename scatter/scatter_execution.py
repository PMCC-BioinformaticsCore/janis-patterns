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
from janis_unix.tools import Echo

wf = j.WorkflowBuilder("scatter_execution")

wf.input("inputs", j.Array(j.String))

wf.step(
    "print",
    # Connect the regular array inputs
    Echo(inp=wf.inputs),
    # Scatter of the 'inp' input of Echo.
    scatter="inp",
)

# This will automatically be an array of files
# because wf.print has a scatter block.
wf.output("out", source=wf.print.out)
