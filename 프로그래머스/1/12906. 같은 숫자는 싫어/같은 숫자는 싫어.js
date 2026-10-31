function solution(arr)
{
    
    const answer = []

    arr.forEach((e, i) => {
        
        if (e === arr[i+1]){
            
        } else{
            answer.push(e)
            
        }
        
    })
    return answer
}