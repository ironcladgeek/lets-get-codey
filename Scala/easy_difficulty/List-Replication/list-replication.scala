def f(num:Int, arr:List[Int]):List[Int] = {
    arr.map(List.fill(num)(_)).flatten
}