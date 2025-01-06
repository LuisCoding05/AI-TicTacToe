const board = document.getElementById("board");
const estado = document.getElementById("status");
const resetButton = document.getElementById("reset");

let gameBoard = ["", "", "", "", "", "", "", "", ""];
let isPlayerTurn = true;
let finished = false;
let result = null;
// Crea el tablero
function createBoard() {
    board.innerHTML = "";
    gameBoard.forEach((cell, index) => {
        const cellDiv = document.createElement("div");
        cellDiv.classList.add("cell");
        cellDiv.dataset.index = index;
        cellDiv.classList.add("notTaken");
        cellDiv.textContent = cell;
        cellDiv.addEventListener("click", handlePlayerMove);
        board.appendChild(cellDiv);
    });
}

// Maneja el turno del jugador
function handlePlayerMove(event) {
    if (!isPlayerTurn) return;

    const index = event.target.dataset.index;
    if (gameBoard[index] !== "") return;

    gameBoard[index] = "X";
    isPlayerTurn = false;
    updateBoard();

    checkWinner("X");
    if (!finished) {
        setTimeout(() => {
            getAIMove();
        }, 250);
    }
}

// Solicita la jugada de la IA al servidor
async function getAIMove() {
    let IAWin;
    //Le manda al backend el tablero
    const response = await fetch("/ai_move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ board: gameBoard }),
    });
    //Recibe la respuesta de la IA
    const data = await response.json();
    if (data.move !== null) {
        gameBoard[data.move] = "O";
        updateBoard();
        IAWin = checkWinner("O");
    }
    //Si no ha ganado la IA devuelve true
    if (!IAWin) {
        isPlayerTurn = true;
    }
}

// Actualiza el tablero
function updateBoard() {
    const cells = document.querySelectorAll(".cell");
    cells.forEach((cell, index) => {
        cell.textContent = gameBoard[index];
        switch (gameBoard[index]) {
            case "":
                cell.classList.add("notTaken");
                break;
            case "X":
                cell.classList.add("purple");
                cell.classList.add("taken");
                cell.classList.remove("notTaken");
                break;
            case "O":
                cell.classList.add("blue");
                cell.classList.add("taken");
                cell.classList.remove("notTaken");
                break;
            default:
                break;
        }
    });
}

// Comprueba si hay un ganador
function checkWinner(player) {
    const winningCombos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];
    // comprueba cada posible condicion de victoria
    for (let combo of winningCombos) {
        if (combo.every((index) => gameBoard[index] === player)) {
            estado.textContent = `${player} gana!`;
            isPlayerTurn = false;
            finished = true;
            result = (player === "X" ? "victory" : "defeat")
            updateStatistics(result);
            return finished;
        }
    }
    //si ninguna posición está vacía el resultado es un empate
    if (!gameBoard.includes("")) {
        estado.textContent = "Empate!";
        isPlayerTurn = false;
        finished = true;
        result = "draw";
        updateStatistics(result);
        return finished;
    }
    return finished;
}

//Publica los resultados
async function updateStatistics(result) {
    await fetch("/update_statistics", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ result: result }),
    });
}

// Reinicia el juego
resetButton.addEventListener("click", () => {
    gameBoard = ["", "", "", "", "", "", "", "", ""];
    isPlayerTurn = true;
    finished = false;
    estado.textContent = "";
    createBoard();
});

// Inicializa el tablero
createBoard();
