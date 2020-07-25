monthConversion = { #key has to be unique,type can vary
    "Jan":"January",
    "Feb":"Febuary",
    "Mar":"March"

}
print(monthConversion["Jan"])
print(monthConversion.get("adsf","Key does not exits"))  #can set default value if key is not found

