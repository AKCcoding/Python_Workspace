customer = {
    "name": "Alrae Kei",
    "age": 23,
    "age": 24,
    "is_verified": True
}
print(customer["age"])
print(customer.get("is_verified"))

#instead of key error will return none cause of get method
print(customer.get("birthdate"))

#updatable
customer["name"] = "Rae"
print(customer.get("name"))
#supply even not in brackets
customer['birthdate'] = 'Mar 12,1999'
print(customer['birthdate'])
#will cause error cause it must be case sensitive
print(customer["Name"])