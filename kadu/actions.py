#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    #fix install path for sdk
    pisitools.dosed("cmake/FindKadu.cmake", "(\s+set\s\(KADU_SDK_DIR\s\$\{CMAKE_INSTALL_PREFIX\}\/)(sdk\))", r"\1share/kadu/\2")
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "THANKS")
