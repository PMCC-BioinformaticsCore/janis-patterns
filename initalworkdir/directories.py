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
How to create an empty directory, using the value of an input
"""

import janis_core as j

CLT = j.CommandToolBuilder(
    tool="create_initial_stuff",
    base_command=["ls", "*"],
    version="dev",
    container="ubuntu:latest",
    inputs=[
        j.ToolInput(
            "name_of_output_folder", j.String(optional=True), default="some-string"
        )
    ],
    outputs=[j.ToolOutput("out_dir", j.Directory, selector="some-string")],
    directories_to_create=[j.InputSelector("name_of_output_folder")],
    files_to_create=[
        (
            j.StringFormatter(
                "{dir}/file.txt", dir=j.InputSelector("name_of_output_folder")
            ),
            "contents of file",
        )
    ],
)

if __name__ == "__main__":
    CLT().translate("cwl")