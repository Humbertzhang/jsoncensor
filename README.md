# jsoncensor
Check json data in your python web service.
<br>

# 作用
1,检查key数目是否一致 <br>
2,检查key是否一致 <br>
3,检查value的type是否一致, 若value为一个对象，则递归地检查它的key number，Key name, value type. <br>

# Usage
Support both python2.7 and python3 <br>
`pip install jsoncensor`
创建一个标准json数据的字典，把它和待检查字典作为初始化JsonCensor对象的参数传入 <br>
调用JsonCensor对象的check方法. <br>

```Python
from jsoncensor import JsonCensor

standard = {...}
suspect = {...}

jc = JsonCensor(standard, suspect)
ret = jc.check()
if ret['statu'] == True:
    print("ok")
else:
    print(ret)

```

返回结构体:

```
{
    "statu": True Or False,
    "error": string 若有错误为错误类型，否则为None,
    "error_indicator": string 错误对象的字符串,
    "should_be": string 错误对象应有的状态
}
```

# 示例

`plain_example`

```Python
from jsoncensor import JsonCensor

standard = {
    "k1":"v1",
    "k2":"v2",
    "k3":["v3_1", "v3_2", "v3_3"],
    "k4":{
        "k4_1":"v4_1",
        "k4_2":"v4_2",
        "k4_3":["v4_3_1", "v_4_3_2"],
        "k4_4":{
            "k_4_4_1":"v_4_4_1"
        }
    },
    "k5":{
        "k5_1":{
            "k5_1_1":{
                "k5_1_1_1":{
                    "k5_1_1_1":"pass"
                }
            }
        }
    }
}

perfect_suspect = {
    "k1":"test",
    "k2":"test",
    "k3":["v3_1", "v3_2", "v3_3"],
    "k4":{
        "k4_1":"v4_1",
        "k4_2":"v4_2",
        "k4_3":["v4_3_1", "v_4_3_2", "Helloooo"],
        "k4_4":{
            "k_4_4_1":"v_4_4_1"
        }
    },
    "k5":{
        "k5_1":{
            "k5_1_1":{
                "k5_1_1_1":{
                    "k5_1_1_1":"test"
                }
            }
        }
    }
}

keynumber_suspect = {
    "k3":["v3_1", "v3_2", "v3_3"],
    "k4":{
        "k4_1":"v4_1",
        "k4_2":"v4_2",
        "k4_3":["v4_3_1", "v_4_3_2", "Helloooo"],
        "k4_4":{
            "k_4_4_1":"v_4_4_1"
        }
    },
    "k5":{
        "k5_1":{
            "k5_1_1":{
                "k5_1_1_1":{
                    "k5_1_1_1":"test"
                }
            }
        }
    }
}

keyname_suspect = {
    "k1":"test",
    "k2":"test",
    "k3":["v3_1", "v3_2", "v3_3"],
    "k4":{
        "k4_1":"v4_1",
        "k4_2":"v4_2",
        "k4_3":["v4_3_1", "v_4_3_2", "Helloooo"],
        "k4_4":{
            "k_4_4_1":"v_4_4_1"
        }
    },
    "k5":{
        "k5_1":{
            "k5_1_1":{
                "fuckccnu":{        #<-Here
                    "k5_1_1_1":"test"
                }
            }
        }
    }
}

valtype_suspect = {
    "k1":["test"],      #<- Difference Here
    "k2":"test",
    "k3":["v3_1", "v3_2", "v3_3"],
    "k4":{
        "k4_1":"v4_1",
        "k4_2":"v4_2",
        "k4_3":["v4_3_1", "v_4_3_2", "Helloooo"],
        "k4_4":{
            "k_4_4_1":"v_4_4_1"
        }
    },
    "k5":{
        "k5_1":{
            "k5_1_1":{
                "k5_1_1_1":{
                    "k5_1_1_1":"test"
                }
            }
        }
    }
}

jc1 = JsonCensor(standard, perfect_suspect)
print(jc1.check() == True)
print(jc1.check())

jc2 = JsonCensor(standard, keynumber_suspect)
print(jc2.check() == True)
print(jc2.check())

jc3 = JsonCensor(standard, keyname_suspect)
print(jc3.check() == True)
print(jc3.check())

jc4 = JsonCensor(standard, valtype_suspect)
print(jc4.check() == True)
print(jc4.check())
```
python3 plain_example.py 结果输出

```
True
{'statu': True, 'error': None, 'error_indicator': None, 'should_be': None}
False
{'statu': False, 'error': 'KeyNumberError', 'error_indicator': 'k3, k4, k5', 'should_be': 'k1, k2, k3, k4, k5'}
False
{'statu': False, 'error': 'KeyNameError', 'error_indicator': 'fuckccnu', 'should_be': 'k5_1_1_1'}
False
{'statu': False, 'error': 'TypeError', 'error_indicator': "['test']", 'should_be': 'str'}
```

关于flask或aiohttp的例子请见example
