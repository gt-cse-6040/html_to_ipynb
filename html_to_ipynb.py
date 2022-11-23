from bs4 import BeautifulSoup
import json
import sys

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 3:
        raise ValueError
    else:
        input_path = argv[1]
        output_path = argv[2]

    with open(input_path) as f:
        text = f.read()
    soup = BeautifulSoup(text, 'lxml')
    dictionary = {'nbformat': 4, 'nbformat_minor': 1, 'cells': [], 'metadata': {}}
    for d in soup.findAll("div"):
        if 'class' in d.attrs.keys():
            for clas in d.attrs["class"]:
                if clas in ["text_cell_render", "input_area"]:
                    # code cell
                    if clas == "input_area":
                        cell = {}
                        cell['metadata'] = {}
                        cell['outputs'] = []
                        cell['source'] = [d.get_text()]
                        cell['execution_count'] = None
                        cell['cell_type'] = 'code'
                        dictionary['cells'].append(cell)
    
                    else:
                        cell = {}
                        cell['metadata'] = {}
    
                        cell['source'] = [d.decode_contents()]
                        cell['cell_type'] = 'markdown'
                        dictionary['cells'].append(cell)
    with open(output_path, 'w') as f:
        f.write(json.dumps(dictionary))
