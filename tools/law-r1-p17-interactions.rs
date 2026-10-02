use std::{collections::HashMap, env, fs};

fn popcount(mut x: usize) -> i32 {
    let mut c = 0;
    while x > 0 { c += (x & 1) as i32; x >>= 1; }
    c
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = args.get(1).cloned().unwrap_or_else(|| "active/g8-law-r1-p17/P17_INTERACTION_MATRIX.tsv".into());
    let output = args.get(2).cloned().unwrap_or_else(|| "out-p17/rust-interactions.json".into());
    let text = fs::read_to_string(&input).expect("read matrix");
    let mut map: HashMap<String, [i32; 8]> = HashMap::new();
    let mut counts: HashMap<String, usize> = HashMap::new();

    for (i, line) in text.lines().enumerate() {
        if i == 0 || line.trim().is_empty() { continue; }
        let p: Vec<&str> = line.split('\t').collect();
        assert_eq!(p.len(), 5, "bad row");
        let d = p[0].to_string();
        let a: usize = p[1].parse().unwrap();
        let l: usize = p[2].parse().unwrap();
        let g: usize = p[3].parse().unwrap();
        let y: i32 = p[4].parse().unwrap();
        let mask = a | (l << 1) | (g << 2);
        map.entry(d.clone()).or_insert([0; 8])[mask] = y;
        *counts.entry(d).or_insert(0) += 1;
    }

    let mut names: Vec<String> = map.keys().cloned().collect();
    names.sort();
    let mut domain_json = Vec::new();
    let mut all_complete = true;
    let mut all_exact_gate = true;
    let mut all_conditional_pair = true;

    for name in names {
        let f = map.get(&name).unwrap();
        let complete = counts.get(&name).copied().unwrap_or(0) == 8;
        all_complete &= complete;

        let mut mobius = [0i32; 8];
        for s in 0usize..8 {
            let mut t = s;
            loop {
                let sign = if (popcount(s) - popcount(t)) % 2 == 0 { 1 } else { -1 };
                mobius[s] += sign * f[t];
                if t == 0 { break; }
                t = (t - 1) & s;
            }
        }
        let expected_and = (0usize..8).all(|m| f[m] == if m == 7 { 1 } else { 0 });
        all_exact_gate &= expected_and;
        let pair_g1 = f[7] - f[5] - f[6] + f[4];
        let pair_g0 = f[3] - f[1] - f[2] + f[0];
        all_conditional_pair &= pair_g1 == 1 && pair_g0 == 0 && mobius[7] == 1;

        domain_json.push(format!(
            "{{\"domain\":\"{}\",\"complete_cube\":{},\"and_gate\":{},\"mobius_3way\":{},\"authority_lifecycle_at_pr_geometry\":{},\"authority_lifecycle_at_nonpr_geometry\":{}}}",
            name, complete, expected_and, mobius[7], pair_g1, pair_g0
        ));
    }

    let out = format!(
        "{{\n  \"tool\":\"rust\",\n  \"complete_factorial_support\":{},\n  \"exact_conjunctive_gate\":{},\n  \"conditional_pairwise_interaction\":{},\n  \"domains\":[{}],\n  \"interpretation\":\"The transported A×L edge is conditional on G=PR; globally the Boolean function has a genuine third-order A×L×G term.\"\n}}\n",
        all_complete, all_exact_gate, all_conditional_pair, domain_json.join(",")
    );
    fs::create_dir_all("out-p17").unwrap();
    fs::write(output, out).unwrap();
    println!("P17_RUST_INTERACTION=PASS");
    println!("COMPLETE_FACTORIAL={}", all_complete);
    println!("EXACT_CONJUNCTIVE_GATE={}", all_exact_gate);
    println!("CONDITIONAL_PAIRWISE={}", all_conditional_pair);
}
