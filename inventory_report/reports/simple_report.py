class SimpleReport:

    def oldest_manufacturing_date(products):
        return min(product["data_de_fabricacao"] for product in products)

    def nearest_expiration_date(products):
        return min(product["data_de_validade"] for product in products)

    def get_unique_company_name(products):
        companies_list = []
        for product in products:
            if product["nome_da_empresa"] not in companies_list:
                companies_list.append(product["nome_da_empresa"])
        return companies_list

    def company_with_more_products(products, companies_list):
        companies_dict = {}
        for company in companies_list:
            companies_dict[company] = 0
        for product in products:
            for company in companies_list:
                if company == product["nome_da_empresa"]:
                    companies_dict[company] = companies_dict[company] + 1
        # https://www.delftstack.com/pt/howto/python/find-max-value-in-dictionary-python/
        return max(companies_dict, key=companies_dict.get)

    @classmethod
    def generate(self, products):

        companies_list = self.get_unique_company_name(products)

        return (
            "Data de fabricação mais antiga: "
            f"{self.oldest_manufacturing_date(products)}\n"
            "Data de validade mais próxima: "
            f"{self.nearest_expiration_date(products)}\n"
            "Empresa com mais produtos: "
            f"{self.company_with_more_products(products, companies_list)}"
        )
