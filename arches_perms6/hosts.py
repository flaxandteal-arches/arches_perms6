import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        re.sub(r"_", r"-", r"arches_perms6"), "arches_perms6.urls", name="arches_perms6"
    ),
)
