from pprint import pprint
import xml.etree.ElementTree as ET

def parse_xml(node, tabs):
    print(tabs, node.tag, ": ", node.text)
    tabs = tabs + "\t"
    for child in node:
        parse_xml(child,tabs)
    tabs = tabs[:-1]

tree = ET.parse('data.xml')
root = tree.getroot()
parse_xml(root,"")