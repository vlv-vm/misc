const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
canvas.width = 1000;
canvas.height = 1000;
const cellSize = 25;
const row = canvas.width / cellSize;

//ctx.fillStyle = "green";
//ctx.fillRect(0,0,canvas.width,canvas.height)

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
            //console.log(grid[i][j])
            const cell = grid[i][j];
            ctx.beginPath();
            ctx.rect(j*cellSize, i*cellSize, cellSize, cellSize);
            ctx.fillStyle = cell ? "black" : "white";
            ctx.fill();
            ctx.stroke();
        }
    }
}

/* 
Any live cell with fewer than two live neighbours dies, as if by underpopulation.   *live cell <2 neigh die
Any live cell with two or three live neighbours lives on to the next generation.    *live cell =2 || =3 neigh lives
Any live cell with more than three live neighbours dies, as if by overpopulation.   *live cell >3 neigh die
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction. dead cell =3 neigh live
*/
function nextGeneration(grid){
    
    let nextGenArr = grid.map(arr => [...arr]);
    //let nextGenArr = JSON.parse(JSON.stringify(grid));
    console.log("This is nextgen")
    console.table(nextGenArr);
    /*
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[i].length;j++){
            if(grid[i][j]===nextGenArr[i][j]){
                console.log("True")
            }else{
                console.log("False")
            }
        }
    }
    */
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[i].length; j++){
            let count = 0;
            if(i >= 1 && j >= 1 && i<grid.length-1 && j<grid[i].length-1){
                count = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]; 
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
    }
    console.log("This is after calc");
    console.table(nextGenArr);
    return nextGenArr;

}

let newGrid = createGrid();
renderGrid(newGrid);

//grid = nextGeneration(newGrid)

setTimeout(requestAnimationFrame(update), "2000");


function update(){
    newGrid = nextGeneration(newGrid)
    renderGrid(newGrid);
    requestAnimationFrame(update)
}