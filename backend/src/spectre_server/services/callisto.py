# SPDX-FileCopyrightText: © 2024-2025 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Tuple
from datetime import date

from spectre_core.logs import log_call
from spectre_core import wgetting


@log_call
def get_instrument_codes() -> list[str]:
    """Get all defined e-Callisto network station codes."""
    return [code.value for code in wgetting.CallistoInstrumentCode]


@log_call
def download_callisto_data(
    instrument_codes: list[str],
    year: int,
    month: int,
    day: int,
) -> list[str]:
    """Download and decompress e-Callisto FITS files, saving them as `spectre` batch files.

    :param instrument_codes: A list of e-Callisto station instrument codes.
    :param year: Year of the observation.
    :param month: Month of the observation.
    :param day: Day of the observation.
    :return: A list of file paths of all newly created batch files, as absolute paths within the container's file system.
    """
    codes = [wgetting.CallistoInstrumentCode(code) for code in instrument_codes]

    batch_file_paths = []
    for code in codes:
        # TODO: Remove redundant date object return from `download_callisto_data` return
        new_batch_files, _ = wgetting.download_callisto_data(code, year, month, day)
        batch_file_paths += new_batch_files
    return batch_file_paths
