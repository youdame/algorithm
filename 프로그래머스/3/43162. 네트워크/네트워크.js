function solution(n, computers) {
  const adjList = {};

  computers.forEach((connection, currentComputer) => {
    connection.forEach((element, index) => {
      if (element === 0) {
        return;
      }
      if (!adjList[currentComputer]) {
        adjList[currentComputer] = [];
      }
      if (index !== currentComputer) {
        adjList[currentComputer].push(index);
      }
    });
  });

  const visited = new Set();

  const dfs = (node, visited) => {
    if (visited.has(node)) {
      return;
    }

    visited.add(node);
    (adjList[node] ?? []).forEach((neighbor) => dfs(neighbor, visited));
  };

  let answer = 0;
  for (let i = 0; i < n; i++) {
    if (!visited.has(i)) {
      dfs(i, visited);
      answer += 1;
    }
  }
  return answer;
}