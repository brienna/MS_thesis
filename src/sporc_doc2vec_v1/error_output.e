==> Error: Class constructor failed for package 'aweits.py-smart-open'.

Caused by:
ValueError: FilePatch: Patch file tkinter.patch for package builtin.python does not exist.
  File "/.autofs/tools/spack/lib/spack/spack/repo.py", line 904, in get
    return package_class(spec)
  File "/.autofs/tools/spack/lib/spack/spack/package.py", line 561, in __init__
    spack.repo.get(self.extendee_spec)._check_extendable()
  File "/.autofs/tools/spack/lib/spack/spack/repo.py", line 1205, in get
    return path.get(spec)
  File "/.autofs/tools/spack/lib/spack/spack/repo.py", line 90, in converter
    return function(self, spec_like, *args, **kwargs)
  File "/.autofs/tools/spack/lib/spack/spack/repo.py", line 664, in get
    return self.repo_for_pkg(spec).get(spec)
  File "/.autofs/tools/spack/lib/spack/spack/repo.py", line 90, in converter
    return function(self, spec_like, *args, **kwargs)
  File "/.autofs/tools/spack/lib/spack/spack/repo.py", line 902, in get
    package_class = self.get_pkg_class(spec.name)
  File "/.autofs/tools/spack/lib/spack/spack/repo.py", line 1097, in get_pkg_class
    module = self._get_pkg_module(pkg_name)
  File "/.autofs/tools/spack/lib/spack/spack/repo.py", line 1071, in _get_pkg_module
    prepend=_package_prepend)
  File "/.autofs/tools/spack/lib/spack/spack/util/imp/imp_importer.py", line 42, in load_source
    return imp.load_source(full_name, path, f)
  File "/tools/spack/opt/spack/linux-rhel7-x86_64/gcc-7.4.0/py-smart-open-1.8.0-zmtznsigsx4xfmwhx7dv3pcstqt6qyvc/.spack/repos/builtin/packages/python/package.py", line 25, in <module>
    """The Python programming language."""
  File "/.autofs/tools/spack/lib/spack/spack/directives.py", line 153, in __init__
    directive(cls)
  File "/.autofs/tools/spack/lib/spack/spack/directives.py", line 489, in _execute_patch
    ordering_key=ordering_key)
  File "/.autofs/tools/spack/lib/spack/spack/patch.py", line 138, in __init__
    raise ValueError(msg)

Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
Traceback (most recent call last):
  File "script.py", line 32, in <module>
    from helper import train_and_evaluate
  File "/home/bkh4324/train_doc2vec_abstracts/helper.py", line 5, in <module>
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
ModuleNotFoundError: No module named 'gensim'
srun: error: skl-a-47: tasks 0-19: Exited with exit code 1
