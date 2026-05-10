# """
# pages/path_setup.py
# ====================
# Adds the `pages/` folder to sys.path so that imports like
#     from services.auth_service import ...
#     from data.snowpark_client  import ...
# work correctly when Streamlit runs pages/main.py.

# Import this as the VERY FIRST LINE of pages/main.py, before
# any services/ or data/ imports.
# """

# import sys
# import os

# # __file__ is always pages/path_setup.py
# # so dirname(__file__) is always the pages/ folder — exactly what we need
# _PAGES_DIR = os.path.dirname(os.path.abspath(__file__))

# if _PAGES_DIR not in sys.path:
#     sys.path.insert(0, _PAGES_DIR)

import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to project root
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

sys.path.insert(0, PROJECT_ROOT)
