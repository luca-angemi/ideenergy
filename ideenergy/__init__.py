#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2021 Luis López <luis@cuarentaydos.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.


import json
import os

from .client import Client, ClientError, InvalidResponse, LoginFailed


def get_credentials(
    parsedargs=None, credentials=None, environ_prefix="IDEENERGY"
):
    if parsedargs.username:
        return parsedargs.username, parsedargs.password

    credentials = credentials or parsedargs.credentials
    if credentials:
        with open(credentials, mode="r", encoding="utf-8") as fh:
            d = json.loads(fh.read())
        return d["username"], d["password"]

    if environ_prefix:
        environ_prefix = environ_prefix.upper()
        return (
            os.environ.get(f"{environ_prefix}_USERNAME"),
            os.environ.get(f"{environ_prefix}_PASSWORD"),
        )


__all__ = ["Client", "ClientError", "InvalidResponse", "LoginFailed"]
