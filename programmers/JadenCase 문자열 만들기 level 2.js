function solution(s) {
    s=s.toLowerCase().split('')
    s[0]=s[0].toUpperCase()
    for(let i=0; i<s.length-1;i++)
        {
            if(isNaN(s[i+1]) && s[i]==' ' )
                s[i+1]=s[i+1].toUpperCase()
        }
    return s.join('')

}