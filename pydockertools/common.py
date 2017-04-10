def exception_handlers(**kwargs):
    types = kwargs.get('errorTypes', None)
    msg = kwargs.get('msg', None)
    
    try:
        raise types(msg)
        return
    except TypeError:
        print 'Error: ' + msg
    except:
        print 'Unknown Error'