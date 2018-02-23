# key name应一致，value若不为dict应一致，若未dict应递归
from queue import Queue

QUEUE_MAXSIZE = 1024

__all__ = ['JsonChecker', 'ArgException']

class JsonChecker(object):
    def __init__(self, standard, suspect, queuesize = QUEUE_MAXSIZE):
        self.checkqueue = Queue(queuesize)
        self.standard = standard
        self.suspect = suspect

    def check(self):
        if type(self.standard) is not dict or type(self.suspect) is not dict:
            raise ArgTypeException

        #初始化队列，将被检查对象加入队列中
        self.checkqueue.put((self.standard, self.suspect))

        while not self.checkqueue.empty():
            _standard, _suspect =  self.checkqueue.get()

            #非字典情况，需要type一致
            if type(_standard) != type(_suspect):
                return {"JSONChecker_msg":"Value type not equal"}

            #字典情况
            if type(_standard) == type(_suspect) and type(_standard) is dict:
                #1,Key 数目检查
                if len(_standard.keys()) != len(_suspect.keys()):
                    return {"JSONChecker_msg":"Key number is not equal."}
                
                #2, Key 名字检查,需要一致
                _standard_keys = _standard.keys()
                _suspect_keys = _suspect.keys()
                if _standard_keys != _suspect_keys:
                    return {"JSONchecker_msg": "Key name is not the same."}
                
                #3, 将Value加入到Queue中
                for key in _standard_keys:
                    self.checkqueue.put( (_standard[key], _suspect[key]) )
            
        return True

class ArgTypeException(Exception):
    'Exception raised when args is illegal'
    pass