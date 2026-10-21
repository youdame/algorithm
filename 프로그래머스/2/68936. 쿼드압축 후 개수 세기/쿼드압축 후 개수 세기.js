function solution(arr) {
    const answer = [0, 0]
    
    
    function 압축가능여부(x, y, len){
        let possible = true
        const start = arr[x][y]
        
        for (let i= x; i < x + len; i+= 1) {
            for (let j = y; j < y + len; j+=1) {
                if (arr[i][j] !== start){
                    possible = false
                    break
                }
            }
        }
        return possible
        
        return possible
        
    }
    
    function dfs(x, y, len){
        if (압축가능여부(x, y, len)){
            answer[arr[x][y]] += 1
            return
        }
        else {
            dfs(x, y, len / 2)
            dfs(x, y + len / 2, len / 2)
            dfs(x + len / 2 , y, len / 2)
            dfs(x + len / 2, y + len / 2, len / 2)
        }
    }
    
    dfs(0, 0, arr.length)
    
    return answer
        
    
}