// var CreateHellWorld = function() {
//     return function(){
//         return "Hello World";
//     }
// };

// console.log(CreateHellWorld()());

// function HellWorld() {
//     return "Hello World!";
// }

// console.log(HellWorld);

var HellWorld2 = function() {
    return function(...args){
        return "Hello World!";
    }
};

console.log(HellWorld2()());