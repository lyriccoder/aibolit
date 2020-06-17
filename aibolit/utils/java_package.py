# The MIT License (MIT)
#
# Copyright (c) 2020 Aibolit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from functools import lru_cache

from typing import List

from aibolit.utils.ast import AST, ASTNodeType
from aibolit.utils.ast_builder import build_ast
from aibolit.utils.java_class import JavaClass


class JavaPackage(AST):
    def __init__(self, filename: str):
        super().__init__(build_ast(filename))

    @property  # type: ignore
    @lru_cache
    def name(self) -> str:
        for compilation_unit_child in self.tree.succ[self.root]:
            if self.tree.nodes[compilation_unit_child]['type'] == \
               ASTNodeType.PACKAGE_DECLARATION:
                for package_declaration_child in self.tree.succ[compilation_unit_child]:
                    if self.tree.nodes[package_declaration_child]['type'] == \
                       ASTNodeType.STRING:
                        return self.tree.nodes[package_declaration_child]['string']

        return '.'  # default package name

    @property  # type: ignore
    @lru_cache
    def java_classes(self) -> List[JavaClass]:
        pass