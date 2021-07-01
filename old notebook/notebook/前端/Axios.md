### 安装

```shell
$ cnpm i axios -S
```

### 使用

get请求

```javascript
axios.get('/user?id=123')						//   '/user?id=123'	
.then((res)=>{
		return res
})
.catch((err)=>{
		return err
})

axios.get('/user',{					//   '/user/123'
   	 params:{
         id:123
     }
})
```



post请求