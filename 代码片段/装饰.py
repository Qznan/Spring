#-*-coding=utf-8-*-
#实现一个装饰器
# def test(function):
#     def test2(arg):
#         print "hello"
#         function(arg)
#     return test2
# @test
# def echo(args):
#     print "world\n" + args
# echo('lin')
#装饰器包含参数
def hello(wo1):
    def hello2(function):
        def hello3(wo2):
            print wo1,"play"
            function(wo2)
        return hello3
    return hello2
@hello('lin')
def say (who):
    print who
say("linlin")