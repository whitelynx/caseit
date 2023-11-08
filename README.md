caseit
======

A simple command-line tool using [stringcase](https://pypi.org/project/stringcase/) to convert text
between different cases. (PascalCase, camelCase, snake_case, kebab-case, etc.)


Setting up
----------

You will need to have [pipenv](https://pipenv.pypa.io/en/latest/) installed.

Then, symlink the `caseit` script into your `$PATH`:
```bash
ln -s $(pwd)/caseit ~/.local/bin/
```


Example
-------

```
$ caseit --kebabcase <<EOF
> ThisWasPascalCase
> this_was_snake_case
> THIS_WAS_CONST_CASE
> This was sentence case.
> EOF
this-was-pascal-case
this-was-snake-case
t-h-i-s--w-a-s--c-o-n-s-t--c-a-s-e
this-was-sentence-case-
```
