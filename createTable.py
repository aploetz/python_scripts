ColName={"qty_dot_url": "int",
"qty_hyphen_url": "int",
"qty_underline_url": "int",
"qty_slash_url": "int"}

columns =  ColName.keys()
values = ColName.values()

createTableCQL = "CREATE TABLE  master_table("

for key, value in ColName.items():
    createTableCQL += key + " " + value + ", "

createTableCQL += "PRIMARY KEY(qty_dot_url))"

print(createTableCQL)
