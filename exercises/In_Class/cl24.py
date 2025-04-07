ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# add three orders of mint ice cream
# mint should be the key
# ice_cream["mint"] = 3

# printing orders of chocolate:
print(ice_cream["chocolate"])

# update the number of orders of vanilla to be 10 (reassign the value to be 10)
ice_cream["vanilla"] = (
    10  # if vanilla exists in the dictionary as a key, then we update this value to 10. If vanilla didn't already exist as a key,it added vanilla to the dictionary
)

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint found!")
