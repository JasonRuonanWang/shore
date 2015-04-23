class event():

    __observers = []

    def _mainloop(self, msg):
        for observer in self.__observers:
            observer(msg)

    def reg_observer(self, func):
        self.__observers.append(func)



