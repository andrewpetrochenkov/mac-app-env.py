#!/usr/bin/env python
"""set macOS app environment variables"""
import click
import mac_app_env
import env_file
import os

MODULE_NAME = "mac_app_env"
USAGE = 'python -m %s env_path app ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('env_path', required=True)
@click.argument('apps', nargs=-1, required=True)
def _cli(env_path, apps):
    for app in apps:
        path = os.path.join(app, "Contents", "Info.plist")
        data = mac_app_env.plist.read(path)
        data["LSEnvironment"] = env_file.get(env_path)
        mac_app_env.plist.write(path, data)


if __name__ == "__main__":
    _cli()
