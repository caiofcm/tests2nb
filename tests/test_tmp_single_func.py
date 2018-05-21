import ast
# import unparse
import sys
import pytest
from tests2nb import tests2nb

@pytest.fixture()
def string_source_single_test_docstring():
	STRING = '''
def test_default_initial_amount():
    """
    A
    """
    a = 5
    a_string = 'aow coco'
    assert(a == 5)
	'''
	return STRING

def test_read_ast(string_source_single_test_docstring):
	s = string_source_single_test_docstring
	ast_from_code = tests2nb.read_ast(s)
	print(ast.dump(ast_from_code))
	assert(isinstance(ast_from_code, ast.Module))
	
@pytest.fixture()
def ast_single_test_docstring(string_source_single_test_docstring):
	s = string_source_single_test_docstring
	ast_from_code = tests2nb.read_ast(s)
	return ast_from_code


def test_create_fmt_string_from_test_name(ast_single_test_docstring):
	ast_expr = ast_single_test_docstring
	node_fun = ast_expr.body[0]
	fmt_str_from_name = tests2nb.format_test_name(node_fun)
	assert('Test Default Initial Amount' in fmt_str_from_name)


def test_modify_ast_tree_with_docstring(ast_single_test_docstring):
	ast_expr = ast_single_test_docstring
	ast_modified = tests2nb.ast_test_func_prepend_docstring(ast_expr)

	assert(isinstance(ast_expr, ast.Module))
	assert(len(ast_modified.body) == 2)
	assert(isinstance(ast_modified.body[0], ast.Expr))
	assert(isinstance(ast_modified.body[0].value, ast.Str))

def test_removed_docstring_from_function(ast_single_test_docstring):
	ast_expr = ast_single_test_docstring
	ast_modified = tests2nb.ast_test_func_prepend_docstring(ast_expr)
	fun_node = ast_modified.body[1]
	assert(isinstance(fun_node, ast.FunctionDef))
	assert(isinstance(fun_node.body[0], ast.Expr) == False)



@pytest.fixture()
def ast_single_test_docstring_modified(ast_single_test_docstring):
	ast_nodes = ast_single_test_docstring
	ast_modified = tests2nb.ast_test_func_prepend_docstring(ast_nodes)
	return ast_modified

def test_ast_unparse_modified(ast_single_test_docstring_modified):
	a = ast_single_test_docstring_modified
	tests2nb.from_ast_to_source(a)
