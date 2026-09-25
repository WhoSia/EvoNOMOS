use std::env;
use std::fs;
use std::io::{self, Write};
use std::process;

fn json_escape(s: &str) -> String {
    let mut out = String::with_capacity(s.len() + 8);
    for ch in s.chars() {
        match ch {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if c.is_control() => out.push_str(&format!("\\u{:04x}", c as u32)),
            c => out.push(c),
        }
    }
    out
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if let Ok(path) = env::var("EVONOMOS_AICHAT_RECORD") {
        let encoded = args
            .iter()
            .map(|a| format!("\"{}\"", json_escape(a)))
            .collect::<Vec<_>>()
            .join(",");
        fs::write(path, format!("{{\"argv\":[{}]}}\n", encoded)).expect("write invocation record");
    }

    match env::var("EVONOMOS_AICHAT_MODE").as_deref() {
        Ok("nonzero") => {
            eprintln!("deterministic fake failure");
            process::exit(23);
        }
        Ok("invalid") => {
            io::stdout().write_all(b"invalid\0payload\n").unwrap();
        }
        _ => {
            let mut stdout = io::stdout().lock();
            stdout.write_all(b"ORACLE_ALPHA ").unwrap();
            stdout.flush().unwrap();
            stdout.write_all(b"ORACLE_BETA\n").unwrap();
        }
    }
}
