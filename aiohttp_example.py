from aiohttp import web
from aiohttp.web import json_response
import asyncio
from jsoncensor import JsonCensor

app = web.Application()

async def test(request):
    # Start Check
    standard = {
        "username":"",
        "password":"",
        "email":""
    }
    jc = JsonCensor(standard, await request.json())
    check_msg = jc.check()
    if check_msg is not True:
        return json_response(check_msg)
    # End Check

    # Your Code Here

    return json_response({"msg":"ok"})

app.router.add_route('POST', '/test/', test, name = "test")

web.run_app(app, host = "localhost", port = 5000)