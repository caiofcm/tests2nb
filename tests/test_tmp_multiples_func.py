import ast
# import unparse
import sys
import pytest
from tests2nb import tests2nb


@pytest.fixture()
def string_source_multiple_test_docstring():
	STRING = '''
import numpy as np
def test_default_initial_amount():
    """
    A
    """
    a = 5
    assert(a == 5)

""" I am a global scopped 
docstring
"""
def test_no_docstring():
    assert(np.pi < 3.15)

def i_am_not_a_test():
	a = 2
	B = np.ones(5)
	'''
	return STRING


#--------------------------------------------
# 	 AST READ
#--------------------------------------------
def test_read_ast(string_source_multiple_test_docstring):
	s = string_source_multiple_test_docstring
	ast_from_code = tests2nb.read_ast(s)
	print(ast.dump(ast_from_code))
	assert(isinstance(ast_from_code, ast.Module))


#--------------------------------------------
# 	 MODIFY AST 	 
#--------------------------------------------

@pytest.fixture()
def ast_multiple_test_docstring(string_source_multiple_test_docstring):
	s = string_source_multiple_test_docstring
	ast_from_code = tests2nb.read_ast(s)
	return ast_from_code


def test_modify_ast_tree_with_docstring(ast_multiple_test_docstring):
	ast_expr = ast_multiple_test_docstring
	ast_modified = tests2nb.ast_test_func_prepend_docstring(ast_expr)

	assert(isinstance(ast_expr, ast.Module))
	assert(len(ast_modified.body) == 7)
	assert(isinstance(ast_modified.body[1], ast.Expr))
	assert(isinstance(ast_modified.body[1].value, ast.Str))
	assert(isinstance(ast_modified.body[4].value,
				ast.Str) and '<codecell>' in ast_modified.body[4].value.s)

#--------------------------------------------
# 	 AST TO SOURCE 	 
#--------------------------------------------

@pytest.fixture()
def ast_multiple_test_docstring_modified(ast_multiple_test_docstring):
	ast_nodes = ast_multiple_test_docstring
	ast_modified = tests2nb.ast_test_func_prepend_docstring(ast_nodes)
	return ast_modified

def test_ast_unparse_modified(ast_multiple_test_docstring_modified):
	a = ast_multiple_test_docstring_modified
	tests2nb.from_ast_to_source(a)
