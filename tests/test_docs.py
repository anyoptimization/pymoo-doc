import os

import pytest

from util import files_from_folder, run_ipynb, ROOT

DOCS = os.path.join(ROOT, "source")

SKIP = ["parallelization.ipynb", "video.ipynb", "modact.ipynb", "dascmop.ipynb", "constraints.ipynb"]

IPYNBS = [e for e in files_from_folder(DOCS, regex='**/*.ipynb', skip=SKIP) if ".ipynb_checkpoints" not in e]


@pytest.mark.parametrize('ipynb', IPYNBS)
def test_docs(ipynb, pytestconfig):
    overwrite = pytestconfig.getoption("overwrite")
    run_ipynb(ipynb, overwrite=overwrite, remove_trailing_empty_cells=True)
    assert True

