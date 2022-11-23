# html_to_ipynb

This script converts the html rendering of a Jupyter Notebook back into its Jupyter Notebook form. 

## Usage

```
python html_to_ipynb.py /path/to/html/input.html /path/to/notebook/output.ipynb
```

## Caveats

This script relies on the DOM construction being equivalent to the *default* output from Jupyter server when notebooks are converted to html. It may or may not work with your particular file.

## Attribution
This script was adapted from this StackOverflow answer: https://stackoverflow.com/questions/28972614/jupyter-ipython-notebook-convert-an-html-notebook-to-ipynb
