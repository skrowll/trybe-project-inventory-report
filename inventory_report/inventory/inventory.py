from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv
import json
import xml.etree.ElementTree as ET


class Inventory:

    def read_csv(path, report_type):
        with open(path, encoding="utf-8") as csv_file:
            data = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            if report_type == "simples":
                return SimpleReport.generate(list(data))
            elif report_type == "completo":
                return CompleteReport.generate(list(data))

    def read_json(path, report_type):
        with open(path, mode="r") as json_file:
            data = json.loads(json_file.read())
            if report_type == "simples":
                return SimpleReport.generate(list(data))
            elif report_type == "completo":
                return CompleteReport.generate(list(data))

    def read_xml(path, report_type):
        tree = ET.parse(path)
        root = tree.getroot()
        products_list = []
        for element in root.findall("*"):
            product_dict = {}
            for child in element:
                product_dict[child.tag] = child.text
            products_list.append(product_dict)
        if report_type == "simples":
            return SimpleReport.generate(products_list)
        elif report_type == "completo":
            return CompleteReport.generate(products_list)

    @classmethod
    def import_data(self, path, report_type):
        if "csv" in path:
            return self.read_csv(path, report_type)
        elif "json" in path:
            return self.read_json(path, report_type)
        elif "xml" in path:
            return self.read_xml(path, report_type)
