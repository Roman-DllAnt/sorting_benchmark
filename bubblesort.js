

function bubbleSort(array_input) {
    alert("Was executed")
    array_input = [12,4,14,89,53]
    
    let condition = true 
    while (condition) {
        let swaps = 0
        for (let a = 0; a < (length(array_input)-1); a++) {
            if (array_input[a]>array_input[a+1]){
                let mem = array_input[a];
                array[a] = array_input[a+1];
                array[a+1] = mem;
                swaps ++
            }
        if (swaps = 0) {
            condition = false
        }
        }
    }
    return (array_input)
}

let array_to_sort = [12,4,14,89,53]
console.log(bubbleSort(array_to_sort));
