<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mac-app-env.svg?maxAge=3600)](https://pypi.org/project/mac-app-env/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-app-env.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-app-env.py/actions)

### Installation
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

#### Examples
```bash
$ find . "*.app" | xargs python -m mac_app_env .env
```

paths with spaces:
```bash
$ find . "*.app" -exec python -m mac_app_env .env {} \;
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
