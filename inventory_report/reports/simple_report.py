class SimpleReport:

    def oldest_manufacturing_date(list):
        return min(product["data_de_fabricacao"] for product in list)

    def nearest_expiration_date(list):
        return min(product["data_de_validade"] for product in list)

    def get_unique_company_name(list):
        companies_list = []
        for product in list:
            if product["nome_da_empresa"] not in companies_list:
                companies_list.append(product["nome_da_empresa"])
        return companies_list

    def company_with_more_products(list, companies_list):
        companies_dict = {}
        for company in companies_list:
            companies_dict[company] = 0
        for product in list:
            for company in companies_list:
                if company == product["nome_da_empresa"]:
                    companies_dict[company] = companies_dict[company] + 1
        # https://www.delftstack.com/pt/howto/python/find-max-value-in-dictionary-python/
        return max(companies_dict, key=companies_dict.get)

    @classmethod
    def generate(self, list):

        companies_list = self.get_unique_company_name(list)

        return (
            "Data de fabricação mais antiga: "
            f"{self.oldest_manufacturing_date(list)}\n"
            "Data de validade mais próxima: "
            f"{self.nearest_expiration_date(list)}\n"
            "Empresa com mais produtos: "
            f"{self.company_with_more_products(list, companies_list)}"
        )
