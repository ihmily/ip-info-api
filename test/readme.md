```shell
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv
uv pip sync /dev/null --allow-empty-requirements
# uv pip sync NUL --allow-empty-requirements
uv pip install aiohttp
uv pip freeze > ./requirements.txt

uv run python ./test_apis.py
uv run python ./test_apis.py -c
uv run python ./test_apis.py -c 8
uv run python ./test_apis.py -c 32 -v
uv run python ./test_apis.py -c 512 -v --clear
```