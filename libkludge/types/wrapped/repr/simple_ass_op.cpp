{############################################################################}
{# Copyright (c) 2010-2017 Fabric Software Inc. All rights reserved.        #}
{############################################################################}
if ( {{this.value_name.edk}}.cpp_ptr )
{
  delete {{this.value_name.edk}}.cpp_ptr;
  {{this.value_name.edk}}.cpp_ptr = NULL;
}
if ( {{param.value_name.edk}}.cpp_ptr )
  {{this.value_name.edk}}.cpp_ptr =
    new ::{{this.base_type_info.lib.name.base}}(
      {{param.value_name.edk}}.cpp_ptr->operator->()
      );
