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

from typing import Optional, List
import janis_core as j

# Although not preferred, you can use Python primitives, and typing
# annotations in place of the Janis types:

#   str     - j.String()
#   int     - j.Int()
#   float   - j.Float()
#   bool    - j.Boolean()
#
#   typing.Optional[str]    - j.String(optional=True)
#   typing.List[str]        - j.Array(j.String())


workflow = j.WorkflowBuilder("typing_tests")

workflow.input("my_string_input", j.String())
workflow.input("my_string_input", str)

workflow.input("my_optional_str_input", j.String(optional=True))
workflow.input("my_optional_str_input", Optional[str])

workflow.input("my_list_of_strings_input", j.Array(j.String()))
workflow.input("my_list_of_strings_input", List[str])

workflow.input("my_optional_list_of_strings", j.Array(j.String(), optional=True))
workflow.input("my_optional_list_of_strings", Optional[List[str]])

workflow.input("my_list_of_optional_strings", j.Array(j.String(optional=True)))
workflow.input("my_list_of_optional_strings", List[Optional[str]])
