const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
canvas.width = 1000;
canvas.height = 1000;
const cellSize = 10;
const row = canvas.width / cellSize;

const button = document.querySelector("button");

button.addEventListener("click", ()=>{
    let newGrid = createGrid();
    renderGrid(newGrid);
    requestAnimationFrame(update)
    update();
});

function createGrid(){
    let grid = new Array(row).fill(null);
    for(let i = 0; i < row;i++){
        for(let j = 0; j < row; j++){
            grid[i] = new Array(row).fill(null).map(()=>Math.floor(Math.random()*2));
        }
    }
    console.table(grid);
    return grid;
}

function renderGrid(grid){
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[i].length;j++){
            const cell = grid[i][j];
            ctx.beginPath();
            ctx.rect(j*cellSize, i*cellSize, cellSize, cellSize);
            ctx.fillStyle = cell ? "purple" : "white";
            ctx.fill();
            ctx.stroke();
        }
    }
}

/* 
Any live cell with fewer than two live neighbours dies, as if by underpopulation.   
Any live cell with two or three live neighbours lives on to the next generation.    
Any live cell with more than three live neighbours dies, as if by overpopulation.   
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction. 
*/

function nextGeneration(grid){
    
    let nextGenArr = grid.map(arr => [...arr]);
    
    console.log("This is nextgen")
    console.table(nextGenArr);
   
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[i].length; j++){
            let count = 0;
            count = doa(i-1, j-1, grid) + doa(i-1, j, grid) + doa(i-1, j+1, grid) + doa(i, j-1, grid) + doa(i, j+1, grid) + doa(i+1, j-1, grid) + doa(i+1, j, grid) + doa(i+1, j+1, grid)

            if(grid[i][j] === 1 && (count < 2 || count > 3)){
                nextGenArr[i][j] = 0;
            }
            if(grid[i][j] === 1 && (count === 2 || count === 3)){
                nextGenArr[i][j] = 1;
            }
            if(grid[i][j] === 0 && count === 3){
                nextGenArr[i][j] = 1;
            } 
        }
    }
    console.log("This is after calc");
    console.table(nextGenArr);
    return nextGenArr;

}

function doa(x, y, grid){
    if(x < 0 || x >= grid.length || y < 0 || y >= grid.length){
        return 0
    }
    
    return grid[x][y] ? 1:0;
}


let newGrid = createGrid();
renderGrid(newGrid);

requestAnimationFrame(update);

function update(){
    setTimeout(() =>{
        newGrid = nextGeneration(newGrid);
        renderGrid(newGrid);
        requestAnimationFrame(update);
    }, 25)
    
}