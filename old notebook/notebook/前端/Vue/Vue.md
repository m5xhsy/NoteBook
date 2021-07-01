# DOM操作

获取原生DOM方式

```javascript
//给标签添加ref
<div ref='a' ></div>
<Home ref='b'></Home>

this.$refs.a	//获取的原始DOM对象
this.$refs.b	//获取组件的实例化对象
```

# 指令系统

## v-text

## v-html

## v-show

## v-if

## v-bind

## v-on

## v-for

## v-model

# 常用属性

## data:function(){}

## el:'#app"

## methods

## watch

## computed

## template

# 组件

## （一）局部组件

- 声明局部组件

```javascript
let Ass = {
    data(){
        return {
            msg:'这是局部组件'
        }
    }
}
```

- 挂载局部组件

```java
new Vue({
   ...
   	components:{
   		Ass
   	}
        
})
```

- 使用局部组件

```javascript
new Vue({
   ...
   	template:`
		<div>
			<Ass />
		</div>
	`  
})
```



## （二）全局组件

- ### 声明全局组件

```javascript
Vue.conponent('Ass',{
    data(){
        return {
            msg:'这是全局组件'
        }
    }
})
```

​	全局组件使用和局部组件一致

## （三）组件传值

### （ 1 ）子组件传父组件

```javascript
Vue.component('Ass',{
    data(){
        return {
            title:'m5xhsy'
        }
    },
    template:`
        <div>
        	<button @click='cilckHandler'>子组件传值</button>
        </div>
    `,
    methods:{
        cilckHandler(){
            return this.$emit('values',this.title)		//emit函数传值
        }
    }
})
new Vue({
    el:'#app',
    //事件
    template:`
        <div>
        	<Ass @values='values' />
        </div>
	`,
    methods:{
        values(val){
            alert(val)
        }
    }

})
```



### （ 2 ）父组件传子组件

```javascript
Vue.component('Ass',{
    props:['msg'],		//子组件接收值
    template:`
        <div>
        <h2>msg:{{ msg }}</h2>	
        </div>
    `
})
new Vue({
    el:'#app',
    data(){
        return {
            title:'m5xhsy'
        }
    },
    //父组件传值
    template:`
        <div>
        <Ass :msg=title></Ass>
        </div>
    `
})
```



### （ 3 ）平行组件传值

- 创建bus公交车对象

  ```javascript
  const bus = new Vue();
  //Vue.prototype.$bus = bus;			//模块化则要挂载到vue.prototype上
  Vue.component('Ass',{
      data(){
          return {
              title:'m5xhsy'
          }
      },
      template:`
          <div>
          	<button @click='cilckHandler'>组件传值</button>
          </div>
      `,
      methods:{
          cilckHandler(){
              bus.$emit('values',this.title)
          }
      }
  })
  new Vue({
      el:'#app',
      template:`
          <div>
              <Ass />
          </div>
  	`,
      created(){
          bus.$on('values',(val)=>{
              alert(val)
          })
      }
  })
  
  ```



# 过滤器

过滤器使用

```html
<div>{{ val|Myfilter(a,b) }}</div>
```



## （一）局部过滤器

​	只在当前组件内部创建和使用

```javascript
filters:{
    Myfilter:function(val, a, b){
    	//处理
    	return xxx
	}
}
```



## （二）全局过滤器

```javascript
Vue.filter('Myfilter',function(val, a, b){
    //处理
    return xxx
})
```



# 生命周期钩子

![lifecycle](A:\lifecycle.png)

## [beforeCreate](https://cn.vuejs.org/v2/api/#beforeCreate)

```javascript
beforeCreate(){
    console.log(this.msg)   
    //组件创建之前 undefined
}
```

## [created](https://cn.vuejs.org/v2/api/#created)

```javascript
created(){
    console.log(this.msg)   
    //组件创建之后 msg
    //使用该组件就会触发以上的钩子函数
    //created中可以操作数据，比如ajax（XMLHttpRequest 简称XHR）、axios、fetchq请求，并且可以实现数据的驱动视图
}
```



## [beforeMount](https://cn.vuejs.org/v2/api/#beforeMount)

```javascript
beforeMount(){
    //装载数据到DOM之前会调用
    console.log(document.getElementById('app'))     //Test组件未被渲染
}
```

## [mounted](https://cn.vuejs.org/v2/api/#mounted)

```javascript
mounted(){
    //这个地方可以操作DOM
    //装载数据到DOM之后会被调用，可以获取真实的DOM元素，Vue操作以后的DOM
    console.log(document.getElementById('app'))     
}
```

## [beforeUpdate](https://cn.vuejs.org/v2/api/#beforeUpdate)

```javascript
beforeUpdate(){
    //更新数据之前调用此钩子，获取原始DOM
    console.log(document.getElementById('app').innerHTML)
}
```

## [updated](https://cn.vuejs.org/v2/api/#updated)

```javascript
updated(){
    //更新数据之后，调用此钩子，获取最新DOM
    console.log(document.getElementById('app').innerHTML)
}
```

## [activated](https://cn.vuejs.org/v2/api/#activated)

```javascript
activated(){
    console.log('组件被激活了')		//应用与缓存
}
```

## [deactivate](https://cn.vuejs.org/v2/api/#deactivated)

```javascript
deactivated(){
    console.log('组件被停用了')
}
//与<keep-alive />一起用
```

## [beforeDestroy](https://cn.vuejs.org/v2/api/#beforeDestroy)

```javascript
beforeDestroy(){
    console.log('beforeDestroy')    //组件销毁之前
}
```

## [destroyed](https://cn.vuejs.org/v2/api/#destroyed)

```javascript
destroyed(){
    console.log('destroyed')        //组件销毁之后，可以用于销毁定时器
}
```

## [errorCaptured](https://cn.vuejs.org/v2/api/#errorCaptured)

