<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-app-env.svg?longCache=True)](https://pypi.org/project/mac-app-env/)
[![](https://img.shields.io/pypi/v/mac-app-env.svg?maxAge=3600)](https://pypi.org/project/mac-app-env/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-app-env.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-app-env.py/)

#### Installation
```bash
$ [sudo] pip install mac-app-env
```

#### How it works
`.env` file
```bash
PATH=path/to/custom/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

`<app>/Contents/Info.plist`
```xml
<key>LSEnvironment</key>
<dict>
     <key>PATH</key>
     <string>path/to/custom/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
</dict>
```

#### Executable modules
usage|`__doc__`
-|-
`python -m mac_app_env env_path app ...` |set macOS app environment variables

#### Examples
```bash
$ find . "*.app" | xargs python -m mac_app_env .env
```

paths with spaces:
```bash
$ find . "*.app" -exec python -m mac_app_env .env {} \;
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>