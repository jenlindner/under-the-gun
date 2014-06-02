# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "under-the-gun"

# Descriptive title of project
TITLE = "Under the Gun"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Google spreadsheet key
SPREADSHEET_KEY = "1-4LjTE4tRvyPybuR3UCe_y5Qij9Ro4muXP1MlA6ZIBI"

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be 
# used.
# CONTEXT_SOURCE_FILE = ""

# S3 bucket configuration
#S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
#}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'under-the-gun',
    'title': 'Under the Gun'
}