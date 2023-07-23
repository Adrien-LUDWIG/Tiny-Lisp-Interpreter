# SPDX-FileCopyrightText: 2023-present Adrien-LUDWIG <ludwig.adrien0@gmail.com>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from tiny_lisp_interpreter.cli import tiny_lisp_interpreter

    sys.exit(tiny_lisp_interpreter())
