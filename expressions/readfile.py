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
Read the contents of a file using the ".contents()" method which gives:
    j.ReadContents(j.InputSelector("input"))

Using an operator on a workflow.output(, source=<operator>) for CWL, will
insert an extra processing step. Translate to CWL, and see the extra step:

    steps:
    # other steps
    - id: _evaluate-output-out
      in:
      - id: _printout
        source: print/out
      run:
        class: ExpressionTool

        inputs:
        - id: _printout
          type: File
          loadContents: true

        outputs:
        - id: out
          type: string
        expression: '${return {out: inputs._printout.contents }}'

    outputs:
    - id: out
      type: string
      outputSource: _evaluate-output-out/out

In WDL this is translated as you'd expect:

    output {
        String out = read_string(print.out)
    }

"""

import janis_core as j
from janis_unix.tools import Echo

w = j.WorkflowBuilder("readfile")

w.input("file_to_read", j.File)

# Read the contents of a file to give to Echo
w.step("print", Echo(inp="File contents: " + w.file_to_read.contents()))

# Read the contents of the output of "print" to return as the output
w.output("out", source=w.print.out.contents())

if __name__ == "__main__":
    w.translate("cwl")