l1 = "MIT OR GPL-2.0-or-later OR (FSFUL AND BSD-2-Clause)"
l2 = "GPL-3.0-only WITH Classpath-Exception-2.0 OR BSD-3-Clause"
l3 = "This software may only be obtained by sending the author a postcard, and then the user promises not to redistribute it."
l4 = "LicenseRef-Proprietary AND LicenseRef-Public-Domain"

import tokenize
from io import StringIO
from pprint import pprint

for l in (l1, l2, l3, l4):
    i = StringIO(l)
    t = tokenize.generate_tokens(i.readline)
    # a = next(t)
    pprint(list(t))
    # breakpoint()
    break
