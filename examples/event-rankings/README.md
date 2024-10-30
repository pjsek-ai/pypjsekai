Make sure to fill in the variables in `event-rankings.py` before running the example. (`user_id` can also be in its `int` form)
```python
key = b""
iv = b""
app_version=""
app_hash=""
user_id = ""
credential = ""
```
```shell
python3 -m venv .venv
.venv/bin/pip install pypjsekai

.venv/bin/python event-rankings.py
```
The rankings should be printed in the console as you run this example.
