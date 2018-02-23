from checker import JsonChecker

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

suspect1 = {
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

jc = JsonChecker(standard, suspect1)
print(jc.check())