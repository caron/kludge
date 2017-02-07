#
# Copyright (c) 2010-2017 Fabric Software Inc. All rights reserved.
#

from libkludge.type_info import TypeInfo
from libkludge.type_simplifier import TypeSimplifier
from libkludge.selector import Selector
from libkludge.cpp_type_expr_parser import dir_qual
from libkludge.dir_qual_type_info import DirQualTypeInfo
from libkludge.cpp_type_expr_parser import Void

class VoidTypeSimplifier(TypeSimplifier):

  def __init__(self):
    TypeSimplifier.__init__(self)

  def param_type_name_base(self, type_info):
    assert False

  def param_type_name_suffix(self, type_info):
    assert False

  def result_type_name(self, type_info):
    return ""

  def render_param_pre(self, type_info):
    assert False

  def render_param_post(self, type_info):
    assert False

  def render_result_pre(self, type_info):
    return ""

  def render_result_post(self, type_info):
    return ""

class VoidTypeInfo(TypeInfo):

  def __init__(self, jinjenv):
    TypeInfo.__init__(
      self,
      jinjenv,
      lib_expr=Void(),
      kl_name_base='',
      simplifier=VoidTypeSimplifier(),
      )

  def build_codec_lookup_rules(self):
    tds = TypeInfo.build_codec_lookup_rules(self)
    tds["result"]["*"] = "types/builtin/void/result"
    return tds

class VoidSelector(Selector):

  def __init__(self, ext):
    Selector.__init__(self, ext)

  def get_desc(self):
    return "Void"

  def maybe_create_dqti(self, type_mgr, cpp_type_expr):
    if isinstance(cpp_type_expr, Void):
      return DirQualTypeInfo(
        dir_qual.direct,
        VoidTypeInfo(self.jinjenv)
        )
