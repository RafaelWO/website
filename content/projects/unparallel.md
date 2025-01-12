+++
date = '2024-05-12'
draft = false
title = 'Unparallel'
disableReadingTime = true
+++

**Create async web requests via Python in no time** [[GitHub]](https://github.com/RafaelWO/unparallel)

<!--more-->

With Unparallel you can easily create thousands of web requests in an efficient way leveraging Python's async capabilities.

Unparallel is built on top of [HTTPX](https://github.com/encode/httpx/) and aims to support its rich set of features.

## Installation

```bash
pip install unparallel
```

## Example
A simple example of doing several GET requests to an HTTP web service:

```python
import asyncio

from unparallel import up


async def main():
    urls = [f"https://httpbin.org/get?i={i}" for i in range(5)]
    results = await up(urls)
    print([item["args"] for item in results])


if __name__ == "__main__":
    asyncio.run(main())
```

This prints:
```
Making async requests: 100%|███████████| 5/5 [00:00<00:00,  9.98it/s]
[{'i': '0'}, {'i': '1'}, {'i': '2'}, {'i': '3'}, {'i': '4'}]
```

---

Check out the [docs](https://rafaelwo.github.io/unparallel/latest/) for more information.
