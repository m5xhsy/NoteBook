# Vue-router

vue+vue-router+vuex

vue+vue-router主要来做SPA（Single Page Application）单页面应用，vue的核心插件

为什么做单页面应用呢？

传统的路由跳转，如果后端页面资源过多，会导致页面出现”白屏现象“，让前端来做路由，在某个生命周期的钩子函数中发生ajax，数据驱动

## 下载

```shell
$ cnpm i vue-router -S	
```

## 基础使用

HTML

```html
<div>
    <!-- 使用 router-link 组件来导航. -->
    <!-- 通过传入 `to` 属性指定链接. -->
    <router-link :to="{naem:'Home'}"></router-link>  <!-- to='/home' -->
    <!-- 路由出口 -->
  	<!-- 路由匹配到的组件将渲染在这里 -->
    <router-view></router-view>
<div>
    <script src="./vue-router.js"></script>
    
```

Js

```javascript
// 0. 如果使用模块化机制编程，导入Vue和VueRouter，要调用 Vue.use(VueRouter)

// 1. 定义 (路由) 组件。
// 可以从其他文件 import 进来
const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }

// 2. 定义路由
// 每个路由应该映射一个组件。 其中"component" 可以是
// 通过 Vue.extend() 创建的组件构造器，
// 或者，只是一个组件配置对象。
// 我们晚点再讨论嵌套路由。
const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar }
]

// 3. 创建 router 实例，然后传 `routes` 配置
// 你还可以传别的配置参数, 不过先这么简单着吧。
const router = new VueRouter({
  routes // (缩写) 相当于 routes: routes
})

// 4. 创建和挂载根实例。
// 记得要通过 router 配置参数注入路由，
// 从而让整个应用都有路由功能
const app = new Vue({
  router
}).$mount('#app')

// 现在，应用已经启动了！

```

### 动态路由匹配

```javascript
const router=new VueRouter({
    routes:[
        {
            path:'/user/:id',
            name:'User',
            component:User
        }
    ]
})
```

```html
<router-link :to='{name:'User',params:{id:xxx}>user{{ $route.params.id }}</router-link>
```



#### $route和$router 

$route 路由信息对象

```javascript
watch:{
    '$route'(to,from){
        console.log(to);
        console.log(from);
    }
}
```

$router 路由对象    VueRouter       





### 编程式导航

### 