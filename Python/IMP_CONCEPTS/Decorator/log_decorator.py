try:
    import os
    import datetime
    import sys
    import logging
except Exception as e:
    print("Some module is missing {}",format(e))

class Meta(type):
    """Meta Class"""

    def __call__(cls, *args, **kwargs):
        instance = super(Meta,cls).__call__(*args,**kwargs)
        return instance

    def __init__(cls,name,base,attr):
        super(Meta,cls).__init__(name,base,attr)



class log(object):

    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):

        """Wrapper Function"""

        start = datetime.datetime.now()    #start Time
        call_func = self.func(*args,**kwargs)    #call function
        name_func = self.func.__name__       #name of the function
        end = datetime.datetime.now()       #end time

        message = """"
        
            Function={}
            Execution Time = {}
            Address = {}
            Memeoy = {} Bytes
            Date = {}
            
        """.format(name_func,
                   end,
                   self.func.__name__,
                   sys.getsizeof(self.func),
                   start)

        cwd = os.getcwd()
        folder = 'Logs'
        newpath = os.path.join(cwd,folder)

        try:
            """ try to create a folder if folder not exists"""
            os.mkdir(newpath)

        except:
            """ Directory already exists"""
            logging.basicConfig(filename='{}/log.log'.format(newpath),level=logging.DEBUG)
            logging.DEBUG(message)

        return  call_func

class Test(metaclass=Meta):

    def __init__(self,*args,**kwargs):
        pass

    @log
    def methodA():
        print("method A")
        return "Neha"

if __name__ == "__main__":
    obj = Test()
    obj.methodA()



