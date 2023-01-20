func asd(a, b){
        return a + b
}
func fib(n){
    if(n == 1){
        return 1
    } 
    if(n == 2){
        return 1
    } else {
        return fib(n - 1) + fib(n - 2)
    }
}
func fact(n){
    if(n == 0){
        return 1
    } else {
        return n * fact(n - 1)
    }
}
func change_var(){
    
}

func pow(a, b){
    var powr = a
    for (var i = b; i > 1; i--){
        powr = powr * a
    }
    return powr
}

print(pow(2, 5))

func hanoi(n, from, to, via){
    if(n == 1){
        print("Move disk from " + from + " to " + to)
    } else {
        if(n == 2){
            print("Move disk from " + from + " to " + via)
            print("Move disk from " + from + " to " + to)
            print("Move disk from " + via + " to " + to)
            
            return
        }
        hanoi(n - 1, from, via, to)
        print("Move disk from " + from + " to " + to)
        hanoi(n - 1, via, to, from)
    }
}


//simulator(hard_mode, 1000)
//unit(archer_b,5, "red", hard, hard_fuzzy_strategy) -> simulator
//unit(archer_b,5, "blue", hard, hard_fuzzy_strategy) -> simulator
//field(10, 10) -> simulator
//random_allocate
//simulator
//print(fib(8))
//print(fact(10))

hanoi(5, "A", "C", "B")
