var reverseString = function(s) {
    var array = s.split('')
    var result = "hello World"
    for(var i = 0; i < array.length/2; i++){
        var temp = array[array.length-1-i]
        array[array.length-1-i] = array[i]
        array[i] = temp
    }
    var result = array.join('')
    return result;
};