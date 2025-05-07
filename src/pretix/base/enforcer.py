from typing import Any

from instrlib.enforcer import EnfPal
from instrlib.logger import Logger
from instrlib.mapping import Mapping
from instrlib.django.handlers import default_handler
from instrlib.schema import Schema

from pretix.base.handlers import none_handler

from pretix.settings import INSTRLIB_EXE, INSTRLIB_FORMULA, INSTRLIB_LOG, INSTRLIB_SIG

# Enforcer

enfpal = EnfPal(INSTRLIB_EXE, INSTRLIB_SIG, INSTRLIB_FORMULA, log_file=INSTRLIB_LOG)

# Mapping

sup_event_map: dict[str | tuple[str, ...], Any] = {
    ('read'):  none_handler,  # noqa: E241
    ('write'): none_handler,  # noqa: E241
    ('input'): default_handler,
}
cau_event_map: dict[str | tuple[str, ...], Any] = {}

mp = Mapping(sup_event_map=sup_event_map, cau_event_map=cau_event_map)

# Logger

logger = Logger(mp, Schema(), enfpal, cache_timeout=30)
