from inventory_report.importer.importer import Importer

import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if "xml" in path:
            tree = ET.parse(path)
            root = tree.getroot()
            products_list = []
            for element in root.findall("*"):
                product_dict = {}
                for child in element:
                    product_dict[child.tag] = child.text
                products_list.append(product_dict)
            return products_list
        else:
            raise ValueError("Arquivo inválido")