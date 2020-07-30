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

# from ... import ToolWithTwoInputs

wf = j.WorkflowBuilder("scatter_execution")

# Two inputs which MUST have the same length
wf.input("input1", j.Array(j.String))
wf.input("input2", j.Array(j.String))

wf.step(
    "run_toolwithtwoinputs",
    # Connect the inputs as normal
    ToolWithTwoInputs(toolInput1=wf.input1, toolInput2=wf.input2),
    # Scatter using the 'dot-product' on 'input1' | 'input2'
    # input of Echo.
    scatter=["toolInput1", "toolInput2"],
    # this is equivalent to:
    # scatter=j.ScatterDescription(
    #     fields=["toolInput1", "toolInput2"], method=j.ScatterMethod.dot
    # ),
)

# This will automatically be an array of files
# because wf.run_toolwithtwoinputs has a scatter block.
wf.output("out", source=wf.run_toolwithtwoinputs.out)
