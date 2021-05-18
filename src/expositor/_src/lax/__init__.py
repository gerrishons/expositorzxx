import os

from jax._src import traceback_util
traceback_util.register_exclusion(os.path.dirname(__file__))
