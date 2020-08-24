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

HelloWorldTool = j.CommandToolBuilder(
    tool="HelloWorldTool",
    container=None,
    version="development",
    base_command="echo",
    inputs=[j.ToolInput("inp", j.String, position=0, default="Hello, World!")],
    outputs=[j.ToolOutput("out", j.String, selector=j.standard.ReadContents(j.Stdout()))],
)

# as there is no container, you need to provide "allow_empty_containers=True" to the translate method:
HelloWorldTool.translate("wdl", allow_empty_container=True)

# OR (bash):
# $ janis translate --allow-empty-container hello wdl
