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
We'll use Janis to _try_ and collect a SINGLE file with the extension '.txt',
but one won't exist. CWL will automatically coerce the empty File[0] to File? (null).

However, in WDL, we have do this slightly differently:
    File? out = if length(glob("*.txt")) > 0 then glob("*.txt")[0] else None

NB: Although WDL supports optional files, some backends of Cromwell do not.
"""

import janis_core as j

ToolWithOptionalWildcardOutput = j.CommandToolBuilder(
    tool="optional_wildcard_output_tool",
    version="v0.1.0",
    container="ubuntu:latest",
    base_command=None,
    # write '1' to a file called 'out.csv'
    arguments=[j.ToolArgument("echo 1 > out.csv", shell_quote=False)],
    inputs=[
        j.ToolInput("inp", j.File, localise_file=True)
    ],
    outputs=[
        j.ToolOutput("out_csv_files", j.Array(j.File), selector=j.WildcardSelector("*.csv")),
        # the next two are functionally equivalent
        j.ToolOutput("out_single_csv_file_1", j.Array(j.File), selector=j.WildcardSelector("*.csv", select_first=True)),
        j.ToolOutput("out_single_csv_file_2", j.Array(j.File), selector=j.WildcardSelector("*.csv")[0]),

        # OPTIONAL glob outputs
        # capture all files with *.txt pattern (but select the first if possible)
        j.ToolOutput("out_optional_glob", j.File(optional=True), selector=j.WildcardSelector("*.txt", select_first=True))
    ],
)

if __name__ == "__main__":
    ToolWithOptionalWildcardOutput().translate("wdl")