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
from janis_unix.tools import Echo

w = j.WorkflowBuilder("multiply")

w.input("number_input", int)
w.input("list_input", j.Array(j.String()))

# The input expression:
#   (w.number_input * w.list_input.length()).as_str()
# is equivalent to the following manually constructed:
#   j.AsStringOperator(j.MultiplyOperator(w.number_inputs, j.LengthOperator(w.list_input)))

w.step("multiply", Echo(inp=(w.number_input * w.list_input.length()).as_str()))

w.output("out", source=w.number_input.as_str() + w.multiply.out.contents() + "my-output")

if __name__ == "__main__":
    w.translate("wdl")
