# IoT设备中的分组密码研究——以Chaskey、Simon和Speck为例

## 小组成员

刘存展 1901210442

胡兆杰 1901210403

高亨利 1901210713

## 简介

思科IBSG的最新白皮书估计，到2020年，将有500亿个设备连接到互联网，这意味着在不远的将来，每个人都将被数十种传感器设备所包围，从互联网到物联网的这种演进将对我们的日常生活产生巨大影响，并改变我们与周围的物理世界的交互方式。然而，显而易见的是，连接到Internet的500亿智能设备给其所有者或用户的安全和隐私带来了前所未有的挑战。众所周知，对称密码系统在物联网的安全领域中扮演着重要角色，但是物联网硬件设备的计算和存储资源十分有限，这就需要对密码体系进行更加细致有效的设计，保证在物联网设备中有限的资源上能够稳定运行。在[本篇报告](./IoT设备中的分组密码研究——以Chaskey、Simon和Speck为例.pdf)中，我们选取了3种在IoT设备中性能表现优异并且安全性较高的密码方案，即Chaskey、Simon和Speck，来进行简单的分析和介绍。

## Reference

1. Beaulieu R, Treatman-Clark S, Shors D, et al. The SIMON and SPECK lightweight block ciphers[C]//2015 52nd ACM/EDAC/IEEE Design Automation Conference (DAC). IEEE, 2015: 1-6.

2. Beaulieu R, Shors D, Smith J, et al. SIMON and SPECK: Block Ciphers for the Internet of Things[J]. IACR Cryptology ePrint Archive, 2015, 2015: 585.

3. Daniel D , Le C Y , Dmitry K , et al. Triathlon of lightweight block ciphers for the Internet of things[J]. Journal of Cryptographic Engineering, 2018.

4. D. Evans. The Internet of Things: How the Next Evolution of the Internet is Changing Everything. Cisco IBSG white paper, available for download at http://www.cisco.com/web/about/ac79/docs/innov/IoT_IBSG_0411FINAL.pdf, Apr. 2011.

5.  N. Mouha, B. Mennink, A. Van Herrewege, D. Watanabe, B. Preneel, I. Verbauwhede, "Chaskey: an efficient mac algorithm for 32-bit microcontrollers", International Workshop on Selected Areas in Cryptography, pp. 306-323, 2014

6. Dworkin, M.: Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication. NIST special publication 800-38b, National Institute of Standards and Technology (NIST) (May 2005), http://csrc.nist.gov/publications/nistpubs/800-38B/SP_800-38B.pdf

7. Bellare, M., Canetti, R., Krawczyk, H.: Keying Hash Functions for Message Authentication. In: Koblitz [47], pp. 1–15
