import ast
from . import unparse
import sys

def read_ast(s):
	expr_ast = ast.parse(s)
	return expr_ast

def from_ast_to_source(ast_nodes, file_path = 'tmp_cnv.py'):
	with open(file_path, 'w') as target:
		unparse.Unparser(ast_nodes, target)

def from_source_to_modified(filepath, output_path = None):
	with open(filepath) as target:
		file_read = target.read()
	expr_ast = read_ast(file_read)
	ast_node_mod = ast_test_func_prepend_docstring(expr_ast)
	ast_node_mod = ast.fix_missing_locations(ast_node_mod)
	from_ast_to_source(ast_node_mod, output_path)

#--------------------------------------------
# 	 NODE MODIFIERS 	 
#--------------------------------------------

class TestFunctions(ast.NodeTransformer):

	def __init__(self, remove_docstring=True, fun_prefixed_text=None):
		self.remove_docstring = remove_docstring
		self.fun_prefixed_text = fun_prefixed_text or format_test_name

	def visit_FunctionDef(self, node):
		if node.name.startswith('test_'):
			node_prepend = create_markdowncell_node(node, self.fun_prefixed_text)
			node_no_ds = remove_docstring_from_node(node)
			return [node_prepend, node_no_ds]
		return node

def ast_test_func_prepend_docstring(ast_expr):
	astIsFunc = TestFunctions().visit(ast_expr)
	return astIsFunc


def create_markdowncell_node(node, fun_prefixed_string=None):
	if fun_prefixed_string is None:
		text = format_test_name(node)
	else:
		text = fun_prefixed_string(node)

	docstring = ast.get_docstring(node, False)
	if docstring is not None:
		text += docstring
	
	node_prepend = create_node_ExpStr_markdowncell(text)
	return node_prepend



#--------------------------------------------
# 	 HELPERS 	 
#--------------------------------------------
def format_test_name(fun_node):
	name_cap = separate_and_capitalize_first_letter_test_name(fun_node.name)
	text = '## {}\n'.format(name_cap)
	return text

def separate_and_capitalize_first_letter_test_name(name):
	name_splt = name.split('_')
	text = ' '.join(name_splt)
	return text.title()

def create_node_ExpStr_markdowncell(string):
	# fmt = "<markdowncell>\n{}".format(string)
	fmt = "\"\"\"\n{}".format(string)
	return create_Expr_Str_node(fmt)

def create_Expr_Str_node(string):
	return ast.fix_missing_locations(ast.Expr(ast.Str(string)))


def remove_docstring_from_node(node):
	docstring = ast.get_docstring(node)
	if docstring:
		del node.body[0]
	return node
