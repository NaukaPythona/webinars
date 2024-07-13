# ruff: noqa
breakpoint()

from sys import meta_path, path_hooks, path_importer_cache
from devtools import debug

debug(meta_path)
debug(path_hooks)
debug(path_importer_cache)

breakpoint()

for finder in meta_path:
    debug(finder)
    debug([attr for attr in dir(finder) if not attr.startswith("_")])

    breakpoint()
