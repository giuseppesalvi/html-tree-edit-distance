from zss import simple_distance, Node
from bs4 import BeautifulSoup
import re

def create_tree(html):
    soup = BeautifulSoup(html, 'html.parser')
    root = Node(soup.name if soup.name else 'root')
    create_tree_recursive(soup, root)
    return root

def create_tree_recursive(bs4node, zssnode):
    for child in bs4node.children:
        if child.name:  # this will ignore text nodes
            newnode = Node(child.name)
            zssnode.addkid(newnode)
            create_tree_recursive(child, newnode)

def calculate_ted(html1, html2):
    tree1 = create_tree(html1)
    tree2 = create_tree(html2)
    return simple_distance(tree1, tree2)

def extract_html_tree(html):
    match = re.search(r'(<html>.*?</html>)', html, re.DOTALL)
    if match:
        return match.group()
    else:
        return None

if __name__ == '__main__':
    file_name_1 = 'examples/rw_0.html'
    file_name_2 = 'examples/rw_0_modified.html'

    with open(file_name_1, 'r') as f1:
        html_1 = extract_html_tree(f1.read())

    with open(file_name_2, 'r') as f2:
        html_2 = extract_html_tree(f2.read())

    ted = calculate_ted(html_1, html_2)
    print(f"Html Tree Edit Distance: {ted:.2f}")
