#!/usr/bin/env python
##############################################################################
##############################################################################
##
## py.test driver for {{ext.name}} extension
## Automatically generated by KLUDGE
## *** DO NOT EDIT ***
##
##############################################################################
##############################################################################

import os, subprocess, difflib

kl_env = os.environ.copy()
kl_env['FABRIC_EXTS_PATH'] = '.' + os.pathsep + kl_env['FABRIC_EXTS_PATH']
with open('{{ext.name}}.test.out') as expected_kl_output_file:
  expected_kl_output = expected_kl_output_file.read().splitlines()
actual_kl_output = subprocess.check_output(
  ['kl', '{{ext.name}}.test.kl'],
  env = kl_env,
  ).splitlines()
difflines = difflib.unified_diff(expected_kl_output, actual_kl_output)
diffline_count = 0
for diffline in difflines:
  print diffline
  diffline_count += 1
assert diffline_count == 0
print "{{ext.name}} extension tests passed!"