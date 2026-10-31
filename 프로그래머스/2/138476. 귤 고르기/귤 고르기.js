function solution(k, tangerine) {
    const tanger_obj = {}
    
    
    tangerine.forEach((e) => {
        tanger_obj[e] = (tanger_obj[e] || 0 ) + 1
    })
    
    // console.log(tanger_obj)
    
    sorted_tanger = (Object.values(tanger_obj).sort((a, b) => b - a))
    
    let answer = 0
    
    for (element of sorted_tanger){
        if (k <=0) {
            break
        }
        k -= element
        answer += 1
    }
    return answer
}