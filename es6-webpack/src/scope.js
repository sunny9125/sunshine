//ES5 中的作用域
const callbacks=[];
for(var i=0;i<=2;i++){
    callbacks[i] = function(){
        return i*2
    }
}

console.table([
    callbacks[0](),
    callbacks[1](),
    callbacks[2](),
])

//ES5中的变量会进行变量提升。callbacks对变量的引用而不是变量值的引用。i变量为闭包作用域。

const callbacks2=[];
for(let j=0;j<=2;j++){
    callbacks2[j] = function(){
        return j*2
    }
}

console.table([
    callbacks2[0](),
    callbacks2[1](),
    callbacks2[2](),
]);

//ES5 用立即执行函数来隔离变量的作用域
(function(){
    var foo=function(){
        return 1
    }
    console.log('foo()===1',foo() === 1);
    ((function(){
        const foo = function(){
            return 2
        }
        console.log("foo()===2",foo() ===2)
    })())
})()

//ES6 块作用域
{
    function foo(){
        return 1
    }
    console.log('foo()===1',foo()===1)
    {
        function foo(){
            return 2
        }
        console.log("foo()===2",foo()===2)
    }
    console.log('foo()===1',foo()===1)
}