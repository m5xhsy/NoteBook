    - let
        1.局部作用域
            2.不会存在变量提示
            3.变量不能重复声明
    - const
        特点:
            1.局部作用域
            2.不会存在变量提示
            3.变量不能重复声明
            4.只声明常量

    - 模板字符串
        let name = 'm5xhsy'
        let str = `我是${ name }`

    - 箭头函数
        let add = (x)=>{        //对象中用箭头函数this指向定义函数的父级对象(上下文)
            return x
        }
        let add = x => x;
    - 对象单体模式
        let person = {
            name:'xxx',
            func(){                 //相当于func:function(){console.log('xxx')}
                console.log('xxx')
            }
        }
    - 类
        class Ass{
            constructor(name) {
                this.name = name;
            }
            showname(){
                console.log(this.name)
            }
        }
        let A = new Ass();
        A.showname()



    - 类的继承
        class Bss extends Ass{
            constructor(name, age) {
                super(name); // 调用父类的constructor(name)
                this.age = age;
            }
            toString() {
                return super.showname() + ' ' + this.age ; // 调用父类的toString()
            }
        }