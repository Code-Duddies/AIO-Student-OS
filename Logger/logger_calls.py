from logger_tools import LoggerTools as LT

class LoggerCalls(LT):
    
    def __init__(self):
        super().__init__()
        self.logger.info('LoggerCalls object created')
        
    def __del__(self):
        self.logger.info('LoggerCalls object deleted')
        
    def info_call(self, passedString):
        '''Logger information call'''
        self.logger.info(passedString)
            
    def error_call(self, passedString):
        '''Logger error call'''
        self.logger.error(passedString)
        
    def debug_call(self, passedString):
        '''Logger debug call'''
        self.logger.debug(passedString)
