#!/usr/bin/python

#
# Assumes plugins/<dirname>/__init__.py with a run() function
#
for i in pluginloader.getPlugins():
    print("Loading plugin " + i["name"])
    plugin = pluginloader.loadPlugin(i)
    plugin.run()
