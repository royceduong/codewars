function getCombinations(list){
    result = []
    for(var i = 0; i < list.length; i++){
        for( var j = i+1; j < list.length; j++){
            result.push([i,j])
        }
    }
    console.log(result)
}

getCombinations([1,2,3,4], 2)