def compose(*functions):
    def func(a):
        result=None
        for i in range(-1,-(len(functions)+1),-1):
            if(i==-1):
                result=functions[i](a)
                continue
            result=functions[i](result)
        return result
    return func