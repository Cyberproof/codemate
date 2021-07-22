# pylint: disable=missing-function-docstring
# flake8: noqa: E101, W191, W291, W293

from codemate import Block

DOC_TEMPLATE = '"""\n{content}\n"""\n'

DOC_LINE = "Checks: the following - DOC line@!#$%^&*()"

DOC_LINES = (
    "Checks: the following - DOC line@!#$%^&*()",
    "n2j31k4nbj3hb5t4hrjb 4bn `j34kn24iu2o1hj124n331jbn3jk1b2 ",
    "n2j31k4nbj3hb5t4hrjb 4bn `j34kn24iu2o1hj124n331jbn3jk1b2 \n\n",
    "\t\t\n\n\t\t\n\n",
    "dasdsadwt3et435t457658697809-9654142341`4q23rewr2$!$$%@%^$%^&*^&()",
)

DOC_BLOCK = "\n".join(DOC_LINES)

DOC_COMPLEX = '''
    """
    Checks: the following - DOC line@!#$%^&*()
    n2j31k4nbj3hb5t4hrjb 4bn `j34kn24iu2o1hj124n331jbn3jk1b2 
    n2j31k4nbj3hb5t4hrjb 4bn `j34kn24iu2o1hj124n331jbn3jk1b2 


    		

    		


    dasdsadwt3et435t457658697809-9654142341`4q23rewr2$!$$%@%^$%^&*^&()
    Checks: the following - DOC line@!#$%^&*()
    Checks: the following - DOC line@!#$%^&*()
    n2j31k4nbj3hb5t4hrjb 4bn `j34kn24iu2o1hj124n331jbn3jk1b2 
    n2j31k4nbj3hb5t4hrjb 4bn `j34kn24iu2o1hj124n331jbn3jk1b2 


    		

    		


    dasdsadwt3et435t457658697809-9654142341`4q23rewr2$!$$%@%^$%^&*^&()
    Checks: the following - DOC line@!#$%^&*()
    """
'''.lstrip(
    "\n"
)


def test_single_line():
    block = Block()
    block.add_doc_line(DOC_LINE)
    assert DOC_TEMPLATE.format(content=DOC_LINE) == block.syntax()


def test_remove_single_line():
    block = Block()
    block.add_doc_line(DOC_LINE)
    block.add_doc_line(DOC_LINE)
    block.remove_doc_line(DOC_LINE)
    assert DOC_TEMPLATE.format(content=DOC_LINE) == block.syntax()


def test_multiple_lines():
    block = Block()
    block.add_doc_lines(*DOC_LINES)
    assert DOC_TEMPLATE.format(content=DOC_BLOCK) == block.syntax()


def test_remove_multiple_lines():
    block = Block()
    block.add_doc_lines(*DOC_LINES)
    block.add_doc_lines(*DOC_LINES)
    block.remove_doc_lines(*DOC_LINES)
    assert DOC_TEMPLATE.format(content=DOC_BLOCK) == block.syntax()


def test_single_block():
    block = Block()
    block.add_doc_block(DOC_BLOCK)
    assert DOC_TEMPLATE.format(content=DOC_BLOCK) == block.syntax()


def test_remove_single_block():
    block = Block()
    block.add_doc_block(DOC_BLOCK)
    block.add_doc_block(DOC_BLOCK)
    block.remove_doc_block(DOC_BLOCK)
    assert DOC_TEMPLATE.format(content=DOC_BLOCK) == block.syntax()


def test_multiple_block_and_lines():
    block = Block()
    block.add_doc_block(DOC_BLOCK)
    block.add_doc_line(DOC_LINE)
    block.add_doc_lines(*DOC_LINES)
    block.add_doc_line(DOC_LINE)
    assert DOC_COMPLEX == block.syntax(indent=1)


def test_remove_multiple_block_and_lines():
    block = Block()
    block.add_doc_block(DOC_BLOCK)
    block.add_doc_line(DOC_LINE)
    block.add_doc_lines(*DOC_LINES)
    block.add_doc_line(DOC_LINE)
    block.add_doc_block(DOC_BLOCK)
    block.add_doc_line(DOC_LINE)
    block.add_doc_lines(*DOC_LINES)
    block.add_doc_line(DOC_LINE)
    block.remove_doc_block(DOC_BLOCK)
    block.remove_doc_line(DOC_LINE)
    block.remove_doc_lines(*DOC_LINES)
    block.remove_doc_line(DOC_LINE)
    assert DOC_COMPLEX == block.syntax(indent=1)
