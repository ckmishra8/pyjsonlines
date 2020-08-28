pyjsonlines
===========

A Python library to convert `Json <https://www.json.org/json-en.html>`__
to `Jsonlines <http://jsonlines.org/>`__ and
`Jsonlines <http://jsonlines.org/>`__ to
`Json <https://www.json.org/json-en.html>`__. This library is helpful to
convert `ndjson <http://ndjson.org/>`__ to
`Json <https://www.json.org/json-en.html>`__ and vice versa too.

Installation
------------

User can install ``pyjsonlines`` either via the `Python Package Index
(PyPI) <https://pypi.org/>`__ or from
`source <https://github.com/thisischandanmishra/pyjsonlines>`__.

Install using pip
~~~~~~~~~~~~~~~~~

::

    pip install pyjsonlines

How to use
----------

This library contains two APIs to convert data:

1. json2jsonl(in\_take, file=None)
2. jsonl2json(in\_take, file=None)

json2jsonl(in\_take, file=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User should use this API incase to convert Json to Jsonlines or ndjson.
User has to pass valid Json to this API, which is passed to ``in_take``
argument. User can either pass a Json file or Json object to convert to
Jsonlines. The other argument, ``file`` is optional. It's required when
user wants to store the converted Jsonlines or ndjson data to a file.
Full path of file along with name is suggested to pass.

jsonl2json(in\_take, file=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User should use this API incase to convert Jsonlines or ndjson to Json.
User has to pass valid Jsonlines to this API, which is passed to
``in_take`` argument. User can either pass a Jsonlines file or Jsonlines
object to convert to Json. The other argument, ``file`` is optional.
It's required when user wants to store the converted Json data to a
file. Full path of file along with name is suggested to pass.
