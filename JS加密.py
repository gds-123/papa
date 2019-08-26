import async
import execjs

#第一种 escape()和unescape()
m ="%61%6C%65%72%74%28%22%u9ED1%u5BA2%u9632%u7EBF%22%29%3B"
#第二种 八进制 和十六进制
# m ="\141\154\145\162\164\50\42\u9ED1\u5BA2\u9632\u7EBF\42\51\73"

fun=execjs.compile(
    """
    function a(x){
       var s =unescape(x)
       return s
    }
    """
)
print(fun.call("a", m))


