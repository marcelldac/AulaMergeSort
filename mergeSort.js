let lista = [1,2,5,45,36,4,3653,4,23,6];

// push() : Adiciona um novo elemento ao final do array
// Operador condicional terciário : condição ? expressão1 : expressão2
// shift() : Remove o primeiro elemento do array e retorna ele.
//Math.floor() : Arredonda o float para baixo e o transforma em inteiro.
//slice() : Retorna um subarray a partir do array informado.

function merge (a,b) {
    var result = [];
    while (a.length >0 && b.length >0)
        result.push(a[0] < b[0]? a.shift() : b.shift());
    return result.concat(a.length? a : b);
}

function mergeSort (arr) {
    if (arr.length < 2) return arr;
    var mid = Math.floor(arr.length /2);
    var subLeft = mergeSort(arr.slice(0,mid));
    var subRight = mergeSort(arr.slice(mid));
    return merge(subLeft, subRight);
}

console.log(mergeSort(lista));