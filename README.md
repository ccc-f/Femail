# Femail

一款可以批量验证邮箱有效性和批量枚举邮箱的工具，适用于寻找有效邮箱。

## 说明

本工具是在 [verifyemail](https://github.com/Tzeross/verifyemail) 的基础上添加了批量验证邮箱有效性和批量枚举邮箱的功能

感谢作者Tzeross https://github.com/Tzeross/verifyemail

## 使用方法

单个email验证：

```
python femail.py -c xxx@abc.com
```

批量验证邮箱有效性：

```
python femail.py -v -f emails.txt
```

批量枚举有效邮箱：

```
python femail.py -b -d 163.com -f burpemails.txt
```

## 注意事项

部分邮箱无法对其进行枚举和有效性验证，如 qq.com。

部分邮箱可能会将发件邮箱服务器 @chacuo.net 拉入黑名单，也可能将你的 IP 拉入黑名单，可以在 femail.py 修改 from_email 的值，更换为其他邮箱。

经尝试，无法使用多线程、多进程运行，因为验证原理是先与邮件服务器建立连接，再验证用户是否存在。

python 的 validate_email 模块功能不够强大，很多邮箱的有效性无法验证，所以没用那个。



## 写在最后

如有遗漏错误好的想法，请提到 issues，万分感谢。
