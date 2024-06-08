# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

import os
from datetime import datetime

from spectre.utils import datetime_helpers, file_helpers
from cfg import CONFIG

class ChunkExt:
    def __init__(self, chunk_start_time: str, tag: str, ext: str):
        self.chunk_start_time = chunk_start_time
        self.tag = tag
        self.ext = ext
        self.file = f"{self.chunk_start_time}_{tag}.{self.ext}"
        self.chunk_dir = datetime_helpers.build_chunks_dir(self.chunk_start_time)
        self.chunk_start_datetime = datetime.strptime(chunk_start_time, CONFIG.default_time_format)


    def get_path(self) -> str:
        return os.path.join(self.chunk_dir, f"{self.chunk_start_time}_{self.tag}{self.ext}")
    

    def exists(self) -> bool:
        return os.path.exists(self.get_path())
    

    def delete_self(self, doublecheck_delete = True, ignore_file_existance = True) -> None:
        if not self.exists():
            return
        else:
            if doublecheck_delete:
                file_helpers.doublecheck_delete(self.get_path())
            try:
                os.remove(self.get_path())
            except FileNotFoundError:
                if ignore_file_existance:
                    pass
                else:
                    raise
        return
    