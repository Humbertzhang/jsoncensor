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
    result = jc.check()
    if result['statu'] is not True:
        return json_response({"JSON_msg":result})
    # End Check

    # Your Code Here

    return json_response({"msg":"ok"})

app.router.add_route('POST', '/test/', test, name = "test")

web.run_app(app, host = "localhost", port = 5000)
