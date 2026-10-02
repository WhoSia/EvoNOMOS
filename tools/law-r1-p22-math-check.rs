use std::collections::HashSet;
use std::fs;

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
enum S { Present, Lost }

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Edge { Carry, Drop, Repair }

fn apply(e: Edge, s: S) -> S {
    match e {
        Edge::Carry => s,
        Edge::Drop => S::Lost,
        Edge::Repair => S::Present,
    }
}

fn run(path: &[Edge], mut s: S) -> S {
    for &e in path { s = apply(e, s); }
    s
}

fn all_edges_carry(bits: &[bool]) -> bool { bits.iter().all(|&x| x) }
fn no_gap(bits: &[bool]) -> bool { !bits.iter().any(|&x| !x) }

fn enumerate_binary(n: usize, prefix: &mut Vec<bool>, out: &mut Vec<Vec<bool>>) {
    if prefix.len() == n { out.push(prefix.clone()); return; }
    prefix.push(false); enumerate_binary(n,prefix,out); prefix.pop();
    prefix.push(true); enumerate_binary(n,prefix,out); prefix.pop();
}

fn main() {
    for n in 0..=10 {
        let mut rows=Vec::new();
        enumerate_binary(n,&mut Vec::new(),&mut rows);
        for r in rows {
            assert_eq!(all_edges_carry(&r), no_gap(&r));
        }
    }

    for n in 0..=8 {
        let mut rows=Vec::new();
        enumerate_binary(n,&mut Vec::new(),&mut rows);
        for r in rows {
            let path: Vec<Edge> = r.iter().map(|&b| if b {Edge::Carry}else{Edge::Drop}).collect();
            let expected = if r.iter().all(|&b| b) {S::Present} else {S::Lost};
            assert_eq!(run(&path,S::Present), expected);
        }
    }

    let gap_then_repair = run(&[Edge::Drop,Edge::Repair], S::Present);
    let repair_then_gap = run(&[Edge::Repair,Edge::Drop], S::Present);
    assert_eq!(gap_then_repair,S::Present);
    assert_eq!(repair_then_gap,S::Lost);
    assert_ne!(gap_then_repair,repair_then_gap);

    let mut outputs=HashSet::new();
    outputs.insert(run(&[Edge::Drop],S::Present));
    outputs.insert(run(&[Edge::Drop,Edge::Repair],S::Present));
    assert_eq!(outputs.len(),2);

    let prop_a = run(&[Edge::Carry], S::Present);
    let prop_b = run(&[Edge::Drop], S::Present);
    assert_ne!(prop_a,prop_b);

    fs::create_dir_all("out-p22").unwrap();
    fs::write(
        "out-p22/p22-math.json",
        r#"{
  "stage":"EvoNOMOS Generation VIII LAW-R1-P22",
  "status":"PASS",
  "BOOLEAN_R4_R5_EQUIVALENCE":"PASS",
  "IRREVERSIBLE_BOOLEAN_QUOTIENT":"PASS",
  "REPAIR_BREAKS_QUOTIENT":"PASS",
  "NONCOMMUTATIVE_WITNESS":"PASS",
  "PROPERTY_INDEXED_WITNESS":"PASS",
  "GAP_THEN_REPAIR":"PRESENT",
  "REPAIR_THEN_GAP":"LOST"
}
"#,
    ).unwrap();

    println!("P22_MATH_CHECK=PASS");
    println!("BOOLEAN_R4_R5_EQUIVALENCE=PASS");
    println!("IRREVERSIBLE_BOOLEAN_QUOTIENT=PASS");
    println!("REPAIR_BREAKS_QUOTIENT=PASS");
    println!("NONCOMMUTATIVE_WITNESS=PASS");
    println!("PROPERTY_INDEXED_WITNESS=PASS");
}
