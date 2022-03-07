
class ApptPlusException(Exception):
    cname = None
    ecode = None
    emsg = None

    def __init__(self, className, errCode, errMsg):
        self.cname = className
        self.ecode = errCode
        self.emsg = errMsg
