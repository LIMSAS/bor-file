# -*- coding: utf-8 -*-
import pytest
from pytest_cases import pytest_fixture_plus

import bor

from . import INPUT_BOR_FILES, INPUT_FILES_DIR
from .utils import assert_same_files


@pytest_fixture_plus(
    scope="function",
    params=INPUT_BOR_FILES,
    ids=[p.relative_to(INPUT_FILES_DIR).as_posix() for p in INPUT_BOR_FILES],
)
def bor_file(request):
    if request.param.as_posix().lower().endswith(".bor"):
        bor_file = bor.read(request.param)
        return bor_file


def test_csv_export(bor_file, tmp_path):
    csv_output_filename = tmp_path / "output.csv"
    bor_file.to_csv(csv_output_filename)
    assert_same_files(
        csv_output_filename,
        bor_file._source_file.with_suffix(".csv")
    )
