use std::fs;
use std::process::Command;

fn bin() -> &'static str {
    env!("CARGO_BIN_EXE_aichat")
}

#[test]
fn records_exact_contract_arguments_and_streams_deterministic_text() {
    let record = std::env::temp_dir().join(format!("evonomos-aichat-{}.json", std::process::id()));
    let output = Command::new(bin())
        .args(["-m", "fixture:model", "-s", "fixture-session", "-f", "C:\\fixture path\\doc.pdf", "question with spaces"])
        .env("EVONOMOS_AICHAT_RECORD", &record)
        .output()
        .unwrap();
    assert!(output.status.success());
    assert_eq!(output.stdout, b"ORACLE_ALPHA ORACLE_BETA\n");
    assert_eq!(fs::read_to_string(&record).unwrap(), "{\"argv\":[\"-m\",\"fixture:model\",\"-s\",\"fixture-session\",\"-f\",\"C:\\\\fixture path\\\\doc.pdf\",\"question with spaces\"]}\n");
    let _ = fs::remove_file(record);
}

#[test]
fn exposes_nonzero_and_invalid_modes() {
    let failed = Command::new(bin()).env("EVONOMOS_AICHAT_MODE", "nonzero").output().unwrap();
    assert_eq!(failed.status.code(), Some(23));
    let invalid = Command::new(bin()).env("EVONOMOS_AICHAT_MODE", "invalid").output().unwrap();
    assert!(invalid.status.success());
    assert!(invalid.stdout.contains(&0));
}
