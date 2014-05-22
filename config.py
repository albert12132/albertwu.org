import os
import sys

# path for repo -- best not to change this
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# filepaths for apps with templates
TEMPLATE_DIRS = [
    BASE_PATH,
    os.path.join(BASE_PATH, 'cs61a'),
    os.path.join(BASE_PATH, 'review'),
    os.path.join(BASE_PATH, 'notes'),
    os.path.join(BASE_PATH, 'blog'),
]

# config variables used by templates
# for development, change the '/' to the directory of published
# materials
CONFIGS = {
    'MASTER_DIR': '',
    'CS61A_DIR': '/cs61a',
    'REVIEW_DIR': '/cs61a/review',
    'NOTES_DIR': '/cs61a/notes',
    'BLOG_DIR': '/blog',
}
