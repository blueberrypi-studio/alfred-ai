import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()

config_file.add_section("General Settings")
config_file.set("General Settings","bot_name", "Alfred")
config_file.set("General Settings","window_title", "Alfred Ai")
config_file.set("General Settings","window_width", "1500")
config_file.set("General Settings","window_height", "800")
config_file.set("General Settings","hold_top_layer", "True")


# ADD SECTION
config_file.add_section("GUI Colours")
# ADD SETTINGS TO SECTION
config_file.set("GUI Colours", "background_colour", "black")
config_file.set("GUI Colours", "foreground_colour", "white")
config_file.set("GUI Colours", "widget_colour", "white")

config_file.add_section("GUI Config")
config_file.set("GUI Config", "DEBUG", "True")




# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()