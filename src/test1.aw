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


simulator(hard_mode, 1000)
unit(archer_b,5, "red", hard, hard_fuzzy_strategy) -> simulator
unit(archer_b,5, "blue", hard, hard_fuzzy_strategy) -> simulator
field(10, 10) -> simulator
random_allocate
//simulator
//print(fib(8))
//print(fact(10))
