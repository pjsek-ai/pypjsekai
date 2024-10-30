https://docs.mitmproxy.org/stable/overview-installation/#installation-from-the-python-package-index-pypi
```shell
pipx install mitmproxy
pipx inject mitmproxy pypjsekai

mitmweb -s pjsekai-content-view.py
```
You will need to fill in `pjsekai_key` and `pjsekai_iv` in the options before the content-view will work.
`pjsekai_time_travel_destination` allows you to mock the server time returned to the game.
