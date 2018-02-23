# jsoncensor
Check json data in your python web service.
<br>

# 作用
1,检查key数目是否一致 <br>
2,检查key是否一致 <br>
3,检查value的type是否一致, 若value为一个对象，则递归地检查它的key number，Key name, value type. <br>

#Usage
创建一个标准json数据的字典，把它和待检查字典作为初始化JsonCensor对象的参数传入 <br>
调用JsonCensor对象的check方法，若检查通过返回True, 否则返回字符串msg. <br>

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
True
False
KeyNumberError:['k3', 'k4', 'k5']Should Be:['k1', 'k2', 'k3', 'k4', 'k5']
False
KeyNameError:['fuckccnu']Should Be:['k5_1_1_1']
False
TypeError:['test']|Should Be:str
```

关于flask或aiohttp的例子请见example
