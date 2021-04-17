from osw.hal import OswHal

class OswLuaApp:
    SLEEP_TIME = 1 / 30.0

    def __init__(self, script: str, lua):
        self.script = script
        self.lua = lua

    def setup(self, hal: OswHal):
        injectHal = self.lua.eval("function(py_hal) _G.hal = py_hal end")
        injectHal(hal)

        self.lua.execute(self.script)
        
        self.lua.globals().setup()

    def loop(self):
        self.lua.globals().loop()
        

    def stop(self):
        self.lua.globals().stop()