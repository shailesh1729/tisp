jupyter-book clean ../book
jupyter-book build ../book
ghp-import -n -p -f ../book/_build/html
