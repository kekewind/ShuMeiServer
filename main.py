"""
代码已脱敏
Vx:Code-Bin
"""
import uvicorn
from fastapi import FastAPI

from captcha.sm_route import sm_router

app = FastAPI(title="数美验证码", description="数美验证码服务API\n核心代码已经脱敏，防止滥用\n有需要请联系VX:Code-Bin")

app.include_router(sm_router)

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
