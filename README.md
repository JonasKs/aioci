## aioci

`aioci` was a proof of concept fork of `pyaci`, with typing, asyncio and PEP8 in mind.

You can read more about it in the [original documentation](http://aioci.readthedocs.io/en/latest/)

Work to be done:
- [x] rewrite to be more pythonic 
  - [x] function names should be `up()`, `.json`, `.dn`, `.parent` and **not** `Up()`, `.Json`, `.Dn`, `.Parent`
  - [x] files should be formatted by black
- [ ] implement typing
  - [x] typing for configurable objects
    - [x] Automatically generate stub file (see [`scripts/`](scripts))
  - [ ] typing for all objects*
- [x] remove clutter, such as scripts for generating meta, flask implementations etc.
- [ ] rewrite tests from `nose` / `nosetests` to pytest
- [ ] rewrite to asyncio
  - [ ] requests to httpx / aiohttp
  - [ ] websocket and threading -> websockets / aiohttp


*Only configurable objects has types at the moment. This is due to the 2.6mb cap PyCharm has on file-inspection.
The stub file (`aioci/core.pyi`) generated for _all_ objects is about 8.6mb, compared to the ~1mb with only 
configurable objects. 
All objects could be implemented by updating PyCharm intellisense max filesize to 10mb
(`idea.max.intellisense.filesize=10000000`), but that will not be done until it is needed.  
Another idea could be to utilize imports differently, but I have not experienced with this yet. 
See [docs](https://typing.readthedocs.io/en/latest/source/stubs.html)
