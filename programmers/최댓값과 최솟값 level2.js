function solution(s) {
    s= s.split(' ').map(ele=>parseInt(ele))
    max =Math.max(...s)
    min = Math.min(...s)

    return `${min} ${max}`
}