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
assert jc1.check() == True

jc2 = JsonCensor(standard, keynumber_suspect)
assert jc2.check() == {"JSONcensor_msg":"Key number is not equal."}

jc3 = JsonCensor(standard, keyname_suspect)
assert jc3.check() == {"JSONcensor_msg": "Key name is not the same."}

jc4 = JsonCensor(standard, valtype_suspect)
assert jc4.check() == {"JSONcensor_msg":"Value type not equal"}