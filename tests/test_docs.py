import os

import pytest

from util import files_from_folder, run_ipynb, ROOT

DOCS = os.path.join(ROOT, "source")

OVERWRITE = True

SKIP = ["parallelization.ipynb", "video.ipynb", "modact.ipynb", "dascmop.ipynb"]

IPYNBS = [e for e in files_from_folder(DOCS, regex='**/*.ipynb', skip=SKIP) if ".ipynb_checkpoints" not in e]


@pytest.mark.parametrize('ipynb', IPYNBS)
def test_docs(ipynb):
    run_ipynb(ipynb, overwrite=OVERWRITE, remove_trailing_empty_cells=True)
    assert True

