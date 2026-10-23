Make sure to fill in the variables in `auto_app_update.py` before running the example. (`user_id` can also be in its `int` form)
```shell
python3 -m venv .venv
.venv/bin/pip install "pypjsekai[appinfo]"

.venv/bin/python auto_app_update.py
```
The `systemInfo` of the game should be printed as you run this example.
