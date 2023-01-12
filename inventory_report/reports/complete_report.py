from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def get_unique_company_name(products):
        companies_list = []
        for product in products:
            if product["nome_da_empresa"] not in companies_list:
                companies_list.append(product["nome_da_empresa"])
        return companies_list

    def get_stocked_by_company(products, companies_list):
        companies_dict = {}
        for company in companies_list:
            companies_dict[company] = 0
        for product in products:
            for company in companies_list:
                if company == product["nome_da_empresa"]:
                    companies_dict[company] = companies_dict[company] + 1
        return companies_dict

    def result_str(companies):
        result = ""
        # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        sort_dict = sorted(companies.items(), key=lambda x: x[1], reverse=True)
        converted_dict = dict(sort_dict)
        for company in converted_dict:
            result = result + f"- {company}: {converted_dict[company]}\n"
        return result

    @classmethod
    def generate(self, products):
        simple_report = super().generate(products)
        companies_list = self.get_unique_company_name(products)
        companies_dict = self.get_stocked_by_company(products, companies_list)

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{self.result_str(companies_dict)}"
        )
