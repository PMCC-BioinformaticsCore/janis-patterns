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

# Declare workflow builder
w = j.WorkflowBuilder("my_conditional_workflow")

# Expose an input called 'inp' which is an optional string
w.input("inp", j.String(optional=True), doc="Will br printed if the string has value")

w.step(
    "print_if_has_value",
    Echo(inp=w.inp),
    # only print if the input "inp" is defined.
    when=j.logical.IsDefined(w.inp)
)

w.output("out", source=w.print_if_has_value)


if __name__ == "__main__":
    w.translate("cwl")
