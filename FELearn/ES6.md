 
##ECMAScript_6学习
###ECMAScript_6简介
1. 查看node已经实现的ES6特性：`node --v8-options | grep harmony`


####Babel转码器
1. Babel是ES6转码器。 
2. 配置文件是：.babeIrc。 presets字段设定转码规则。
3. 命令行转码babel-cli Bable提供babel-cli工具，用于命令行转码。 全局安装命令为：`npm install --global babel-cli` 项目安装命令：`npm install --save-dev babel-cli`

 ```
 babel example.js  #转码结果输出到标准输出
 指定输出文件 -o/--out-file 
 指定输出目录  -d/--out-dir
 
 ```
4. 转码的命令 `npm run build`


###let和const命令

#### let命令
1. let命令用来声明变量。他的用法类似于var，但是所声明的变量只能在let命令所在的代码块内有效。 for循环的计数器，很适合使用let命令。

	```
	#用var声明for循环中的变量
	for (var i=0;i<10;i++){
	... a[i] = function(){
	..... console.log(i);
	..... };
	... }
	[Function]
	> a[6]();
	10
	#上述for循环中的var变量，全局范围内有效，所以数组a[]的成员里面的i值指向的都是同一个i值。
	
	#用let声明for循环中的变量
	for (let i = 0;i<10;i++){
	... a[i] = function(){
	..... console.log(i);
	..... };
	... }
	[Function]
	> a[6]();
	6
	#上述for循环中的let变量，i值只在本轮for循环中有效
	```
2. for循环的一个特别之处，设置循环变量的那部分是个父作用域，而循环体内部是一个单独的子作用域。

   ```
    for (let i = 0;i<3;i++){
    ... let i = 'abc';
    ... console.log(i);
    ... }
    abc
    abc
    abc
    undefined
    ```
3. 不存在变量提升。 var变量可以在声明之前使用，其值为undefined。let变量必须在变量声明之后才能使用。
4. 暂时性死区  :如果代码块内存在let和const命令，这个区块对这些命令声明的变量，从一开始就形成了封闭作用域。凡是在声明之前就使用这些变量，就会报错。  总之在代码块内，使用let命令声明变量之前，该变量都是不可用的。 暂时性死区也就意味着typeof不再是一个百分之百安全的操作。 

```
#let变量在声明之前 typeof也是不可用的
> typeof y; let y;
ReferenceError: y is not defined

#其实一个变量在声明之前，直接用typeof是不会报错的。和let变量里面有点冲突。
> typeof undefine_value
'undefined'

#不容易发现的死区
1.
function bar(x=y,y=2){
... return [x,y]
... }
undefined
> bar();
ReferenceError: y is not defined
    at bar (repl:1:16)
#如果换个顺序就不会报错
> function bar2(x=2,y=x){
... return[x,y];
... }
undefined
> bar2()
[ 2, 2 ]
2.
> var x=x
undefined
> let y=y
ReferenceError: y is not defined

```
暂时性死区的本质：只要已进入当前作用域，索要使用的变量就已经存在了，但是不可获取，只有等到声明变量的那一行代码出现，才可以获取和使用该变量。
5. 不允许重复声明。let不允许在相同作用域内，重复声明同一个变量。

```node
#在相同作用域，重复声明同一个变量会报错
function func1(){
... let a =10;
... var a = 1;
... }
undefined
> func1();
SyntaxError: Identifier 'a' has already been declared
#在相同作用域，重复声明同一个let变量会报错
> function func2(){
... let a =10;
... let a = 1;
... }
undefined
> func2();
SyntaxError: Identifier 'a' has already been declared
#不能在函数内部重新声明参数
> function func3(arg){
... let arg;
... }
undefined
> func3(2)
SyntaxError: Identifier 'arg' has already been declared
#在不同函数内部重新声明变量时可以的
> function fun4(arg){
... {
..... let arg;
..... }
... }
undefined
> fun4(3);
undefined
```
####块级作用域
1. ES5只有全局作用域和函数作用域，没有块级作用域。会存在一些不合理的场景。

   ```
#内部变量会覆盖外层变量
> var tmp = new Date();
undefined
> function f(){
... console.log(tmp);
... if(false){
..... var tmp = 'hello world';
..... }
... }
undefined
> f();
undefined
undefined
#用来计数的循环变量泄露为全局变量
> var s = 'hello';
undefined
> for (var i =0;i<s.length;i++){
... console.log(s[i]);
... }
h
e
l
l
o
undefined
> console.log(i);
5
undefined
```
2. ES6的块级作用域：let为js新增了块级作用域。

   ```
#外层代码块和内层代码快内都声明了变量n，但是变量互不影响。
> function f1(){
... let n  =5;
... if (true){
..... let n = 10;
..... }
... console.log(n);
... }
undefined
> f1();
5
undefined
```
3. ES6允许块级作用域的任意嵌套。外层作用域无法访问内层作用域的变量。内层作用域可以定义外层作用域的同名变量。

   ```
  #变量可以嵌套多层作用域
   > {{{{{let insane ='hello world'}}}}}
undefined
#外层作用域不能访问内层作用域的变量
> {{{{{let insane = 'hello world'} console.log(insane);}}}}
ReferenceError: insane is not defined
#内层作用域可以定义外层作用域的同名变量
> {{{{{let insane = 'hello world'} let insane = 'nihao';}}}}
undefined
```
4. 块级作用域的出现，实际上使得广泛应用的立即执行函数表达式不再必要了。
5. 允许在块级作用域内声明函数。函数声明类似于var，即会提升到全局作用域或者函数作用域的头部。 函数声明还会提升到所在的块级作用域的头部。
6. 推荐使用函数表达式，而不是函数声明语句。

   ```
   // 函数声明语句
{
  let a = 'secret';
  function f() {
    return a;
  }
}

// 函数表达式
{
  let a = 'secret';
  let f = function () {
    return a;
  };
}
```
6. ES6的块级作用域允许声明函数的规则，只在使用大括号的情况下城里，如果没有使用大括号，就会报错。
    
####const命令
1. const声明一个只读变量。一旦声明，变量的值就不能改变了。const一旦声明变量，就必须立即初始化，不能留到以后赋值(只声明不赋值就会报错)。
2. const的作用域与let命令相同：只在声明所在的块级作用域内有效。
3. const变量也是不提升，会存在暂时性死区，只能在声明的位置后面使用。
4. const声明的变量也与let一样不可重复声明。
5. const的本质是变量所指向的内存地址所保存的数据不得改动。

```
  
   #常亮foo存储的是一个地址，这个地址指向一个对象，不能把foo指向另一个对象，但对象本身是可变的，可以为变量添加新属性
   > const foo={};
	undefined
	> foo.prop =123;
	123
		> foo.prop
	123
	> foo={};
		TypeError: Assignment to constant variable.
	  #常量a是一个数组，这个数组本身是可写的，但是如果将另一个数组赋值给a就会报错
	> const a = [];
		undefined
	> a.push('hello');
	1
	> a.length=0
	0
	> a=['dave']
		TypeError: Assignment to constant variable.
	>
```
   
####顶层对象的属性
1. 顶层对象的属性赋值与全局变量的赋值，是同一件事。
2. ES6中，var命令和function命令声明的全局变量依旧是顶层对象属性；let和const，class命令声明的全局变量，不属于顶层对象的属性。从ES6开始，全局变量将逐步与顶层对象的属性脱钩。

####global对象