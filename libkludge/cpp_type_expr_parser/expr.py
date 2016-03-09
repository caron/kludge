import abc
import directions, qualifiers
from dir_qual import DirQual

class CPPTypeExprException(Exception):

  def __init__(self, desc):
    Exception.__init__(desc)

class Type:

  __metaclass__ = abc.ABCMeta

  def __init__(self, qualifier=qualifiers.Unqualified):
    self.qualifier = qualifier

  @property
  def is_const(self):
    return qualifiers.is_const(self.qualifier)
  
  @property
  def is_mutable(self):
    return not self.is_const
  
  @property
  def is_volatile(self):
    return qualifiers.is_volatile(self.qualifier)

  def make_const(self):
    if qualifiers.is_const(self.qualifier):
      return self
    else:
      copy = self.__copy__()
      copy.qualifier = qualifiers.make_const(self.qualifier)
      return copy

  def make_volatile(self):
    if qualifiers.is_volatile(self.qualifier):
      return self
    else:
      copy = self.__copy__()
      copy.qualifier = qualifiers.make_volatile(self.qualifier)
      return copy

  def make_unqualified(self):
    if self.qualifier == qualifiers.Unqualified:
      return self
    else:
      copy = self.__copy__()
      copy.qualifier = qualifiers.Unqualified
      return copy

  def get_desc(self):
    result = self.get_unqualified_desc()
    if self.is_const:
      result += " const"
    if self.is_volatile:
      result += " volatile"
    return result

  @abc.abstractmethod
  def get_unqualified_desc(self):
    pass

  def get_undq_type_expr_and_dq(self):
    if isinstance(self, Direct):
      direction = directions.Direct
      undq_cpp_type_expr = self
    elif isinstance(self, PointerTo):
      direction = directions.Pointer
      undq_cpp_type_expr = self.pointee
    elif isinstance(self, ReferenceTo):
      direction = directions.Reference
      undq_cpp_type_expr = self.pointee
    else:
      raise CPPTypeExprException("internal error")

    qualifier = undq_cpp_type_expr.qualifier
    if qualifier != qualifiers.Unqualified:
      undq_cpp_type_expr = undq_cpp_type_expr.__copy__()
      undq_cpp_type_expr.qualifier = qualifiers.Unqualified

    return (undq_cpp_type_expr, DirQual(direction, qualifier))

  def __str__(self):
    return self.get_desc()

  def __eq__(self, other):
    return type(self) == type(other) \
      and self.qualifier == other.qualifier

  def __ne__(self, other):
    return not self == other

class Direct(Type):

  def __init__(self):
    Type.__init__(self)

class Void(Direct):

  def __init__(self):
    Direct.__init__(self)

  def get_unqualified_desc(self):
    return "void"

  def __copy__(self):
    return Void()

class Bool(Direct):

  def __init__(self):
    Direct.__init__(self)

  def get_unqualified_desc(self):
    return "bool"

  def __copy__(self):
    return Bool()

class Numeric(Direct):

  def __init__(self):
    Direct.__init__(self)

class Integer(Numeric):

  def __init__(self):
    Numeric.__init__(self)
    self.is_signed = True

  def make_unsigned(self):
    self.is_signed = False
    return self

  def make_signed(self):
    self.is_signed = True
    return self

  def get_unqualified_desc(self):
    result = ""
    if not self.is_signed:
      result = "unsigned "
    result += self.get_signed_desc()
    return result

  @abc.abstractmethod
  def get_signed_desc(self):
    pass

  def __eq__(self, other):
    return Numeric.__eq__(self, other) \
      and self.is_signed == other.is_signed

class Char(Integer):

  def __init__(self):
    Integer.__init__(self)

  def get_signed_desc(self):
    return "char"

  def __copy__(self):
    return Char()

class Short(Integer):

  def __init__(self):
    Integer.__init__(self)

  def get_signed_desc(self):
    return "short"

  def __copy__(self):
    return Short()

class Int(Integer):

  def __init__(self):
    Integer.__init__(self)

  def get_signed_desc(self):
    return "int"

  def __copy__(self):
    return Int()

class Long(Integer):

  def __init__(self):
    Integer.__init__(self)

  def get_signed_desc(self):
    return "long"

  def __copy__(self):
    return Long()

class LongLong(Integer):

  def __init__(self):
    Integer.__init__(self)

  def get_signed_desc(self):
    return "long long"

  def __copy__(self):
    return LongLong()

class FloatingPoint(Numeric):

  def __init__(self):
    Numeric.__init__(self)

class Float(FloatingPoint):

  def __init__(self):
    FloatingPoint.__init__(self)

  def get_unqualified_desc(self):
    return "float"

  def __copy__(self):
    return Float()

class Double(FloatingPoint):

  def __init__(self):
    FloatingPoint.__init__(self)

  def get_unqualified_desc(self):
    return "double"

  def __copy__(self):
    return Double()

class Named(Direct):

  def __init__(self, name):
    Direct.__init__(self)
    self.name = name

  def get_unqualified_desc(self):
    return self.name

  def __eq__(self, other):
    return Direct.__eq__(self, other) \
      and self.name == other.name

  def __copy__(self):
    return Named(self.name)

class FixedArrayOf(Direct):

  def __init__(self, element, size):
    Direct.__init__(self)
    self.element = element
    self.size = size

  def get_unqualified_desc(self):
    return "%s[%u]" % (self.element.get_desc(), self.size)

  def __eq__(self, other):
    return Direct.__eq__(self, other) \
      and self.element == other.element \
      and self.size == other.size

  def __copy__(self):
    return FixedArrayOf(self.element, self.size)

class Template(Direct):

  def __init__(self, name, params):
    Direct.__init__(self)
    self.name = name
    self.params = params

  def get_unqualified_desc(self):
    return self.name + "< " + ", ".join(map(
      lambda param: param.get_desc(),
      self.params
      )) + " >"

  def __eq__(self, other):
    return Direct.__eq__(self, other) \
      and self.name == other.name \
      and self.params == other.params

  def __copy__(self):
    return Template(self.name, self.params)

class Indirect(Type):

  def __init__(self, pointee):
    Type.__init__(self)
    self.pointee = pointee

  def __eq__(self, other):
    return Type.__eq__(self, other) \
      and self.pointee == other.pointee

class PointerTo(Indirect):

  def __init__(self, pointee):
    Indirect.__init__(self, pointee)

  def get_unqualified_desc(self):
    return self.pointee.get_desc() + " *"

  def __copy__(self):
    return PointerTo(self.pointee)

class ReferenceTo(Indirect):

  def __init__(self, pointee):
    Indirect.__init__(self, pointee)

  def get_unqualified_desc(self):
    return self.pointee.get_desc() + " &"

  def __copy__(self):
    return ReferenceTo(self.pointee)

def Const(ty):
  return ty.make_const()