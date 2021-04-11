#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os

class LinuxdeployqtConan(ConanFile):
    name = "linuxdeployqt"
    version = "6.0"
    description = "Makes Linux applications self-contained by copying in the libraries and plugins that the application uses, and optionally generates an AppImage. Can be used for Qt and other applications"
    url = "https://github.com/Tereius/conan-linuxdeployqt"
    homepage = "https://github.com/probonopd/linuxdeployqt"
    license = "GPLv3"
    no_copy_source = True
    settings = {"os": ["Linux"], "arch": ["x86", "x86_64"]}

    def source(self):
        tools.download("https://github.com/probonopd/linuxdeployqt/releases/download/6/linuxdeployqt-6-x86_64.AppImage", "linuxdeployqt.AppImage")

    def package(self):
        self.copy("*.AppImage", src=self.source_folder)
        self.run("[ -f linuxdeployqt.AppImage ] && chmod u+x linuxdeployqt.AppImage", cwd=self.package_folder)

    def package_info(self):
        self.output.info('Adding linuxdeployqt to PATH: %s' % self.package_folder)
        self.env_info.path.append(self.package_folder)
