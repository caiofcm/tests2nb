import pytest
import os
import sys
from tests2nb import tests2nb
from py2nb import tools, reader, converter

def test_read_file_to_tmp():
	filepath = os.path.join(os.path.dirname(__file__), '../samples/test_wallet.py')
	tests2nb.from_source_to_modified(filepath)

def test_read_file_convert_to_nb():
	filepath = os.path.join(os.path.dirname(__file__), '../samples/test_wallet.py')
	tmp_filepath = os.path.join(os.path.dirname(__file__), '../samples/my_conv_file.py')
	tests2nb.from_source_to_modified(filepath, tmp_filepath)
	cvt = reader.read(tmp_filepath)
	converter.convert(cvt, 'out.ipynb')
	assert(True == True)
