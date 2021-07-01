## Vue-cookies

### 安装

```shell
$ cnpm i vue-cookies -S
```

### 引入vue-cookies

```javascript
//require 
var Vue = require('vue');
Vue.user(require('vue-cookies'));

//es
import VUe from 'vue';
import VueCookies from 'vue-cookies';
Vue.use(VueCookies)

```

### 过期时间和URL

```javascript
this.$cookies.config(expireTimes,path)
/*
expireTimes：默认为1d
path：默认为 ' / '。注意//哈希模式下：域名/projectName/#/aaa默认为'/projectName'。域名/projectName#/aaa默认为' / '。确认#前是否有' / '。
*/
```

### 设置cookie

```javascript
this.$cookies.set(key,value[,expireTime[,path[,domain[,secure]]]])
/*
key: cookie名
注意 $cookies key names Cannot be set to ['expires', 'max-age', 'path', 'domain', 'secure']
value: cookie值
vue-cookie会自动帮你把对象转为json if (value && value.constructor === Object ){value = JSON.stringify(value)}
expireTimes: cookie有效时间，默认时间为1d
可以为到期时间点(expire=) [Date]，也可以为有效时间段单位s(max-age=)[Number]，传入Infinity||-1被认该cookie永久有效，传入0 会被判断为false导致取默认值，传入非-1 的负数会立即删除该cookie。传入String类型但又不会被正则匹配的('0'、'abc'、'Session')则关闭浏览器的时候销毁cookie(Expire/Max-Age=Session)，效果类似Session。
path: cookie所在目录，默认 '/' 根目录
设置path: '/projectName'指定项目名下'/projectName'使用
domain: cookie所在的域，默认为请求地址
secure: Secure属性是说如果一个cookie被设置了Secure=true，那么这个cookie只能用https协议发送给服务器，用http协议不发送。
*/
```

### 获取cookie

```javascript
this.$cookies.get(key)       // return value
```

### 删除cookie

```javascript
this.$cookies.remove(key [, path [, domain]])   
// return  false or true , warning： next version return this； use isKey(key) return true/false,please
```

### 是否有key cookie

```javascript
this.$cookies.isKey(key) // return true or false
```

### 列出所有cookie

```javascript
this.$cookies.keys() // return ['key', 'key', ......]
```

### 源码

```javascript
/**
 * Vue Cookies v1.5.7
 * https://github.com/cmp-cc/vue-cookies
 *
 * Copyright 2016, cmp-cc
 * Released under the MIT license
 */

(function() {

    var defaultConfig = {
        expires : '1d',
        path : '; path=/'
    }

    var VueCookies = {
        // install of Vue
        install: function(Vue) {
            Vue.prototype.$cookies = this
            Vue.cookies = this
        },
        config : function(expireTimes,path) {
            if(expireTimes) {
                defaultConfig.expires = expireTimes;
            }
            if(path === '') {
                defaultConfig.path = '';
            }else {
                defaultConfig.path = '; path=' + path;
            }
        },
        get: function(key) {
            var value = decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(key).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null

            if(value && value.startsWith("{") && value.endsWith("}")) {
                try {
                    value = JSON.parse(value)
                }catch (e) {
                    return value;
                }
            }
            return value;
        },
        set: function(key, value, expireTimes, path, domain, secure) {
            if (!key) {
                throw new Error("cookie name is not find in first argument")
            }else if(/^(?:expires|max\-age|path|domain|secure)$/i.test(key)){
                throw new Error("cookie key name illegality ,Cannot be set to ['expires','max-age','path','domain','secure']\t","current key name: "+key);
            }
            // support json object
            if(value && value.constructor === Object ) {
                value = JSON.stringify(value);
            }
            var _expires = "; max-age=86400"; // temp value, default expire time for 1 day
            expireTimes = expireTimes || defaultConfig.expires;
            if (expireTimes) {
                switch (expireTimes.constructor) {
                    case Number:
                        if(expireTimes === Infinity || expireTimes === -1) _expires = "; expires=Fri, 31 Dec 9999 23:59:59 GMT";
                        else _expires = "; max-age=" + expireTimes;
                        break;
                    case String:
                        if (/^(?:\d{1,}(y|m|d|h|min|s))$/i.test(expireTimes)) {
                            // get capture number group
                            var _expireTime = expireTimes.replace(/^(\d{1,})(?:y|m|d|h|min|s)$/i, "$1");
                            // get capture type group , to lower case
                            switch (expireTimes.replace(/^(?:\d{1,})(y|m|d|h|min|s)$/i, "$1").toLowerCase()) {
                                // Frequency sorting
                                case 'm':  _expires = "; max-age=" + +_expireTime * 2592000; break; // 60 * 60 * 24 * 30
                                case 'd':  _expires = "; max-age=" + +_expireTime * 86400; break; // 60 * 60 * 24
                                case 'h': _expires = "; max-age=" + +_expireTime * 3600; break; // 60 * 60
                                case 'min':  _expires = "; max-age=" + +_expireTime * 60; break; // 60
                                case 's': _expires = "; max-age=" + _expireTime; break;
                                case 'y': _expires = "; max-age=" + +_expireTime * 31104000; break; // 60 * 60 * 24 * 30 * 12
                                default: new Error("unknown exception of 'set operation'");
                            }
                        } else {
                            _expires = "; expires=" + expireTimes;
                        }
                        break;
                    case Date:
                        _expires = "; expires=" + expireTimes.toUTCString();
                        break;
                }
            }
            document.cookie = encodeURIComponent(key) + "=" + encodeURIComponent(value) + _expires + (domain ? "; domain=" + domain : "") + (path ? "; path=" + path : defaultConfig.path) + (secure ? "; secure" : "");
            return this;
        },
        remove: function(key, path, domain) {
            if (!key || !this.isKey(key)) {
                return false;
            }
            document.cookie = encodeURIComponent(key) + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT" + (domain ? "; domain=" + domain : "") + (path ? "; path=" + path : defaultConfig.path);
            return this;
        },
        isKey: function(key) {
            return (new RegExp("(?:^|;\\s*)" + encodeURIComponent(key).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=")).test(document.cookie);
        },
        keys:  function() {
            if(!document.cookie) return [];
            var _keys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, "").split(/\s*(?:\=[^;]*)?;\s*/);
            for (var _index = 0; _index < _keys.length; _index++) {
                _keys[_index] = decodeURIComponent(_keys[_index]);
            }
            return _keys;
        }
    }

    if (typeof exports == "object") {
        module.exports = VueCookies;
    } else if (typeof define == "function" && define.amd) {
        define([], function() {
            return VueCookies;
        })
    } else if (window.Vue) {
        Vue.use(VueCookies);
    }
    // vue-cookies can exist independently,no dependencies library
    if(typeof window!=="undefined"){
        window.$cookies = VueCookies;
    }

})()


```

参考链接：https://www.jianshu.com/p/8deae75624eb
来源：简书