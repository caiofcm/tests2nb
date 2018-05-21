import pytest
import os
import sys
from tests2nb import tests2nb
from py2nb import tools, reader, converter


def from_dir_file(rel_path):
	return os.path.join(
		os.path.dirname(__file__),
		rel_path)


# def test_read_file_to_tmp():
# 	filepath = os.path.join(os.path.dirname(
# 		__file__), '../samples/test_wallet.py')
# 	tests2nb.from_source_to_modified(filepath)


def test_read_file_convert_to_nb(ref_ipynb):
	filepath = os.path.join(os.path.dirname(
		__file__), '../samples/test_wallet.py')
	tmp_filepath = os.path.join(os.path.dirname(
		__file__), '../samples/my_conv_file.py')
	tests2nb.from_source_to_modified(filepath, tmp_filepath)
	cvt = reader.read(tmp_filepath)
	converter.convert(cvt, 'out.ipynb')
	with open('out.ipynb', 'r') as target:
		out_converted = target.read()
	assert(out_converted == ref_ipynb)
	os.remove(tmp_filepath)


def test_pytest_to_nb(ref_ipynb):
	filepath = os.path.join(
            os.path.dirname(__file__),
            '../samples/test_wallet.py'
        )
	tests2nb.pytests_to_notebook(filepath, 'out.ipynb')
	with open('out.ipynb', 'r') as target:
		out_converted = target.read()
	assert(out_converted == ref_ipynb)

#--------------------------------------------
# 	 fixtures 	 
#--------------------------------------------
@pytest.fixture()
def ref_ipynb():
	tmp_filepath = os.path.join(os.path.dirname(
		__file__), '../samples/out_ref.ipynb')
	with open(tmp_filepath, 'r') as target:
		ref = target.read()
	return ref

def main():
	# test_read_file_convert_to_nb()
	pass

if __name__ == '__main__':
	main()
