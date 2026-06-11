"""
ophix_admin_settings.validators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Security validators for ServerSettings fields that reach CSS or HTML output.

Kept intentionally separate from admin_interface.validators so this package
remains independent of ophix-admin-interface.  The color validator is
equivalent to the one in admin_interface — same rules, no shared import.
"""

import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# ---------------------------------------------------------------------------
# Compiled patterns
# ---------------------------------------------------------------------------

_HEX_COLOR_RE = re.compile(
    r"^#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$"
)
_SERVER_TITLE_RE = re.compile(r"^[^{}<>;\\]*$", re.UNICODE)
_ENV_NAME_RE = re.compile(r"^[\w\s\-]*$", re.UNICODE)

# ---------------------------------------------------------------------------
# Error messages
# ---------------------------------------------------------------------------

_COLOR_MSG = _(
    "Enter a hex colour code — e.g. #0096c7 (6 digits) or #09c (3 digits). "
    "Named colours and CSS functions are not accepted."
)
_SERVER_TITLE_MSG = _(
    "Server title contains invalid characters. "
    "Use letters, numbers, spaces, and standard punctuation."
)
_ENV_NAME_MSG = _(
    "Environment name may only contain letters, numbers, spaces, and hyphens — "
    "e.g. Production, Staging, Dev-EU."
)

# ---------------------------------------------------------------------------
# Validator functions
# ---------------------------------------------------------------------------

# ColorFields on ServerSettings that are emitted as CSS variables.
SETTINGS_COLOR_FIELDS = (
    "env_color",
    "env_color_dark",
    "env_text_color",
    "env_text_color_dark",
)


def validate_css_color(value):
    """Accept only empty string or a hex colour (#RGB / #RRGGBB / #RRGGBBAA).

    Leading and trailing whitespace is stripped before checking — a field that
    contains only spaces is treated as blank (allowed), and a value like
    ' #ddab52 ' passes the same as '#ddab52'.
    """
    if not value:
        return
    if not _HEX_COLOR_RE.match(value.strip()):
        raise ValidationError(_COLOR_MSG)


def validate_server_title(value):
    """Accept printable text; deny characters that enable HTML/CSS injection."""
    if not value:
        return
    if not _SERVER_TITLE_RE.match(value):
        raise ValidationError(_SERVER_TITLE_MSG)


def validate_env_name(value):
    """Accept only letters, digits, spaces, and hyphens."""
    if not value:
        return
    if not _ENV_NAME_RE.match(value):
        raise ValidationError(_ENV_NAME_MSG)
