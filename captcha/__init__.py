from os import path

import execjs

with open(path.join(path.dirname(__file__), "js\\ShuMei.js"), "r", encoding="utf-8") as f:
    js_content = f.read()
sm_js = execjs.compile(js_content)
ttf = path.join(path.dirname(__file__), "ttf\\chinese.ttf")