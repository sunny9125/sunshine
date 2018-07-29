//ES5 中常量的写法

Object.defineProperty(window,"PI2",{
    value:3.1415926,
    writeable:false,
})

// ES6 的常量写法

const PI =3.1415926
console.log(PI)

//PI = 4