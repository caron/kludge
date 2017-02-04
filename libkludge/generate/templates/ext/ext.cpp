{############################################################################}
{# Copyright (c) 2010-2017 Fabric Software Inc. All rights reserved.        #}
{############################################################################}
//////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////
//
// C++ definitions for {{ext.name}} extension
// Automatically generated by KLUDGE
// *** DO NOT EDIT ***
//
//////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////
// Topmosts
//////////////////////////////////////////////////////////////////////////////

{% for cpp_topmost in ext.cpp_topmosts %}
{{ cpp_topmost }}
{% endfor %}

//////////////////////////////////////////////////////////////////////////////
// Inclusion of FabricEDK and EDK initialization
//////////////////////////////////////////////////////////////////////////////

#include <FabricEDK.h>

#define FABRIC_EDK_EXT_{{ext.name}}_DEPENDENT_EXTS \
  { \
    { 0, 0, 0, 0, 0 } \
  }
IMPLEMENT_FABRIC_EDK_ENTRIES({{ext.name}})

//////////////////////////////////////////////////////////////////////////////
// Includes of C++ global headers for extension
//////////////////////////////////////////////////////////////////////////////

// To include C++ global headers in your extension, add to
// gen_script.kludge.kl:
//
// ext.add_cpp_angled_include('string')  # -> #include <string>
// ext.add_cpp_quoted_include('hello.h')  # -> #include "hello.h"
//
// You can also include headers on a per-type and per-function basis.
//
{% for cpp_include in ext.cpp_includes %}
{% if cpp_include.is_angled %}
#include <{{cpp_include.filepath}}>
{% else %}
#include "{{cpp_include.filepath}}"
{% endif %}
{% endfor %}

//////////////////////////////////////////////////////////////////////////////
// Prologs
//////////////////////////////////////////////////////////////////////////////

{% for cpp_prolog in ext.cpp_prologs %}
{{ cpp_prolog }}
{% endfor %}

//////////////////////////////////////////////////////////////////////////////
// Forwards
//////////////////////////////////////////////////////////////////////////////

{% for decl in ext.decls %}
{{ decl.render('fwds', 'cpp') }}
{% endfor %}

//////////////////////////////////////////////////////////////////////////////
// Definitions
//////////////////////////////////////////////////////////////////////////////

{% for decl in ext.decls %}
{{ decl.render('defns', 'cpp') }}
{% endfor %}

//////////////////////////////////////////////////////////////////////////////
// Implementations
//////////////////////////////////////////////////////////////////////////////

{% for decl in ext.decls %}
{{ decl.render('impls', 'cpp') }}
{% endfor %}

//////////////////////////////////////////////////////////////////////////////
// Epilogs
//////////////////////////////////////////////////////////////////////////////

{% for cpp_epilog in ext.cpp_epilogs %}
{{ cpp_epilog }}
{% endfor %}
