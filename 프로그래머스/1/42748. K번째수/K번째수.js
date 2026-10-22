function solution(array, commands) {
    const answer = []
    for (command of commands){
        const [start, end, index] = command

        sliced_arr = array.slice(start-1, end)
        
        sliced_arr.sort((a, b) => a-b)
        answer.push(sliced_arr[index-1])
    }
    return answer
}