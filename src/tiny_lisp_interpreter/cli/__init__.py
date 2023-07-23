# SPDX-FileCopyrightText: 2023-present Adrien-LUDWIG <ludwig.adrien0@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from tiny_lisp_interpreter.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="Tiny-Lisp-Interpreter")
def tiny_lisp_interpreter():
    click.echo("Hello world!")
