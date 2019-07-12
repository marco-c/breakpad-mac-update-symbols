#!/usr/bin/env python
# Copyright 2015 Ted Mielczarek. See the LICENSE
# file at the top-level directory of this distribution.
from __future__ import print_function

import os
import sys
import reposadolib.reposadocommon as reposadocommon
reposadocommon.get_main_dir = lambda: '/home/worker/venv/bin/'

products = reposadocommon.get_product_info()
args = []
for product_id, p in products.iteritems():
  t = p['title']
  #p['CatalogEntry']['Packages']
  if t.startswith('OS X') or t.startswith('Mac OS X') or t.startswith('macOS'):
    args.append('--product-id=' + product_id)
  else:
    print('Skipping %r for repo_sync' % t, file=sys.stderr)
if 'JUST_ONE_PACKAGE' in os.environ:
  args = args[:1]

print(' '.join(args))
