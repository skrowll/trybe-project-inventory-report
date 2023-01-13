from inventory_report.importer.importer import Importer

import csv

class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if "csv" in path:
            with open(path, encoding="utf-8") as csv_file:
                data = list(csv.DictReader(csv_file, delimiter=',', quotechar='"'))
            return data
        else:
            raise ValueError("Arquivo inválido")
