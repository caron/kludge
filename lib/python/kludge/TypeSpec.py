class KLTypeSpec:

  def __init__(self, base, suffix):
    self.base = base
    self.suffix = suffix

  @property
  def compound(self):
    return self.base + self.suffix

class EDKTypeSpec:

  def __init__(self, name):
    self.name = name

class CPPTypeSpec:

  def __init__(self, cpp_type_name, cpp_type_expr):
    self.name = cpp_type_name
    self.expr = cpp_type_expr

class TypeSpec:

  def __init__(
    self,
    kl_base,
    kl_suffix,
    edk_name,
    cpp_type_spec,
    child_values,
    ):
    self.kl = KLTypeSpec(kl_base, kl_suffix)
    self.edk = EDKTypeSpec(edk_name)
    self.cpp = cpp_type_spec
    self.child_values = child_values

  @staticmethod
  def builder(
    kl_base,
    kl_suffix,
    edk_name,
    child_values,
    ):
    return lambda cpp_type_spec: TypeSpec(
      kl_base,
      kl_suffix,
      edk_name,
      cpp_type_spec,
      child_values,
      )

class SimpleTypeSpec(TypeSpec):

  def __init__(
    self,
    kl_name,
    cpp_type_spec,
    ):
    TypeSpec.__init__(
      self,
      kl_name,
      "",
      kl_name,
      cpp_type_spec,
      [],
      )

  @staticmethod
  def builder(kl_name):
    return lambda cpp_type_spec: SimpleTypeSpec(
      kl_name,
      cpp_type_spec,
      )
