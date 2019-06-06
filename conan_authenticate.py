#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans.client.conan_api import Conan

if __name__ == "__main__":
    password = os.getenv("CONAN_PASSWORD", None)
    if not password:
        raise Exception("Password can not be empty.")

    remote_name = "bintray"
    remote_url = os.getenv("CONAN_REMOTE", "https://api.bintray.com/conan/uilianries/conan")
    name = os.getenv("CONAN_USERNAME", "uilianries")

    conan_api, _, _ = Conan.factory()

    for _ in range(1000):
        conan_api.remote_add(remote_name, remote_url)
        conan_api.authenticate(name, password, remote_name)
        conan_api.remote_remove(remote_name)
