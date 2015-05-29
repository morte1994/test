print True and True
print False and False
print 1 == 1 and 2 == 1
print "test" == "test"
print 1 == 1 and 2 == 1
print True and 1 == 1
print 1 != 0 and 2 ==1
print "***********************"
print "test" == "testing"
print "test" == "test"
print "test" == 1
print not (True and False)
print not (1 == 1 and 0 !=1)
print not (10 == 1 or 1000 ==1000)
print not (1 != 10 or 3 ==4)
print not ("testing" == "testing" and "zed" == "cool")
print 1 ==1 and not ("testing" == 1 or 1 == 0)
print "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print 3 == 3 and not ("testing" == "testing" or "Python" == "fun") 
#存在逻辑短路问题，以  False  开头的  and  语句都会直接被处理成  False  并且不会继续检查后面语句了。任何包含  True  的  or  语句，只要处理到  True  这个字样，就不会继续向下推算
#!=  和  <>  有何不同？Python  中  <>  将被逐渐弃用，  !=  才是主流
