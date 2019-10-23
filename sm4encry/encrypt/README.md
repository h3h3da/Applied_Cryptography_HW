# SM4图片加密

### 1921210442 刘存展

## 思路

将图片转化为rgb格式，并且对分别对rgb格式的数据使用gmssl进行加密，将带到的rgb文件使用magick工具转换为png格式的图片即可。这里可能要装一下ImageMagick工具。

## 效果

校徽原图:

![校徽原图](./pku_logo.png)

使用SM4/ECB加密后:

![使用SM4/ECB加密后](./sm4ecb.png)

使用SM4/CBC加密后：

![使用SM4/CBC加密后](./sm4cbc.png)