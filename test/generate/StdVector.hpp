//
// Copyright (c) 2010-2016, Fabric Software Inc. All rights reserved.
//

#pragma once

#include <string>
#include <vector>

inline float ReturnSecond(
  std::vector<float> const &vals
  )
{
  return vals[1];
}

inline char const * ReturnSecondSecond(
  std::vector< std::vector<char const *> > const &vals
  )
{
  return vals[1][1];
}

inline std::vector< std::vector<std::string> > ReturnStringArrayArray()
{
  std::vector<std::string> b;
  b.push_back("hello");
  b.push_back("there");
  b.push_back("my");
  b.push_back("friend");

  std::vector< std::vector<std::string> > a;
  a.push_back(b);
  a.push_back(b);
  a.push_back(b);

  return a;
}

typedef std::vector< std::string > StringVector;

StringVector GetStringVector()
{
  StringVector s;
  s.push_back("hello");
  s.push_back("world");
  return s;
}

void AppendToStringVector( std::vector<std::string> &v )
{
  v.push_back("appended string");
}