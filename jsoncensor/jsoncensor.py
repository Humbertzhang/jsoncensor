from queue import Queue

QUEUE_MAXSIZE = 1024

__all__ = ['JsonCensor', 'ArgNotDictException']

'''
The struct will be return
{
    "statu":True or False,
    "error":"",
    "error_item":"",
    "should_be":""
}
'''

class JsonCensor(object):
    
    #if you want a infinite queuesize, set queuesize with 0
    def __init__(self, standard, suspect, queuesize = QUEUE_MAXSIZE):
        self.checkqueue = Queue(queuesize)
        self.standard = standard
        self.suspect = suspect
        self.ret = {
                    "statu":None,
                    "error":None,
                    "error_item":None,
                    "should_be":None
                }

    def check(self):
        if type(self.standard) is not dict or type(self.suspect) is not dict:
            raise ArgNotDictException

        #初始化队列，将被检查对象加入队列中
        self.checkqueue.put((self.standard, self.suspect))

        while not self.checkqueue.empty():
            _standard, _suspect =  self.checkqueue.get()

            #type不一致
            if type(_standard) != type(_suspect):
                self._set_ret(False, "TypeError", str(_suspect), str(type(_standard).__name__))
                return self.ret

            #字典情况
            if type(_standard) == type(_suspect) and type(_standard) is dict:
                #1,Key 数目检查
                if len(_standard.keys()) != len(_suspect.keys()):
                    self._set_ret(False, "KeyNumberError", str(', '.join(_suspect.keys())), str(', '.join(_standard.keys())))
                    return self.ret
                
                #2, Key 名字检查,需要一致
                _standard_keys = _standard.keys()
                _suspect_keys = _suspect.keys()
                if _standard_keys != _suspect_keys:
                    error_keys = []
                    for key in _suspect_keys:
                        if key not in _standard_keys:
                            error_keys.append(key)
                    
                    self._set_ret(False, "KeyNameError", str(', '.join(error_keys)), str(', '.join(_standard.keys())))
                    return self.ret

                #3, 将Value加入到Queue中
                for key in _standard_keys:
                    self.checkqueue.put( (_standard[key], _suspect[key]) )
        
        #Set True return
        self._set_ret(True)
        return self.ret

    def _set_ret(self, statu, error = None, error_item = None, should_be = None):
        self.ret['statu'] = statu
        self.ret['error'] = error
        self.ret['error_item'] = error_item
        self.ret['should_be'] = should_be
        return self.ret


class ArgNotDictException(Exception):
    'Exception raised when args is illegal'
    pass
