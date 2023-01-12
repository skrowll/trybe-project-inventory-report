from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv
import json


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

    @classmethod
    def import_data(self, path, report_type):
        if "csv" in path:
            return self.read_csv(path, report_type)
        elif "json" in path:
            return self.read_json(path, report_type)
