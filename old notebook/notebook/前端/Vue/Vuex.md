## 安装

```shell
$ cnpm i vuex -S
```

## 例子

```javascript
<body>
    <div id="app"></div>
    <script src="../../node_modules/vue/dist/vue.js"></script>
    <script src="../../node_modules/vuex/dist/vuex.js"></script>
    <script>
        Vue.use(Vuex);
        const store = new Vuex.Store({
            state:{
                num:0
            },
            mutations:{
                mutationsAdd1(store,val){		//处理数据交互
                    store.num+=1;
                }
            },
            actions:{
                actionsAdd1(context,val){		//处理异步操作
                    setTimeout(function(){
                        context.commit('mutationsAdd1',val)
                    },1000)
                }
            }
        });
        const Ass = {
            data(){
                return {}
            },
            computed:{
                num:function(){
                    return this.$store.state.num;		//在computed中监听num
                }
            },
            //使用监听的num
            template:`
                <div>
                    {{ num }} 
                    <button @click="clickAdd1" >点击+1</button>
                </div>
            `,
            methods:{
                clickAdd1(){
                    this.$store.dispatch('actionsAdd1',1)
                }
            }
        }
        new Vue({
            el:'#app',
            store,	//挂载在vue
            template:`
                <div>
                    <Ass />
                </div>
            `,
            components:{
                Ass
            }
        })

    </script>
</body>

```

