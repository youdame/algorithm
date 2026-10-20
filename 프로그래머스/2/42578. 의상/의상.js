function solution(clothes) {
    let answer = 1
    
    const record = {}
    clothes.forEach((e) => {
        const [name, category] = e
        
        if (category in record){
            record[category].push(name)
        } else {
            record[category] = [name]
        }
        
        
    })
    for (const key of Object.keys(record)){
        answer *= record[key].length + 1
    }
    
    return answer - 1
    
}