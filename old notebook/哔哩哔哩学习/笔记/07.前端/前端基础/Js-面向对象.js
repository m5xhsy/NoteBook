创建对象
    var person = {};
        person.name = 'Ass';
        person.age = 18;
        person.func = function(){
            alert(this.name);
        }
        person.func();

    字面量方式
        var person={
            name:'Ass';
            age:18;
            func:function{
                alert(this.name)
            }
        }
        person.func();

    工厂方式
        var groupObjects = function(name,age){
            var person = {};
            person.name = name;
            person.age = age;
            person.func = function(){
                alert(this.name);
            }
            return person;
        }
        f1 = groupObjects('aaa',18)
        f2 = groupObjects('bbb',13)

    方式四
        function person(name,age){
            this.name = name;
            this.age = age;
            this.func = function(){
                alert(this.name)
            }
        }
        var v1 = new person('aaa',18);
        v1.func();

    原型
        function person(name,age){
            this.name = name;
            this.age = age;
        }
        person.prototype.showName(){         //person.protoype指person的父类。showName为父类的方法
            alert(this.name);
        }
        var vs = person('aaa',18);
        vs.showName();