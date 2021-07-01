常用命令

### sudo

### ifconfig

### sudo service apache2 start

### sudo passwd root

### sudo apt-get update

### sudo apt-get upgrade

### sudo apt-get install xxx

### sudo apt-get uninstall xxx

## arping

ARP协议是“Address Resolution Protocol”(地址解析协议)的缩写。在同一以太网中，通过地址解析协议，源主机可用通过目的主机的IP地址获得目的主机的MAC地址

arping,用来向局域网内的其他主机发送ARP请求指令，它可用来测试局域网内的某一个IP是否被使用。

### 使用示例

- 查看某个IP的MAC地址

  ```shell
  $ sudo arping 192.168.239.128
  ```

- 查看某个IP地址的MAC地址，并指定count数量

  ```shell
  $ sudo arping -c 6 192.168.239.128
  ```

- 设定一个扫描时间，单位是秒

  ```shell
  $ sudo arping -w 5 192.168.239.128
  ```

## hping3

hping是面向命令行的用于生成和解析TCP/IP协议数据包汇编/分析的开源工具。

目前最新版本的是hping3，它支持TCP、UDP、ICMP和RAW-IP协议，具有跟踪路由模式，能够覆盖信道之前发送文件以及其他许多功能。

hping3是安全审计、防火墙测试等工作的标配工具，hping优势在于能够定制数据包的各个部分，因此用户可用灵活对目标及进行细致的探测。

### 使用示例

- 查看帮助

  ```shell
  $ sudo hping3 --help
  ```

- 端口扫描

  ```shell
  $ hping3 -I eth0 -S 192.168.239.128 -p 80
  ```

- 防火墙测试

  ```shell
  $ hping3 -S -c 1000000 -a 10.10.10.10 -p 21 10.10.10.10
  ```

  

- 拒绝服务器攻击

### 参数说明

