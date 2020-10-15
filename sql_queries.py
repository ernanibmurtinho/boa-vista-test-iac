import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

bill_of_materials_drop ="DROP TABLE IF EXISTS fornecedores_tubos.bill_of_materials;"
comp_boss = "DROP TABLE IF EXISTS fornecedores_tubos.comp_boss;"
price_quote_drop = "DROP TABLE IF EXISTS fornecedores_tubos.price_quote;"


# CREATE TABLES

"""
bill_of_materials_create = CREATE TABLE fornecedores_tubos.bill_of_materials (
tube_assembly_id VARCHAR(30),
component_id_1 VARCHAR(30),
quantity_1 INTEGER,
component_id_2 VARCHAR(30),
quantity_2 INTEGER,
component_id_3 VARCHAR(30),
quantity_3 INTEGER,
component_id_4 VARCHAR(30),
quantity_4 INTEGER,
component_id_5 VARCHAR(30),
quantity_5 INTEGER,
component_id_6 VARCHAR(30),
quantity_6 INTEGER,
component_id_7 VARCHAR(30),
quantity_7 INTEGER,
component_id_8 VARCHAR(30),
quantity_8 INTEGER
);
"""

bill_of_materials_create = """ 
CREATE TABLE fornecedores_tubos.bill_of_materials (
tube_assembly_id VARCHAR(30),
component_id_1 VARCHAR(30),
quantity_1 VARCHAR(30),
component_id_2 VARCHAR(30),
quantity_2 VARCHAR(30),
component_id_3 VARCHAR(30),
quantity_3 VARCHAR(30),
component_id_4 VARCHAR(30),
quantity_4 VARCHAR(30),
component_id_5 VARCHAR(30),
quantity_5 VARCHAR(30),
component_id_6 VARCHAR(30),
quantity_6 VARCHAR(30),
component_id_7 VARCHAR(30),
quantity_7 VARCHAR(30),
component_id_8 VARCHAR(30),
quantity_8 VARCHAR(30)
);"""

comp_boss_create = """CREATE TABLE fornecedores_tubos.comp_boss (
component_id VARCHAR(30),
component_type_id VARCHAR(30),
type VARCHAR(30),
connection_type_id VARCHAR(30),
outside_shape VARCHAR(30),
base_type VARCHAR(30),
height_over_tube VARCHAR(30),
bolt_pattern_long VARCHAR(30),
bolt_pattern_wide VARCHAR(30),
groove VARCHAR(30),
base_diameter VARCHAR(30),
shoulder_diameter VARCHAR(30),
unique_feature VARCHAR(30),
orientation VARCHAR(30),
weight VARCHAR(30)
);"""


#query price_quote

price_quote_create = """CREATE TABLE fornecedores_tubos.price_quote (
tube_assembly_id VARCHAR(30),
supplier VARCHAR(30),
quote_date VARCHAR(15),
annual_usage VARCHAR(15),
min_order_quantity VARCHAR(30),
bracket_pricing VARCHAR(30),
quantity VARCHAR(30),
cost VARCHAR(30)
);"""


# QUERY LISTS

create_table_queries = [bill_of_materials_create, comp_boss_create, price_quote_create ]
drop_table_queries = [ bill_of_materials_drop, comp_boss, price_quote_drop ]
copy_table_queries = ["bill_of_materials", "comp_boss", "price_quote"]
