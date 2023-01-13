from inventory_report.importer.importer import Importer

import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if "json" in path:
            with open(path, mode="r") as json_file:
                data = json.loads(json_file.read())
            return data
        else:
            raise ValueError("Arquivo inválido")