```shell

用法: hping3 host [options]
  -h  --help      显示帮助
  -v  --version   显示版本
  -c  --count     发送数据包的数目
  -i  --interval  发送数据包间隔的时间 (uX即X微秒, 例如： -i u1000)
      --fast      等同 -i u10000 (每秒10个包)
      --faster    等同 -i u1000 (每秒100个包)
      --flood	  尽最快发送数据包，不显示回复。
  -n  --numeric   数字化输出，象征性输出主机地址。
  -q  --quiet     安静模式
  -I  --interface 网卡接口 (默认路由接口)
  -V  --verbose   详细模式
  -D  --debug     调试信息
  -z  --bind      绑定ctrl+z到ttl(默认为目的端口)
  -Z  --unbind    取消绑定ctrl+z键
      --beep      对于接收到的每个匹配数据包蜂鸣声提示

模式选择
  default mode     TCP   // 默认模式是 TCP
  -0  --rawip      RAWIP模式，原始IP模式。在此模式下HPING会发送带数据的IP头。即裸IP方式。使用RAWSOCKET方式。
  -1  --icmp       ICMP模式，此模式下HPING会发送IGMP应答报，你可以用--ICMPTYPE --ICMPCODE选项发送其他类型/模式的ICMP报文。
  -2  --udp        UDP 模式，缺省下，HPING会发送UDP报文到主机的0端口，你可以用--baseport --destport --keep选项指定其模式。
  -8  --scan       SCAN mode. //扫描模式 指定扫描对应的端口。
                   Example: hping --scan 1-30,70-90 -S www.target.host    // 扫描
  -9  --listen     listen mode  // 监听模式
  
IP 模式
  -a  --spoof      spoof source address  //源地址欺骗。伪造IP攻击，防火墙就不会记录你的真实IP了，当然回应的包你也接收不到了。
  --rand-dest      random destionation address mode. see the man. // 随机目的地址模式。详细使用 man 命令
  --rand-source    random source address mode. see the man.       // 随机源地址模式。详细使用 man 命令
  -t  --ttl        ttl (默认 64)  //修改 ttl 值
  -N  --id         id (默认 随机)  // hping 中的 ID 值，缺省为随机值
  -W  --winid      使用win* id字节顺序  //使用winid模式，针对不同的操作系统。UNIX ,WINDIWS的id回应不同的，这选项可以让你的ID回应和WINDOWS一样。
  -r  --rel        相对id字段(估计主机流量)  //更改ID的，可以让ID曾递减输出，详见HPING-HOWTO。
  -f  --frag       拆分数据包更多的frag.  (may pass weak acl)   //分段，可以测试对方或者交换机碎片处理能力，缺省16字节。
  -x  --morefrag   设置更多的分段标志    // 大量碎片，泪滴攻击。
  -y  --dontfrag   设置不分段标志    // 发送不可恢复的IP碎片，这可以让你了解更多的MTU PATH DISCOVERY。
  -g  --fragoff    set the fragment offset    // 设置断偏移。
  -m  --mtu        设置虚拟最大传输单元, implies --frag if packet size > mtu    // 设置虚拟MTU值，当大于mtu的时候分段。
  -o  --tos        type of service (default 0x00), try --tos help          // tos字段，缺省0x00，尽力而为？
  -G  --rroute     includes RECORD_ROUTE option and display the route buffer    // 记录IP路由，并显示路由缓冲。
  --lsrr           松散源路由并记录路由        // 松散源路由
  --ssrr           严格源路由并记录路由      // 严格源路由
  -H  --ipproto    设置IP协议字段，仅在RAW IP模式下使用   //在RAW IP模式里选择IP协议。设置ip协议域，仅在RAW ip模式使用。

ICMP 模式
  -C  --icmptype   icmp类型(默认echo请求)    // ICMP类型，缺省回显请求。
  -K  --icmpcode   icmp代号(默认0)     // ICMP代码。
      --force-icmp 发送所有icmp类型(默认仅发送支持的类型)    // 强制ICMP类型。
      --icmp-gw    设置ICMP重定向网关地址(默认0.0.0.0)    // ICMP重定向
      --icmp-ts    等同 --icmp --icmptype 13 (ICMP 时间戳)            // icmp时间戳
      --icmp-addr  等同 --icmp --icmptype 17 (ICMP 地址子网掩码)  // icmp子网地址
      --icmp-help  显示其他icmp选项帮助      // ICMP帮助

UDP/TCP 模式
  -s  --baseport   base source port             (default random)              // 缺省随机源端口
  -p  --destport   [+][+]<port> destination port(default 0) ctrl+z inc/dec    // 缺省随机源端口
  -k  --keep       keep still source port      // 保持源端口
  -w  --win        winsize (default 64)        // win的滑动窗口。windows发送字节(默认64)
  -O  --tcpoff     set fake tcp data offset     (instead of tcphdrlen / 4)    // 设置伪造tcp数据偏移量(取代tcp地址长度除4)
  -Q  --seqnum     shows only tcp sequence number        // 仅显示tcp序列号
  -b  --badcksum   (尝试)发送具有错误IP校验和数据包。许多系统将修复发送数据包的IP校验和。所以你会得到错误UDP/TCP校验和。
  -M  --setseq     设置TCP序列号 
  -L  --setack     设置TCP的ack   ------------------------------------- (不是 TCP 的 ACK 标志位)
  -F  --fin        set FIN flag
  -S  --syn        set SYN flag
  -R  --rst        set RST flag
  -P  --push       set PUSH flag
  -A  --ack        set ACK flag   ------------------------------------- （设置 TCP 的 ACK 标志 位）
  -U  --urg        set URG flag      // 一大堆IP抱头的设置。
  -X  --xmas       set X unused flag (0x40)
  -Y  --ymas       set Y unused flag (0x80)
  --tcpexitcode    使用last tcp-> th_flags作为退出码
  --tcp-mss        启用具有给定值的TCP MSS选项
  --tcp-timestamp  启用TCP时间戳选项来猜测HZ/uptime

Common //通用设置
  -d  --data       data size    (default is 0)    // 发送数据包大小，缺省是0。
  -E  --file       文件数据
  -e  --sign       添加“签名”
  -j  --dump       转储为十六进制数据包
  -J  --print      转储为可打印字符
  -B  --safe       启用“安全”协议
  -u  --end        告诉你什么时候--file达到EOF并防止倒回
  -T  --traceroute traceroute模式(等同使用 --bind 且--ttl 1)
  --tr-stop        在traceroute模式下收到第一个不是ICMP时退出
  --tr-keep-ttl    保持源TTL固定，仅用于监视一跳
  --tr-no-rtt	   不要在跟踪路由模式下计算/显示RTT信息 ARS包描述（新增功能，不稳定）
ARS packet description (new, unstable)
  --apd-send       发送APD描述数据包(参见docs / APD.txt) 
```

