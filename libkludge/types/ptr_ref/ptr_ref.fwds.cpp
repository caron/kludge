{############################################################################}
{# Copyright (c) 2010-2017 Fabric Software Inc. All rights reserved.        #}
{############################################################################}
{% extends "generate/decl/decl.fwds.cpp" %}
{% block body %}
struct {{decl.type_info.const_ptr.edk.name}};
struct {{decl.type_info.mutable_ptr.edk.name}};
struct {{decl.type_info.const_ref.edk.name}};
struct {{decl.type_info.mutable_ref.edk.name}};

{% endblock body %}
