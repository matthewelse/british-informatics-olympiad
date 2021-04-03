/* Just a python wrapper for vision.hh */

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "vision.hh"

namespace py = pybind11;

PYBIND11_MODULE(vision_py, m) {
  m.doc() = "DFS solution to vision.";

  m.def("solve", &solve, "A function which solves the vision problem.");
}

/*
<%
cfg['dependencies'] = ['vision.hh']

setup_pybind11(cfg)
%>
*/
