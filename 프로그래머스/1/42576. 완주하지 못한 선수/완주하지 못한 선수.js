function solution(participant, completion) {
    const map = {}
    participant.forEach((element) => {
        map[element] = (map[element] || 0) + 1
    })
    
    // console.log(map)
    
    for (const com of completion){
        map[com] -= 1 
    }
    
    for (const player in map){
        if (map[player] > 0 ){
            return player
            }
            
    }
    
    
    return participant.join("")
}