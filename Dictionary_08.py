print("\n" + "="*70)
print("PROGRAM 8: MERGING AND UPDATING DICTIONARIES")
print("="*70)

base_config = {"host": "localhost", "port": 5000, "debug": True}
user_config = {"port": 8000, "timeout": 30}
base_config.update(user_config)

print(base_config)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)

defaults = {"color": "blue", "size": "medium", "active": True}
overrides = {"color": "red", "size": "large"}
final = {**defaults, **overrides}
print(final)

employee = {"name": "Alice", "salary": 70000}
raise_amount = 5000
if employee["salary"] < 80000:
   employee["salary"] += raise_amount
   
print(employee)   

default_settings = {
    "theme": "light",
    "language": "en",
    "notifications": True,
    "auto_save": False,
    "timeout": 30
}
user_preferences = {
    "theme": "dark",
    "notifications": False,
    "font_size": 14
}

environment_overrides = {
    "timeout": 60,
    "debug": True
}
merged1 = {**default_settings, **user_preferences, **environment_overrides}
print(merged1)


if environment_overrides["debug"] is True:
   environment_overrides["timeout"] += 60
   
print(environment_overrides)
if user_preferences["theme"] is "dark":
   user_preferences["high_contrast"] = True
print(user_preferences)   
