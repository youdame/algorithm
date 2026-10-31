function solution(bridge_length, weight, truck_weights) {
    
    const wait_queue = truck_weights
    let w_head = 0
    
    
    const bridge_queue = []
    let b_head = 0

    
    let time = 0
    
    while ((w_head < wait_queue.length || b_head < bridge_queue.length)){
        time += 1 
        
        // 다리에서 트럭 내보내기
        if (b_head < bridge_queue.length && time - bridge_queue[b_head][0] == bridge_length){
            b_head++ 
        }
        
        // 다리에 새 트럭 올리기 
        
        const sum = bridge_queue.slice(b_head).reduce((acc, element, index) => element[1] + acc, 0)
        const node = wait_queue[w_head]
        
        if (sum + node <= weight) {
            bridge_queue.push([time, node])
            w_head ++ 
        }

        // console.log(bridge_queue, wait_queue)
        
        
    }
    
    return time
    
    
        
}