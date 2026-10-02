fn main() {
    let tables: [(&str,[u8;4]);8] = [
        ("AND",   [0,0,0,1]),
        ("OR",    [0,1,1,1]),
        ("XOR",   [0,1,1,0]),
        ("Q_ONLY",[0,0,1,1]),
        ("G_ONLY",[0,1,0,1]),
        ("NOR",   [1,0,0,0]),
        ("NAND",  [1,1,1,0]),
        ("XNOR",  [1,0,0,1]),
    ];
    let target=[0,0,0,1];
    let matches: Vec<&str> = tables.iter().filter(|(_,t)| *t==target).map(|(n,_)|*n).collect();
    let mut distinct=true;
    for i in 0..tables.len() {
        for j in i+1..tables.len() {
            if tables[i].1==tables[j].1 { distinct=false; }
        }
    }
    let pass=matches==vec!["AND"] && distinct;
    println!("P25_MATH={}", if pass {"PASS"} else {"FAIL"});
    println!("AND_PACKET_MATCH={:?}", matches);
    println!("FROZEN_STANDARD_RIVALS_DISTINCT={}", distinct);
    if !pass { std::process::exit(2); }
}
