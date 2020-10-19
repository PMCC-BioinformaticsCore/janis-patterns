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
In this file, we produce a workflow that scatters
"""

import janis_core as j

# Choose a tool
from janis_unix.tools import Cat

tool = Cat()

# Declare which input (ids) to scatter on
fields_to_scatter = {"file"}

# State how to scatter those inputs
scatter_method = j.ScatterMethod.dot

# Declare a workflow called {tool.id() + "_scattered"}
w = j.WorkflowBuilder(tool.id() + "_scattered")

# Pass through the inputs, but make any "fields_to_scatter" a j.Array, store these values in a map of inputs
inps = {
    inp.id(): w.input(
        inp.id(), j.Array(inp.intype) if inp.id() in fields_to_scatter else inp.intype,
    )
    for inp in tool.tool_inputs()
}

# Create a step:
stp = w.step(
    # with step_id same as the tool name
    tool.id().lower(),
    # by spreading those inputs (we just declared) onto the tool.
    tool(**inps),
    # declaring the scatter information
    scatter=j.ScatterDescription(fields=list(fields_to_scatter), method=scatter_method),
)

# janis helper method to capture all outputs from a step.
w.capture_outputs_from_step(stp)
