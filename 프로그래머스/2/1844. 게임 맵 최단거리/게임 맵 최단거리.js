function solution(maps) {

    const queue = [[0, 0]]
    let head = 0
    
    
    const n = maps.length
    const m = maps[0].length
    const dist = Array.from({length : n }, () => Array(m).fill(-1))
    
   
    dist[0][0] = 1
    
    while (head < queue.length) {
        const [y, x] = queue[head++]
        
        for (const [dy, dx] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
            
            const ny = dy + y
            const nx = dx + x
            
            if (0 <= ny && ny < n && 0 <= nx && nx < m){
                if (dist[ny][nx] == -1 && maps[ny][nx] == 1){
                    dist[ny][nx] = dist[y][x] + 1
                    queue.push([ny, nx])
                    
                }
            }
            
        }
        
    }
    return dist[n-1][m-1]
    

}