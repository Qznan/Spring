
#-*-coding=utf-8-*-
#运用with类，要引入内置函数enter,exit
class echo:
    def output(self):
        print "1a"
    def __enter__(self):
        print "enter"
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print "exit"
        if exc_type==ValueError:
            return True
        else:
            return False
with echo() as e:
    e.output()
    print "do"
print '-----------'
with echo() as e:
    raise ValueError('value error')
print '-----------'
with echo() as e:
    raise Exception('can not detect')